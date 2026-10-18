# 37 — Pastor's mic: steady when soft, still alive when he lifts

**File:** `console/GHC BROADCAST V11.snap` (built on V10)
**Channel:** 21 — Pastor Lapel

## What was wrong

Three devices were all set to work in the same part of the range, so soft
speech fell through and loud speech got flattened.

| Device | Was | Problem |
|---|---|---|
| Expander (gate) | threshold −48 | Pulling down the same quiet words the compressor should be lifting |
| Channel compressor | −37, 4:1, 30 ms att, 150 ms rel | Only engaged on the loud half, then grabbed hard and let go between words |
| FX6 Combinator (post-insert) | −32.7, 2.5:1 | Compressing normal speech, which is what flattened the exciting moments |

## What V11 does

Splits the job into two stages that work in different places.

**Stage 1 — the leveler (channel compressor).**
Threshold −44, ratio **2:1**, attack 20 ms, release 400 ms, softest knee,
auto makeup. Low and gentle, so it rides the *average*. When he drops to a
near-whisper it lifts him to the same place as normal speech; it holds through
a whole sentence instead of pumping between words. At 2:1 with a soft knee you
cannot hear it working.

**Stage 2 — the ceiling (FX6 Combinator).**
Threshold **−32.7 → −20**, ratio 2.5:1 unchanged. It now sits above normal
speech and does nothing until he lifts his voice. When he does, it catches it
at 2.5:1 — so the moment still comes through clearly louder than the rest, it
just cannot run away.

**The expander gets out of the way.** Threshold −48 → −54, so it only works on
room noise between sentences, never on a quiet word.

**Fader −4 dB** (+5.8 → +1.8) to take back the leveler's auto makeup.

Net: soft speech lands roughly 8–10 dB higher than before. Loud preaching keeps
about 10–12 dB above that — enough to feel, not enough to hurt the stream.

FX5 (the dynamic EQ holding down harshness and sibilance) and his channel EQ
are untouched. They were already right.

## First soundcheck

Watch the gain-reduction meter on channel 21 while he talks normally.

- **Normal speech should show 3–6 dB of reduction.** Less than 3 → threshold
  down to −47. More than 8 → threshold up to −41.
- **The Combinator should show nothing on normal speech** and 3–5 dB when he
  lifts. If it works all the time, raise its threshold to −17.
- Then set the fader by ear. +1.8 is a starting point, not a measurement.
