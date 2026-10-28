# Recur — product spec

## The problem

Small businesses increasingly get paid by instant transfer: Zelle, ACH and wire in the US, bank transfers and Paystack in Nigeria, and the same pattern on UPI, Pix and M-Pesa elsewhere. The money arrives in one place, but the proof arrives everywhere else: a screenshot in a chat, a voice note saying "I've sent it", a PDF remittance, a bank alert email. Someone has to match each one to an invoice by hand, chase the customers who have not paid, and catch the ones who claim to have paid but have not. Fake payment screenshots are a common scam wherever instant transfers exist, and sellers who trust the picture release goods for money that never arrived.

## The product in one sentence

Recur reads every kind of payment proof, checks it against the money that actually arrived, and closes the right invoice only when it can prove the payment is real.

## Who it is for

The owner or bookkeeper of a business that sends invoices to other people or businesses: an agency, a wholesaler, a contractor, a clinic's billing desk, a school's bursar. They have between 20 and 2,000 open invoices and no finance team.

Demo company for the US: **Northwind Studio**, a small design agency in Austin, billing in USD. Demo company for Nigeria: **Adaeze Fabrics**, a fabric wholesaler in Lagos, billing in NGN. The app supports both currencies in the same organisation, but the demo leads with Northwind.

## Core objects

| Object | What it is |
|---|---|
| Organisation | A business. Every row belongs to exactly one. |
| Customer | Who owes money. Has names and aliases used for matching. |
| Invoice | Number, customer, currency, total, outstanding, due date, status (open, partially paid, paid, void). |
| Money record | Something trusted that says money arrived: a Paystack charge, a bank statement line, a bank alert email from a verified sender. Has source, amount, currency, time, reference, payer name, and a stable external ID for idempotency. |
| Evidence | Anything a person sends that claims a payment happened: image, audio, PDF, email, pasted text. Stored in Supabase Storage with a content hash. |
| Claim | The structured reading of one piece of evidence: payer, amount, currency, date, reference, channel, invoice hints, confidence, and which fields were missing. Produced by the model, validated by zod. |
| Decision | What the policy concluded about a claim, with evidence and concerns. Never edited in place; a new decision supersedes the old one. |
| Allocation | Money record applied to an invoice. Created only by the policy or by a person approving a decision. |
| Audit event | Every automatic and human action, with who, when and why. |

## Claim states

The policy puts every claim in exactly one state. These states and their colours drive the whole interface.

| State | Colour | Meaning |
|---|---|---|
| Verified | green | Exactly one money record matches on amount, currency and time window, plus at least one of: reference, payer name or alias, invoice number. Exactly one open invoice fits. Applied automatically. |
| Needs you | amber | Money exists but the target is ambiguous: two invoices for the same amount, a partial payment, a name that half-matches. Shows the candidates and the reason. |
| Not received | red | No money record matches. Recur says plainly that the money has not arrived and the goods should not be released. It keeps watching: if matching money arrives later, the claim is re-evaluated automatically. |
| Duplicate | grey | The same payment was already claimed by other evidence. Linked to the original. |
| Not a payment | grey | Failed, pending, reversed or refunded transaction, or an invoice or request rather than a payment. |

The re-evaluation is important for the demo. A claim can move from Not received to Verified on screen the moment the real money lands.

## How a piece of evidence flows

1. **Intake.** File dropped on the board, uploaded, or found by the Gmail watcher. Hash the content; if the hash already exists in this organisation, link to the existing evidence and stop.
2. **Read.** Send it to Muse Spark Open with the extraction prompt for its type. Images and PDF pages go as images, voice notes as audio, emails as text plus attachments. The model returns JSON only. Validate with zod. Invalid output is retried once, then the evidence is marked "Couldn't read" with the reason.
3. **Claim.** Normalise amounts to minor units, currencies to ISO codes, dates to UTC with the stated time zone, names to lowercase tokens.
4. **Decide.** `packages/core/policy` runs against the organisation's money records and open invoices and returns a decision. This step is pure code and has no model call.
5. **Apply.** Verified decisions create an allocation in one database transaction that also updates the invoice. Everything else waits for a person.
6. **Watch.** New money records trigger re-evaluation of every open claim in that currency.

Steps 2 to 5 run in parallel across evidence items, bounded to a sensible concurrency, so a pile of twelve items processes visibly at once.

## The truth sources

- **Paystack.** The live, real-time source for the demo. Write it fresh, following this design:
  - **Connect.** An organisation admin pastes a Paystack secret key and picks Test or Live mode. The Edge Function checks the prefix (`sk_test_` or `sk_live_`), validates the key with `GET https://api.paystack.co/balance`, then stores it encrypted with AES-256-GCM using a server secret `PAYSTACK_CREDENTIAL_ENCRYPTION_KEY` (32 random bytes, base64). Only status, mode and timestamps ever reach the browser. Disconnect wipes the ciphertext.
  - **Webhook.** One URL per organisation: `https://<project>.supabase.co/functions/v1/paystack-webhook?organisation_id=<uuid>`, entered in that organisation's Paystack dashboard. The function reads the raw body, decrypts that organisation's key and checks `x-paystack-signature`, which is an HMAC-SHA512 of the raw body using the secret key, with a constant-time comparison. Invalid signatures get 401.
  - **Idempotency.** Each event gets a key built from the event type, the transaction reference and a hash of the body, and is claimed in a webhook-events table before processing. A replayed event does nothing.
  - **Never trust the webhook alone.** For `charge.success`, call `GET /transaction/verify/:reference` and only create the money record if Paystack confirms success with the same amount and currency.
  - **Knowing who paid.** Two routes. Checkout payment links created by Recur carry `metadata.recur_invoice_id` and `metadata.recur_customer_id`, which are checked against the database rather than trusted. In Nigeria, each customer can also get a Paystack dedicated virtual account (`POST /dedicated_account/assign`, with `preferred_bank: "test-bank"` in test mode), so a bank transfer to that account number identifies the customer.
  - **After saving** the money record, call `evaluate` for every open claim in that currency.
  - **Mode for the demo.** Live mode works, with small real payments. Test mode is safer for rehearsing because it is free and fires the same webhooks; every Paystack account has test keys in the dashboard. Whether the live demo payment can be in USD depends on the Paystack account being enabled for USD. If it is not, the live moment uses the naira organisation, or the Northwind claim is paired with a naira-denominated demo invoice.
- **Bank statement import.** CSV first, PDF if time allows. Column mapping is detected by the model once per file layout and then applied deterministically.
- **Gmail bank alerts (read-only).** Bank alert emails from senders the organisation marks as trusted become money records. Emails from anyone else are evidence, not truth. This distinction is the security story: a customer cannot create money by sending an email.

## Model contract (fill in during Stage 0)

Record here the exact request and response shapes that worked against `meta-models/muse-spark-open-1026`:

- Text-only JSON extraction: request, response, where the reasoning text appears.
- Image input: content part format, maximum size, latency for a phone screenshot.
- Audio input: content part format, accepted encodings (record from the browser as webm/opus, convert if needed), latency for a 15-second note.
- Whether tool calling or a JSON response format is supported. If not, use a strict JSON instruction plus zod validation.
- Measured cost per call type, to budget the $100 of credits.

## Screens

1. **The Board** (home). Three columns: Inbox (evidence waiting or being read), Decisions (claims in their coloured states), Invoices (open invoices with outstanding amounts). Evidence cards animate from Inbox into a state, and verified cards travel to the invoice they paid, which ticks down to zero. A drop zone covers the whole board.
2. **Evidence detail.** The original (image, audio player with transcript, PDF page or email) on the left. The claim fields on the right, each with its confidence. Below, the decision with plain-English evidence ("Amount $4,200.00 matches Paystack charge NW-3381 received 2:14 PM") and concerns. Approve, choose another invoice, or reject.
3. **Truth vs trust.** A toggle on any claim that shows what an ungated model says when simply asked "Has this customer paid?" next to Recur's decision. This exists to make the safety argument visible in one glance.
4. **Scorecard.** Results of the evaluation set (see below): accuracy of the ungated model against Recur's gate, false "paid" rate, average time per item.
5. **Ask Recur.** Hold the microphone button and ask "Who still owes me?" or "Did Acme pay invoice 1042?" The audio goes to Muse Spark Open with read-only ledger tools; the answer is spoken with the browser's speech synthesis and shown with links to the records it used.
6. **Collections.** For overdue invoices with no claim, Recur drafts a short, polite reminder per customer for the owner to edit and approve. Nothing is sent without approval.
7. **Settings.** Paystack connection, Gmail connection and trusted senders, currencies, team.

## The evaluation set

The labelled set is already in `fixtures/eval/`: 42 items (screenshots, a photographed receipt, PDFs, emails and voice notes) with the correct outcome for each in `fixtures/eval/manifest.json`, built on the seed data in `fixtures/seed/`. Read `fixtures/README.md` before using it, because a few items depend on processing order. All of it is fictional and marked as test data.

`scripts/run-eval.ts` loads the seed, runs every item in manifest order through both an ungated prompt ("Has this customer paid? Answer yes or no.") and Recur's pipeline, inserts `fixtures/seed/demo_live_payment.json`, re-evaluates, and writes `fixtures/eval/results.json` with per-item outcomes and the totals the Scorecard shows. Show the real numbers, whatever they are.

## Out of scope for the hackathon

Sending money, card details of any kind, QuickBooks, WhatsApp Business API, mobile apps, multi-language reminders beyond English unless everything else is finished.
