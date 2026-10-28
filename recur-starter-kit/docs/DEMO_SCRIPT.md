# Recur — the three-minute demo

The judges score the demo at 25%, but the video also carries the other 75%, because it is how they learn the impact, see the use of Meta's model and judge the engineering. Every second has one job.

## The rules this video follows

1. **A person in the first five seconds.** Judges remember a story about someone, not a feature list.
2. **Show, then explain.** The product does the thing first. The voiceover explains afterwards, in one sentence.
3. **One unforgettable moment.** For Recur it is the fake screenshot that stays red while the real payment turns green, live.
4. **Real, not mocked.** Every product shot is the deployed app doing real work. Motion graphics are only for the story and the architecture, never to fake a result. Put a small "Live, not edited" timer on the live payment shot.
5. **Captions on everything.** Many judges watch without sound.
6. **Plain voice.** Short sentences, spoken by you, calm and confident. No buzzwords.

## Shot list

### 0:00 – 0:18 · The hook (motion graphics)

A phone screen in the middle of a dark frame. WhatsApp-style messages pop in faster and faster: a payment screenshot, a voice note waveform, "sent it 🙏", a PDF, a bank alert, another screenshot. A counter in the corner: "Open invoices: 30".

> **Voiceover:** "This is Sarah's phone. She runs a small design studio. Every week her clients pay her by transfer, and every week the proof arrives like this."

The messages freeze. One screenshot enlarges: "$4,200.00 · Sent ✓".

> **Voiceover:** "Last month she shipped a job against this screenshot. The money never came."

Cut to black. The word **Recur** appears.

### 0:18 – 0:30 · The promise (product, wide shot)

The Board, empty and calm.

> **Voiceover:** "Recur reads every kind of payment proof, checks it against the money that actually arrived, and only closes an invoice when it can prove you were paid."

### 0:30 – 1:05 · Everything at once (product)

You drag twelve mixed files onto the board in one move: screenshots, two voice notes, a PDF remittance, three bank alert emails.

All twelve cards enter the Inbox. Each shows a one-line "thinking" status from Muse Spark Open: "Reading a Zelle screenshot…", "Listening to a voice note from Marcus…". Cards land in their states one after another. Green cards fly to their invoices, and the outstanding totals count down.

Zoom in on one voice note card. The transcript and the extracted fields appear.

> **Voiceover:** "Screenshots, voice notes, PDFs and emails all go to one model, Meta's Muse Spark Open, which turns each one into a structured claim. Then Recur checks every claim against Paystack and the bank before it touches an invoice."

### 1:05 – 1:25 · It asks instead of guessing (product)

An amber card (fixture e16). Open it: "Bluebird Coffee paid $1,850.00, but has two open invoices for exactly $1,850.00." Two candidates side by side with their evidence. You pick one. It closes.

> **Voiceover:** "When it isn't sure, it doesn't guess. It shows you why and lets you decide."

### 1:25 – 2:10 · The moment (product, split screen with your phone)

Two red cards side by side, both "Not received". One is from Marcus at Bluebird (fixture e22). The other is a perfect-looking screenshot from Vantage Supply (fixture e21).

> **Voiceover:** "These two both say they've paid. Neither payment has arrived."

Picture-in-picture: your hand pays the Paystack payment link for Marcus's invoice on your phone. A "Live, not edited" timer runs.

Seconds later, Marcus's card turns green on its own and flies to his invoice. A soft chime. The other card stays red.

Open it. The screenshot on the left. On the right: "No payment matching this amount, time or reference has arrived from Paystack or your bank. Don't release the goods yet."

Flip the "Truth vs trust" toggle. Beside Recur's answer, a plain model asked "Has this customer paid?" says "Yes. The screenshot shows a completed payment of $3,600.00."

> **Voiceover:** "Recur doesn't accuse anyone. It just waits for the money. Marcus's payment was real, so it closed the moment it landed. This one is a test screenshot for a payment that never happened, and an AI that trusts the picture would have told Sarah to ship."

### 2:10 – 2:30 · Proof, not promises (product)

The Scorecard page. Two numbers large on screen: how often the ungated model said "paid" when no money arrived, and how often Recur did. Then accuracy across the full evaluation set.

> **Voiceover:** "We tested it on forty-plus labelled cases: genuine payments, fakes, duplicates, partial payments and reversals. The model reads, but a policy we can test decides. It never lets a model move money."

Use the real numbers, whatever they are.

### 2:30 – 2:45 · Talk to it (product)

You hold the microphone button.

> **You:** "Who still owes me money this month?"

Recur answers out loud and highlights three customers and their totals.

### 2:45 – 3:00 · Close (motion graphics, then you)

Three quick cards on a dark background: "Built in Lagos." "Works in dollars and naira." "Every instant-payment rail has this problem."

If you have one, a three-second clip of a real business owner who tried it, saying one sentence.

> **Voiceover:** "I'm Gloria. I built Recur during this hackathon on Muse Spark Open. Small businesses shouldn't have to choose between trusting their customers and getting paid."

End card: **Recur** · github link · "Everything shown was built during the Meta Global AI Developer Hackathon."

## Making the motion graphics

Build them in code with Remotion, which lets you write animations as React components and render them to video, so Claude Code can build and adjust them with you. Check its licence before you start; it is free for individuals and very small companies. Keep the motion graphics to the hook, the architecture beat if you add one, and the close. The middle of the video must be the real product.

Prompt for Claude Code:

> In a new folder `video/`, set up a Remotion project at 1920×1080, 30 fps. Build the 18-second hook described in docs/DEMO_SCRIPT.md: a phone in the centre of a dark frame, chat bubbles arriving faster and faster (screenshot thumbnails, a voice-note waveform, short texts, a PDF icon, a bank alert), an "Open invoices: 30" counter, then a freeze with one screenshot enlarging, a cut to black and the word Recur. Use Recur's accent colour and the same font as the app. Then build the 15-second closing sequence. Expose the text as props so I can change wording without touching the animation.

## Sound

- Quiet instrumental music under the whole video, lowered whenever you speak.
- A soft chime when an invoice closes. It is the sound judges will remember.
- Record the voiceover in a quiet room with your phone close to your mouth, then clean it up with a free noise-removal tool.

## Before you record

- One script resets the database to the exact demo state.
- Browser at 1920×1080, bookmarks bar hidden, notifications off, zoom at 100%.
- Rehearse the live Paystack payment ten times. If it ever takes longer than five seconds, find out why before recording.
