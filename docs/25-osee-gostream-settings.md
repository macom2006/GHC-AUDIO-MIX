# 25 — Osee GoStream Duet 8 ISO: Correct Audio Settings

Read from the GoStream control panel, 2026-09-26. Three faults, all fixable in the
software, no hardware needed.

---

## What the panel showed

| | Mic 1 | Mic 2 |
|---|---|---|
| State | ON | ON |
| Fader | −9.75 dB | −10.07 dB |
| **Preamp** | **+10 dB** | **−1 dB** |
| **Panning** | **−100 (hard left)** | **−21.24 (also left)** |
| **Mic Type** | **Condenser (XLR)** | **Condenser (XLR)** |
| Delay | 0 ms | 0 ms |
| Clip indicator | **RED** | **RED** |

| PGM | |
|---|---|
| Fader | **−28.40 dB** |
| Limiter | **OFF** |
| Threshold | −30.00 dB |
| Clip indicator | **RED** |

| IN1 | IN2 | IN3 | IN4 |
|---|---|---|---|
| −6.50 dB | −17.00 dB | −21.00 dB | −52.50 dB |

---

## Fault 1 — it sounds mono because Mic 2 is panned left

**Mic 1 is at −100 (hard left). Mic 2 is at −21.24 — also left of centre.**

Your left channel is hard left. Your right channel is *mostly left*. Both sides
collapse toward the same place, which is exactly why it sounds mono with a lopsided
image.

### Fix

| | Set to |
|---|---|
| **Mic 1 Panning** | **−100** (hard left) — already correct |
| **Mic 2 Panning** | **+100** (hard right) |

That alone restores the stereo image.

---

## Fault 2 — the clipping: you are feeding line level into a microphone input

**Mic Type is set to `Condenser (XLR)` on both channels.** That means two things, and
both are wrong for a console feed:

1. **The input is expecting microphone level** — roughly −40 to −60 dBu. The WING is
   sending **+4 dBu**. That is a 45–65 dB overload. The input stage is clipping before
   any fader can do anything about it.
2. **48 V phantom power is switched on**, and it is being sent down the cable into
   the WING's output stage. It will not usually damage a modern console output, but
   it is not something to leave running.

Then **Mic 1 has +10 dB of preamp on top of that.** And Mic 2 has −1 dB, an 11 dB
mismatch between your left and right channels — another reason the image is skewed.

### The tell-tale

**PGM is pulled down to −28.40 dB and the clip indicator is still red.** That is the
signature of input-stage clipping: the distortion happens *before* the program fader,
so pulling the fader down only gives you quieter distortion. If turning something
down does not clean it up, the overload is upstream of it.

### Fix, in order

**Step 1 — immediate, on the WING.** Drop the **Matrix 5 output trim** to about
**−30 dB**. This gets the level into a range the mic input can survive and will stop
the worst of it within seconds.

**Step 2 — proper, on the GoStream.** Tap the **`Condenser(XLR)`** button on each mic
channel. It should offer a **Line** option alongside Dynamic and Condenser. Set both
to **Line**. That switches off phantom power and drops the input sensitivity to where
a console feed belongs.

**Step 3 — set the preamps to match.**

| | Mic 1 | Mic 2 |
|---|---|---|
| Preamp | **0 dB** | **0 dB** |
| Fader | **−10 dB** | **−10 dB** |

Identical on both. Any difference between them skews your stereo image.

**Step 4 — bring the WING trim back up.** With Line selected and the preamps at 0,
raise the Matrix 5 output trim until the GoStream meters read **−12 dB average with
peaks around −6 dB**, and the clip indicators stay dark on the loudest worship
moment. Write the value down.

**If there is no Line option**, the mic input cannot accept a console feed directly.
Fit a **−30 dB inline XLR pad** between the WING and the GoStream, or leave the WING's
Matrix 5 trim at roughly −30 dB permanently. A pad is the better answer: it keeps the
console operating at a sensible level.

---

## Fault 3 — PGM settings

| Setting | Now | Set to | Why |
|---|---|---|---|
| **Fader** | −28.40 dB | **0 dB** | Once the input clipping is fixed, this belongs at unity. It is currently being used to hide a problem it cannot fix. |
| **Limiter** | **OFF** | **ON** | You have no safety net at all on the way to the encoder |
| **Threshold** | −30.00 dB | **−3.00 dB** | At −30 it would crush everything. At −3 it catches only true peaks. |
| Attack | 0.70 ms | keep | Fast, correct for a safety limiter |
| Release | 93 ms | keep | Fine |
| Gain | 0.00 dB | keep | |

The WING already has a proper limiter on Matrix 5. The GoStream's limiter is a last
line of defence, not a mix tool — it should sit idle and only move on surprises.

---

## Also worth fixing while you are in there

### IN1–IN4 are open

Those are the HDMI inputs' embedded audio, and **none of them is muted**. IN1 sits at
**−6.50 dB**, which is close to unity. If any camera, laptop or playback device on
HDMI is carrying audio, it is going into your program mix — and camera onboard
microphones produce exactly the hollow, echoing sound that is very hard to diagnose
later.

Unless you are deliberately using a source's embedded audio:

- Pull **IN1, IN2, IN3, IN4 faders to minimum**
- Set **AFV to OFF** on all four

**AFV is "Audio Follow Video."** If it is on, cutting from camera 1 to camera 2
changes or drops the audio mid-sentence. Verify it is off by talking on a mic and
cutting cameras.

### Lip-sync

Each mic channel has a **Delay** control, 0–500 ms, currently at 0. That is a
perfectly good place to set your lip-sync offset — arguably better than the WING,
since it is in the same box as the video.

Use **one or the other**, never both. If you use the GoStream's delay, set the same
value on Mic 1 and Mic 2 and leave Matrix 5's delay off on the console.

---

## Target settings summary

| Channel | Mic Type | Preamp | Fader | Pan | Delay |
|---|---|---|---|---|---|
| **Mic 1** (WING LCL out 4) | **Line** | 0 dB | −10 dB | **−100** | lip-sync or 0 |
| **Mic 2** (WING LCL out 5) | **Line** | 0 dB | −10 dB | **+100** | same as Mic 1 |
| IN1–IN4 | — | — | **minimum** | 0 | — |

| PGM | |
|---|---|
| Fader | 0 dB |
| Limiter | **ON** |
| Threshold | −3.00 dB |

| On the WING | |
|---|---|
| Matrix 5 output trim | **−30.5 dB** — set and verified clean, 2026-09-26. Scene-safe this. |

---

## Checking it worked

1. Play loud worship material through the system.
2. **No red clip indicators** on Mic 1, Mic 2 or PGM.
3. Mic 1 and Mic 2 meters move **together and at the same level**.
4. Listen on headphones — pan a source hard left on the console and confirm it moves
   to the left in the stream. Then hard right. If both stay centred, the panning is
   still wrong.
5. Check the stream itself on a phone, not just the GoStream's monitoring.
