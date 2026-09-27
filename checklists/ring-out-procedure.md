# RINGING OUT THE STAGE MONITORS — GHC

**Print this. 60–90 minutes. Mid-week, empty room, nobody waiting.**

Date: ____________  Done by: ____________

---

## WHAT YOU ARE DOING

Finding the exact frequencies where each microphone and wedge want to howl, and
cutting **only** those frequencies, narrowly. Every notch you place buys back
headroom — the mic can go louder before it rings.

You are **not** making it sound better. You are raising the ceiling. Tone comes after.

---

## YOUR SYSTEM — the numbers you need

| Thing | Where |
|---|---|
| **Main wedge mix** | **Bus 1 "STAGE MON"** → stage box outputs 1 and 2 |
| **Its graphic EQ** | **FX7**, 31-band, post-insert on Bus 1 |
| Second wedge | Bus 3 → stage box output 3 |
| Bus 3's EQ | **No GEQ available.** Use its 6-band parametric at Q 8–10. |
| Mains graphic EQs | FX12 (PA L), FX13 (PA C), FX14 (PA R) |
| Speech channels | 21 Pastor, 23 House, 33 Kids Lapel |
| Vocal channels | 13, 14, 15, 16, 20, 22, 24, 25, 26, 27 |

The infrasonic bands on FX7 (20–80 Hz) are already pulled down. **Leave them.**

---

## BEFORE YOU START

- [ ] **Save the show file.** `Setup → Show → Save As` → `PRE-RINGOUT-<date>`
- [ ] Nobody on the platform. All channels muted.
- [ ] **Hearing protection in your pocket.** You will make it howl on purpose.
- [ ] Someone else in the building who knows where the master fader is
- [ ] Bring a notepad, or use the log at the back of this sheet

### Set up the RTA — this is what makes it possible

1. Open the **RTA**
2. Detector: **PEAK**
3. Decay: **SLOW** — this holds the spike on screen long enough to read it
4. Source: **follow solo**, so it shows whatever channel you have soloed
5. Open the **FX7 GEQ** page — the WING can overlay the RTA on the graphic EQ.
   **Turn that overlay on.** The spike appears directly above the slider you need.

### Protect the system

- [ ] **Pull the main PA down** — Matrix 1, 2, 3 to −∞. You are working on wedges only.
- [ ] Set the **Bus 1 fader to −11** where it is now. You will raise it as you go.

---

## THE LOOP — repeat for each microphone

Work one microphone at a time. Never two.

### Step 1 — Isolate

- [ ] Every channel muted except the **one** mic you are testing
- [ ] That mic **physically in the position it is really used** — on its stand, at the
      pulpit, wherever the singer stands. Not on the desk.
- [ ] Its send to Bus 1 at its normal level

### Step 2 — Make it ring

- [ ] Raise the **Bus 1 master fader** slowly — a decibel or two at a time
- [ ] Listen for the tone that starts to "bloom" and hang
- [ ] **Stop the moment it starts.** Do not let it get loud. A gentle ring tells you
      everything a scream does, and does not damage drivers or ears.

### Step 3 — Find the frequency

**On the RTA:** one band will spike well above the rest and stay there. That is it.

**By ear, if the RTA is ambiguous:**

| It sounds like | Look around |
|---|---|
| Rumble, chest thump | 100–250 Hz |
| Boxy, hollow "woof" | 250–500 Hz |
| Honky, nasal, "aww" | 500 Hz – 1 kHz |
| Ringing, "eee" | **1–4 kHz — most common** |
| Whistle, "sss" | 4–8 kHz |
| Piercing, needle-like | 8 kHz+ |

### Step 4 — Cut it

- [ ] On **FX7**, pull that band down **3 dB**
- [ ] Ring gone? Good. Still ringing? Another **3 dB**.
- [ ] **Never more than 6 dB on one band.** If 6 dB will not hold it, the problem is
      placement, not EQ — see the back of this sheet.

### Step 5 — Go again

- [ ] Raise the Bus 1 fader again until the **next** frequency rings
- [ ] Repeat steps 3 and 4
- [ ] **STOP AFTER 4 NOTCHES ON THIS MIC.** More than four and you are destroying
      the microphone to solve a placement problem.

### Step 6 — Back off and log it

- [ ] Note the fader position where it rang
- [ ] **Pull back 6 dB from that point.** That is your working headroom.
- [ ] Write the frequencies in the log below
- [ ] Mute this mic. Move to the next one.

---

## ORDER TO WORK IN

Do the ones that matter most, while you are freshest:

1. **ch 21 Pastor Lapel** — the most important mic in the building
2. **ch 23 House** — currently your worst offender
3. **ch 20 LEAD2 (David)** — lead vocal
4. ch 22 Raissa
5. ch 24 Wireless 3, ch 27 Wireless 4
6. ch 13–16 — the Vox group
7. ch 25 Jude, ch 26 Brenda
8. ch 33 Kids Lapel

**If you run out of time, the first three are worth more than the rest combined.**

---

## THE ALL-TOGETHER TEST

Once every mic is done individually:

- [ ] Unmute **all** of them at their normal levels
- [ ] Raise Bus 1 slowly
- [ ] It will ring earlier than any single mic did — that is the open-mic arithmetic,
      not a mistake
- [ ] Place **up to 3 more notches** on FX7 for whatever rings with everything open
- [ ] Back off 6 dB. **That is your working wedge level.** Write it down.

---

## THEN THE MAINS

Same method, different EQ:

- Work from the **Matrix 1 / 2 / 3 fader**, not Bus 1
- Notch on the **channel's own EQ at Q 8–10** for a single-mic problem
- Notch on **FX12 / FX13 / FX14** for something that rings on every mic
- Do the centre cluster (Matrix 2) first — it carries most of the speech

---

## WHEN TO STOP AND FIX SOMETHING ELSE

Put the mouse down and go and look if:

| Sign | What it means |
|---|---|
| A mic needs more than 4 notches | Placement is wrong |
| Cutting 6 dB does not hold it | It is too near a speaker |
| The same frequency rings on every mic | It is the **room**, not the mics. Notch it once on the GEQ and stop. |
| It rings again the moment anyone moves | The mic is in the wedge's coverage |
| The voice now sounds hollow | You have cut too broadly. Narrow the Q; keep the depth. |

**Placement beats EQ every time.** Halving mic-to-mouth distance gives 6 dB — more
than four notches combined and it costs nothing.

---

## FINISH

- [ ] **Save as** `RUNG-OUT-<date>`, export to USB **and** the server
- [ ] Set the Bus 1 fader to its new working level: **________ dB**
- [ ] **Scene-safe Bus 1 and Matrix 1/2/3** so a recall cannot undo this
- [ ] Run a song through it and check the wedges still sound musical

---

## NOTCH LOG

### FX7 — Bus 1 STAGE MON (the wedge GEQ)

| # | Frequency | Cut | Which mic caused it |
|---|---|---|---|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |

### Channel EQ notches (single-mic problems, Q 8–10)

| Channel | Frequency | Cut | Frequency | Cut |
|---|---|---|---|---|
| 21 Pastor | | | | |
| 23 House | | | | |
| 20 David | | | | |
| 22 Raissa | | | | |
| 24 Wireless 3 | | | | |
| 27 Wireless 4 | | | | |

### Working levels found

| | Before | After |
|---|---|---|
| Bus 1 STAGE MON | −11.1 dB | |
| Matrix 1 PA L | −0.5 dB | |
| Matrix 2 PA C | −0.3 dB | |
| Matrix 3 PA R | −0.7 dB | |

**Headroom gained: ________ dB**
