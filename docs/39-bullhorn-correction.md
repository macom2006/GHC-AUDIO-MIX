# 39 — The bullhorn: what V10 broke and how V12 undoes it

**File:** `console/GHC BROADCAST V12.snap` (built on V11)

## What went wrong

In V7 I narrowed the House mic's EQ cuts from an octave wide to Q 5–7. That was
correct: those were **feedback notches**, found by ringing out, and a notch
should be narrow.

In V10 I applied the same move to Dehil, Peggy and Elsie. That was wrong. Their
cuts were **tonal shaping** — a broad, gentle scoop across 400 Hz to 6 kHz that
was holding the voices natural. Narrowing them left three deep holes and let
everything between them come back up.

Measured change from the V9 curve, V10/V11 against V9:

| | 500 Hz | 630 Hz | 800 Hz | 1 kHz | 1.6 kHz | 2.5 kHz |
|---|---|---|---|---|---|---|
| Dehil | +2.1 | +3.8 | +1.9 | +3.4 | +2.4 | +2.2 |
| Peggy | +2.1 | +3.8 | +1.9 | +3.4 | +2.4 | +2.6 |
| Elsie | +2.8 | +3.8 | +4.1 | +2.7 | +1.9 | +2.0 |

Average across 700 Hz – 4 kHz: **−3.1 dB → −1.0 dB** on all three. That band is
exactly what makes a voice sound like a megaphone. The 5:1 ratio added to it.

## What V12 does

| | V11 | V12 |
|---|---|---|
| Singer EQ | narrow notches Q 5/7/7/3 | **V9 broad curve, restored exactly** |
| Ratio | 5:1 | 3:1 |
| Threshold | −42 / −42 / −41 | −40 / −40 / −38.5 |
| Attack | 8 ms | **8 ms — kept** |
| Release | 120 ms | 150 ms (V9) |
| 12 kHz air | +1.5 dB | **+1.5 dB — kept** |
| Faders | V9 −4 dB | V9 −2 dB |
| Pastor comp threshold | −44 | −41 |

The shout control that worked — the **8 ms attack** — stays. The ratio comes
down because 5:1 was adding midrange density of its own. The air shelf stays:
air is the opposite of a bullhorn.

Pastor's threshold moves −44 → −41 so his leveler does 4–6 dB instead of 8–10.
The two-stage structure from V11 is unchanged; it was just working too hard.

Verified: the 700 Hz – 4 kHz average is back to −3.1 / −3.4 / −2.9 dB, identical
to V9.

## The rule this cost us

**A narrow Q is for a frequency you found. A broad Q is for a tone you want.**

Never narrow a cut you did not place by ringing out. On these three channels the
broad cuts were doing real work and the width *was* the setting.

## If it is still thick

The remaining candidates, in order, and all reversible:

1. Bus 13 BC VOX → Bus 7 (doc 38) — stream only.
2. Bus 7 EQ, not the channels. One broad −2 dB at 800 Hz, Q 1.0, fixes all
   twelve voices at once without touching anyone's channel.
3. Only then go back to individual channels.
