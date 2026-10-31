# 43 — System status run-down

**Audited against:** `console/GHC BROADCAST V16.snap`

| Area | Verdict |
|---|---|
| 1. Live stream | Structure correct. **One live defect: reverb balance.** |
| 2. Wedges | Content correct. **Feedback still unaddressed.** |
| 3. FOH | Well built, but **measurably too dark.** |
| 4. P16 | **"All vocals and instruments" is not achievable.** Hard limit. |

---

## 1. Live stream

Chain: channels → BC BAND (16) / BC VOX (13) / speech → Bus 7 → MX5 → LCL 4/5 → GoStream.

| Feed | → Bus 7 |
|---|---|
| BC BAND | 0.0 |
| BC VOX | −5.0 |
| Pastor HH, House | +3.0 each |
| KIDS LAPEL | −6.0 |
| Crowd L/R | −12.0 each |
| Inst Verb (Bus 14) | −1.0 |
| **Vox Verb (Bus 15)** | **−1.0** |

Compression now sits at a sane four stages (channel, F670, Bus 7 glue 2:1 @ −18,
ECL33 2:1 @ −15) plus the FX16 limiter, with FX10 pushed to −12 so it only
catches peaks. BC BAND's compressor is deliberately off.

### DEFECT: the reverb no longer tracks the vocals

V14 took **BC VOX from −2.0 to −5.0**. `Vox Verb → Bus 7` was left at **−1.0**.

The dry vocals dropped 3 dB and the reverb did not. The stream is now
**3 dB wetter in relative terms** than it was before the balance change —
washier, which is the opposite of "clean".

**Fix: Bus 15 Vox Verb → Bus 7 from −1.0 to −4.0.** This was flagged as a
caveat in doc 38 and then missed when the balance actually moved.

### Open

- **FX16 limiter may be inert.** It is a post-insert on a matrix whose fader is
  at −32.1 dB. If the insert runs after the fader, nothing ever reaches the
  −1 dB ceiling and the stream has no peak protection. Meter it; do not change
  the gain structure, which is what cured the clipping.
- Everything tonal — the Bus 7 EQ curve, FX10's band 1, tape drive at 5,
  whether −5.0 is the right vocal balance — still needs recordings.

---

## 2. Wedges

| Bus | Output | State |
|---|---|---|
| **1 STAGE MON** | A-1 / A-2 | 15 sources, fader −11.1 — the vocalists' wedges |
| 3 | A-3 | 11 sources, fader −2.0 |
| 4 | A-4 | 3 sources, fader **−52.3** — effectively dead but still patched |
| 2 | **not patched** | 9 sources, a real mix that reaches nothing |
| 5 | **not patched** | muted, 2 sources — abandoned |

Bus 1 content is correct to brief: 11 vocal mics averaging −5.3 dB, band
(Kick, Snare, Keys 1, Keys 2) averaging −19.7 dB. **14.4 dB separation** —
vocals clearly on top with usable tempo reference underneath.

### STILL THE BIGGEST OUTSTANDING ITEM: the wedges have never been rung out

`FX7` on Bus 1 holds seven cuts, **all of them infrasonic**:

```
20 Hz −15   25 −15   31 −15   40 −15   50 −12   63 −6   80 −3
```

**Every band from 100 Hz up is flat.** Bus 1 sits at −11.1 dB purely to stay
below feedback. A proper ring-out is worth **6–8 dB** — more than every monitor
change made in this entire engagement combined, which totals **+0.4 dB**.

Procedure: `checklists/ring-out-procedure.md`. Needs 20 minutes in an empty
room with the band's mics live. **Do not raise Bus 1 before doing it.**

Three monitor mixes (2, 4, 5) are in limbo. Worth resolving so nobody inherits
a desk with dead mixes on live outputs.

---

## 3. FOH

Well built. Per-source high-passes on all 26 channels, gates on all 19 sources
that need them, FX8 limiter at −1 dB, a properly crossed-over sub matrix with a
−3.1 dB room-mode notch at 107 Hz Q 5.2, PA zones matched within 0.4 dB.

### FINDING: measurably too dark

Composite response — Main 1 EQ + PA-C GEQ + PA-C matrix EQ:

| Hz | Main 1 | GEQ | Matrix | **Total** |
|---|---|---|---|---|
| 200 | −1.2 | 0.0 | 0.0 | **−1.2** |
| 500 | −1.3 | −3.5 | 0.0 | **−4.8** |
| 1 k | −0.2 | −3.0 | 0.0 | **−3.2** |
| 2 k | 0.0 | −4.5 | −0.1 | **−4.6** |
| 4 k | −0.1 | −1.5 | −0.7 | **−2.3** |
| 8 k | −1.1 | −1.5 | −2.4 | **−5.0** |
| **10 k** | −1.9 | −2.8 | −2.7 | **−7.3** |
| **16 k** | −2.9 | −2.0 | −2.8 | **−7.7** |

- 200 Hz – 1 kHz average: **−3.2 dB**
- 1 k – 4 k average: **−2.4 dB**
- 8 k – 16 k average: **−6.4 dB**
- **Downward tilt, 200 Hz → 10 kHz: −6.1 dB**

Nobody chose −7 dB at 10 kHz. **Three separate stages each took 2–3 dB** and
nobody summed them: Main 1's −3 dB shelf at 9 kHz, the PA GEQ's −2.8 at 10 kHz,
and the matrix HF shelf at −2.8 from 5.2 kHz.

Speech intelligibility (2–4 kHz) survives at −2 to −4.6 dB. What is gone is air
and detail. That is past "comfortable" and into dull — cymbals, consonants and
acoustic guitar will sound veiled.

**Recommended:** recover roughly 3 dB above 8 kHz by backing off **one** stage,
not all three. The matrix HF shelf is the one to move, because it starts lowest
(5.2 kHz) and so does the most damage. **Not changed here** — this is a tonal
judgement about a room I have not heard, and that is exactly the mistake that
produced V11.

---

## 4. P16 in-ears

### "All vocals and instruments" cannot be done

Ultranet carries **16 channels per bank**. The requirement is 10 vocals +
14 instruments + talkback = **25 sources minimum**. Both banks are already
16 of 16 full. This is a protocol limit, not a configuration problem.

What exists:

| | Bank A (musicians) | Bank B (singers) |
|---|---|---|
| 1–2 | **Bus 8 DRUMS** stem | **Bus 6 BAND STEM** |
| Instruments | Bass, E Gtr, AC Gtr, Keys 1, Keys 2, LOOP — **7 individual** | none individually |
| Vocals | **only 4 of 10** — Raissa, Wireless 4, LEAD2, Vox 2 | **all 10** |
| Speech | Pastor HH | Pastor HH |
| Other | Crowd L/R, Talkbacks | Crowd L/R, Talkbacks |

### Gaps

1. **Bank A carries only 4 of the 10 singers, and the four look arbitrary.**
   A musician cannot hear the other six at all. This is the real defect.
2. **Bank B has no individual instruments** — a singer cannot turn the guitar
   down without pulling the whole band.
3. **KIDS LAPEL (ch33) is in neither bank.** It sits on local input LCL-1. It
   *can* be patched to Ultranet; it simply isn't. Nobody on ears hears kids'
   ministry.
4. **House mic (ch23) is in neither bank.** A guest speaker on it is inaudible
   to anyone wearing ears. In-ears cannot feed back, so there is no reason to
   exclude it beyond slot pressure.
5. **A-15 is claimed by both ch17 Sax and ch18 LOOP.** Bank A slot 14 is
   labelled LOOP and fed from A-15, so whatever is physically in that jack is
   what the musicians get. One of the two is mis-patched. **Unresolved — needs
   someone at the stage box.**
6. **Nothing in the P16 is processed.** Every feed is tapped direct from the
   stage box, so no EQ, compression, gating or high-pass reaches anyone's ears.
   The singer work in V12 and Pastor's leveller in V11 are inaudible in the
   in-ears. If a singer complains about their monitor sound, console EQ will not
   help them.

### The fix worth making

**Give Bank A a vocal stem instead of four arbitrary singers.** One stereo stem
delivers all ten voices and **frees two slots** — enough for the House mic and
the Kids lapel.

That needs a spare bus. **Bus 5 is the safe candidate:** muted, two sources,
patched to nothing, clearly abandoned. Bus 2 also reaches nothing, but it
contains a real nine-source mix somebody built, so it should not be taken
without asking.

**Not built.** It changes what the band hears, and that decision is the music
team's to make, not mine.

---

## Priority order

| | Item | Worth |
|---|---|---|
| **1** | **Ring out the wedges** (FX7) | **6–8 dB** — dwarfs everything else |
| **2** | Fix the stream reverb balance — Bus 15 → −4.0 | removes the wash V14 introduced |
| **3** | Fit SD cards, record Matrix 5 for two services | unblocks every tonal fix |
| **4** | Recover ~3 dB above 8 kHz in FOH, one stage only | fixes the dullness |
| **5** | Bank A vocal stem, + House mic and Kids lapel | real P16 gap |
| **6** | Resolve the A-15 Sax/LOOP duplicate at the stage box | correctness |
| **7** | Resolve the three limbo monitor mixes (buses 2, 4, 5) | tidiness |

Items 2 and 7 I can build now. Item 1 needs the room. Items 3 and 6 need
hands on site. Items 4 and 5 need a decision from you.
