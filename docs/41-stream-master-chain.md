# 41 — Cleaning the master chain and setting the balance

**File:** `console/GHC BROADCAST V14.snap` (built on V13)

Two values changed in the whole file. Nothing else moved.

## The finding: six compressors in series

| | Stage | Setting |
|---|---|---|
| 1 | Channel compressor | per channel |
| 2 | BC VOX — F670 | on |
| 3 | Bus 7 — COMP | 2:1 from −18 — **the glue, correct** |
| 4 | Bus 7 — FX10 C5-CMB | **2.5:1 from −32.7** |
| 5 | Matrix 5 — ECL33 | 2:1 from −15 |
| 6 | Matrix 5 — FX16 LIMITER | ceiling −1 |

A studio master runs two or three gentle stages. Six is cumulative, and it is
why the stream sounds squashed rather than clean.

**Stage 4 was the offender.** A threshold of −32.7 with 2.5:1 means it works on
the entire programme, continuously, on a bus that has already been through the
channel compressor, the F670 and the Bus 7 glue. It is the same wrong threshold
found on Pastor's FX6 in V11.

**FX10 threshold −32.7 → −12.0.** It now catches peaks only. Stage 4 is
effectively out of the chain.

Its band 1 setting (−2.8 dB static, width 10) is left exactly as it is. That is
tonal, and tonal changes wait for measurement.

## Balance

| | → Bus 7 |
|---|---|
| BC BAND | 0.0 dB (unity) |
| BC VOX | −2.0 → **−5.0 dB** |

Vocals now sit 5 dB under the band at the stem level. This is the number from
doc 38. **If you found a different one riding it live, use yours** — this is a
starting point, not a measurement.

## Why there is no band glue compressor

Adding a compressor to BC BAND was the obvious "make it sound produced" move,
and it is the wrong one here. The chain is already over-compressed; another
stage makes the exact problem worse. Bus 7's 2:1 from −18 is the correct place
for that job and it is already doing it.

BC BAND's compressor stays **off**.

## Deliberately untouched

- Every channel — FOH, wedges and in-ears are byte-identical
- All EQ everywhere. No tonal guesses.
- **Matrix 5 at −32.1 dB.** Hard-won, cured the clipping, not touched. No
  GoStream re-trim needed.
- ECL33, TAPE (22% parallel, drive 5) and the FX16 limiter — this is the part
  that genuinely gives the "mastered" character and it is set sensibly

## Open item worth metering

FX16 is a **post**-insert on Matrix 5, and the matrix fader sits at −32.1 dB.
If the insert runs after the fader, the signal never approaches the limiter's
−1 dB ceiling and **the limiter is doing nothing at all**.

That is not necessarily a problem — nothing is clipping since the level was
reduced — but it means the stream currently has no peak protection.

Check it on the desk: watch FX16's gain-reduction meter during a loud chorus.
If it never moves, the limiter is inert. The fix is to attenuate after the
limiter rather than before it, not to raise the level back up.

Do not change this before metering it. The current gain structure is what
finally cured the clipping.

## What still needs recordings

Everything tonal:

- Whether the Bus 7 EQ curve is right for the room
- Whether FX10's band 1 cut is helping or hurting
- Whether the TAPE drive at 5 is too much or too little
- Whether BC VOX at −5.0 is the right balance

Fit the SD cards, record Matrix 5 for two services, and these stop being
opinions.
