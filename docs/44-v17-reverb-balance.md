# 44 — V17: the stream reverb tracks the vocals again

**File:** `console/GHC BROADCAST V17.snap` (built on V16)

**One value changed.**

## What was wrong

V14 moved **BC VOX → Bus 7 from −2.0 to −5.0** to bring the stream vocals down.
`Vox Verb → Bus 7` was left at **−1.0**.

| | dry (BC VOX) | wet (Vox Verb) | wet vs dry |
|---|---|---|---|
| before V14 | −2.0 | −1.0 | +1.0 dB |
| V14 – V16 | −5.0 | −1.0 | **+4.0 dB** |
| **V17** | −5.0 | **−4.0** | **+1.0 dB** |

The dry vocals dropped 3 dB and the reverb did not, so the stream was 3 dB
wetter than intended — washier, the opposite of the "clean" V14 was for.

I wrote this caveat myself in doc 38 and then missed it when the balance
actually moved.

## Why this is a send change, not a fader change

`tools/coupling_check.py` flags Bus 15 as reaching **three** destinations:

| Vox Verb feeds | |
|---|---|
| Main 1 | the house reverb |
| Bus 1 at −19.1 dB | **the wedges** |
| Bus 7 | the stream |

Its **fader is shared between all three.** Pulling the fader would have taken
reverb out of the house and the wedges too.

Verified: Bus 15's fader, its send to Bus 1, its send to Main 1, its EQ and the
reverb itself (FX1) are all untouched. Only the send to Bus 7 moved.

## Inst Verb deliberately unchanged

BC BAND sits at unity and Inst Verb at −1.0 — a 1 dB gap, correct as-is. V14
never moved the band level, so the instrument reverb never drifted.

## Verified

All 40 channels byte-identical. Mains and all matrices identical. Output patch
and every FX slot identical. Every bus but 15 identical. Structural check
identical, including value types.

Coupling check on V17: the wet/dry item is cleared, 9 issues down to 8. The
remaining 8 are all pre-existing and listed in doc 43.

## Still outstanding — none of it is in any snapshot

| | Needs |
|---|---|
| **Ring out the wedges** — worth 6–8 dB | 20 minutes in an empty room |
| Record Matrix 5 for two services | SD cards in WING-LIVE |
| **Patch Bus 9 to Ultranet** — the P16 vocal stem already exists | one output patch |
| Recover ~3 dB above 8 kHz in FOH | a decision, then a listen |
| ch3 is a snare bottom mic, not a hi-hat | rename, check polarity |
| A-15 serves two live channels | someone at the stage box |
| Buses 2, 5, 12 are dead ends | a decision on what they were for |
