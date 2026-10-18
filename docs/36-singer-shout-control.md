# 36 — Dehil, Elsie and Peggy: quieter but more audible

**File:** `console/GHC BROADCAST V10.snap` (built on V9)

| Singer | Channel | Source |
|---|---|---|
| Dehil | 14 — Vox 2 | A-30 |
| Peggy | 16 — Vox 4 | A-29 |
| Elsie | 24 — Wireless 3 | A-18 |

## What was wrong

Same two faults the House mic had before V7.

1. **Compressor attack 30 ms.** A shouted syllable is over in about 20 ms, so the
   compressor was letting the whole front of every loud word through at full
   level and only clamping down afterwards. That is exactly what "screaming"
   sounds like in a mix.
2. **Octave-wide EQ cuts** (Q 1.54–2.50). Four broad cuts totalling 14–16 dB were
   removing most of the voice to try to tame a narrow problem. Quiet, but gone.

On top of that the faders were uneven: Dehil +5.5, Elsie +4.3, Peggy −0.3.

## What V10 changes

Per channel, nothing else on the console touched:

- **Attack 30 → 8 ms**, release 150 → 120 ms. The shout gets caught; the voice
  recovers between phrases.
- **Threshold down 5 dB, ratio 4:1 → 5:1.** The compressor now works on every
  word instead of only the peaks. Auto makeup is on, so the average level comes
  back up on its own — that is the "more audible" half.
- **Same cuts, a quarter the width.** Q 2.50 → 5, and 1.68/1.57 → 7, at the same
  frequency and the same depth. Roughly two octaves of voice come back for free.
  The 5.9 kHz band goes Q 1.54 → 3.
- **+1.5 dB shelf at 12 kHz.** Audibility comes from consonants, not from
  presence. A 4 kHz lift would have made the shouting worse.
- **Fader −4 dB on all three.** Takes back the auto makeup so the net result is
  quieter at the desk. Their balance against each other is unchanged.

Net: peaks down roughly 6–8 dB, average level about the same or slightly up,
intelligibility up.

## After loading

Listen on one chorus. If anyone is still too loud, pull that fader — do not
touch the compressor. If anyone is now too dull, lift the 12 kHz shelf to
+2.5 dB rather than undoing the EQ cuts.
