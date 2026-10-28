# Recur test fixtures

Everything in this folder is invented test data: the companies, people, banks and payment apps are fictional, email domains use the reserved `.example` domain, and every image and PDF carries a "SAMPLE · Recur test data" line. None of it is a real transaction.

## Folders

| Folder | What it holds |
|---|---|
| `spike/` | One screenshot and one voice note for the Stage 0 model test, plus `expected.json` with the fields the model should extract. |
| `seed/` | The two demo organisations, their customers, open invoices and trusted money records, a bank statement CSV for Northwind, and `demo_live_payment.json` describing the payment that arrives live during the video. |
| `eval/` | 42 evidence items and `manifest.json`, which states the correct outcome for every item. |
| `truth/` | Bank alert emails. The four from `brightlinebank.example` and `lagoonbank.example` are trusted senders and become money records. `spoofed_alert_vantage.eml` comes from a look-alike domain and must be treated as ordinary evidence, never as money. |

## The evaluation set

| Expected state | Count | What it tests |
|---|---|---|
| Verified | 15 | Screenshots from four app styles, a photographed paper receipt, a wire PDF, a customer email and voice notes, in USD and NGN. Includes payers known only by an alias or initials. |
| Needs you | 5 | Two invoices with the same amount, a partial payment, a remittance covering two invoices, a deposit with no invoice, and a naira part payment. |
| Not received | 11 | Convincing claims with no matching money, including the demo's two red cards, a dollar claim against a naira invoice, an amount mismatch and two prompt-injection attempts. |
| Duplicate | 4 | A byte-identical resend, a forwarded email of a payment already claimed, a second photo of the same receipt and a low-quality copy of an earlier payment. |
| Not a payment | 7 | Failed, scheduled and reversed transfers, an invoice, a payment request, a promotional email and an unrelated photo. |

Each manifest item lists the file, its type, organisation, the claim a correct reader should extract, the expected state, the expected invoice or candidates, the money record it should match, and notes on anything subtle.

## Order matters for a few items

The evaluation runner should load `seed/` first, then process items in manifest order, because the duplicates refer to earlier items (e28 after e02, e29 after e09, e30 after e06, e41 after e03). Items e22 and e23 start as Not received. After the run, insert the record in `seed/demo_live_payment.json` and re-evaluate: e22 must become Verified and e23 a Duplicate of it, while e21 stays Not received.

## Voice notes

The five voice notes were made with an offline speech synthesiser, so they sound robotic. They are fine for testing. For the demo video, re-record the ones you show (e23 and one other) in a real voice, keeping the same words.

## Regenerating

The generator lives in `tools/fixture-generator/`. Edit `data.py` to change the world, then run `python3 build.py`. It needs Pillow, ReportLab, ffmpeg and the `espeakng-loader` pip package.
