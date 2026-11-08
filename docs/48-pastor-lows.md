# 48 — Pastor's mic lacks lows

**File:** `console/GHC BROADCAST V21.snap` (built on V20)
**Channel:** 21 Pastor HH

## Measured

Composite of his high-pass and channel EQ. A male speaking fundamental sits
**85–155 Hz**.

| Hz | V1 (149 Hz HPF) | Now (165 Hz) | V21 | V21 gain |
|---|---|---|---|---|
| 80 | −22.8 | −26.3 | −11.5 | **+14.8** |
| 100 | −15.4 | −18.8 | −5.2 | **+13.6** |
| **110** | −12.3 | **−15.6** | −3.3 | **+12.4** |
| 125 | −8.7 | −11.7 | −1.7 | **+10.0** |
| 150 | −5.0 | −7.0 | −1.0 | **+6.0** |
| 250 | −6.8 | −6.9 | −3.3 | **+3.5** |

**At 110 Hz — the middle of his voice — he is 15.6 dB down.** That is the
answer to "it lacks lows". Three things stack:

1. High-pass at **165 Hz, 24 dB/oct**
2. EQ band 1 at **−5.5 dB, 257 Hz** — straight through the chest
3. Low shelf **−1.0 dB at 445 Hz**

## My share of it, stated plainly

**In V2 I raised his high-pass from 148.9 Hz to 165 Hz.** That cost **3.3 dB at
110 Hz** and 3.0 dB at 125 Hz.

So I made it worse — but I did not cause most of it. At V1, before I touched
anything, he was already 12.3 dB down at 110 Hz. The bulk was in the file as
built.

## But why did it *change* recently?

The EQ has not moved since V4. What changed is **V11's leveller**: threshold
−41, 2:1, 400 ms release, auto makeup on.

A leveller lifts the quiet passages — which are the ones where he is **off-mic**.
Off-axis and at distance a handheld loses its proximity bass. So the leveller
raises the thin, distant version of his voice into the average, and the overall
sound reads thinner **without any EQ having moved**.

That is the mechanism. The fix is to give the low end back, not to undo the
levelling he asked for.

## What V21 changes

Three values.

| | V20 | V21 |
|---|---|---|
| High-pass | 164.7 Hz | **110 Hz** (24 dB/oct unchanged) |
| EQ band 1 | −5.5 dB @ 257 Hz | **−3.0 dB**, same frequency and Q |
| Low shelf | −1.0 dB @ 445 Hz | **0.0 dB** |

**Nothing else.** His leveller, expander, fader and all his routing — wedge,
stream and FOH — are untouched, as is every FX slot.

## By hand, if you would rather not reload

The desk has drifted from these files, so changing it at the console may be
simpler:

```
ch21  →  high-pass          165 Hz  ->  110 Hz
ch21  →  EQ band 1 gain    -5.5 dB  ->  -3.0 dB   (leave 257 Hz, Q 1.93)
ch21  →  low shelf gain    -1.0 dB  ->   0.0 dB
```

## Watch for

**He is in the wedges at −6.0 dB, post-fader**, so his low end now reaches the
stage monitors too. At 110 Hz with a 24 dB/oct slope, rumble below 80 Hz is
still 11.5 dB down, so this should be safe — but if the wedges get muddy or
handling noise becomes audible, take the high-pass to 125 Hz rather than back to
165.

## Left alone deliberately

**FX6's band 1 carries a −2.8 dB static cut.** If band 1 is the low band, that
is another 2.8 dB off his bottom end. I have not touched it: the C5-CMB's
crossover points are not something I can read reliably from the file, and
guessing at a multiband's band layout is the kind of assumption that produced
V11. If V21 is still short of low end, that is the next place to look — on the
desk, where the band edges are visible.
