# 42 — The vocalists' wedge mix

**File:** `console/GHC BROADCAST V15.snap` (built on V14)
**Bus:** 1 STAGE MON → A-1 / A-2

Brief: *vocals, a little keys, and drums for tempo, to the vocalists.*

## What the wedge now contains

| Send | Channel |
|---|---|
| −4.9 to −5.7 | Vox 1–4, LEAD2, Raissa, Wireless 3, Jude, Brenda, Wireless 4 — **all 10 singers** |
| −22.4 | Keys 1, Keys 2 — already "a little", unchanged |
| −18.0 | Kick |
| −16.0 | Snare |

## Removed

| Channel | Why |
|---|---|
| Bass, E Gtr, AC Gtr, Sax, LOOP | Not in the brief |
| **Pastor Lapel** (was −6.0) | A lapel mic in a wedge is the worst feedback source there is |
| **House mic** (was −5.3) | Speech mic the singers don't need |
| KIDS LAPEL (was −12.0) | Speech, not in the brief |

**Two judgement calls to check on the first run-through:**

1. **Bass is out** because it wasn't in the brief. It's a DI, so it costs
   nothing in feedback, and singers often want it for pitch. One send to add it
   back if they ask.
2. **Pastor is out of this wedge.** He can still hear the singers through it —
   what's gone is *his own voice*. If he needs to hear himself on stage, use his
   P16 (Bank A slot 16, Bank B slot 13), not this wedge.

## Drums raised

Kick and Snare were at −32.1 and −30.2, about **27 dB under the vocals** —
inaudible, so there was no tempo reference at all. Now −18 and −16, roughly
12 dB under the vocals. Adjust by ear; this is a starting point.

## Correcting the open-mic count

Doc 00 and this session have carried three different numbers. The right one:

**12 microphones were in this wedge near unity. Now 10.** That is **+0.8 dB**
of gain before feedback — real, but modest.

An earlier count of "21 open mics" was wrong: it counted DI and line channels
(Bass, guitars, keys, LOOP), which cannot feed back acoustically. A later
attempt to classify by preamp gain was also wrong — the wireless vocal mics run
at 15.5 dB because the receivers output line level, so preamp gain does not
distinguish a microphone from a DI on this desk. Classify by what the source
physically is.

## This is still not the feedback fix

`FX7`, the ring-out GEQ on Bus 1, holds only an infrasonic high-pass:

```
20 Hz −15   25 −15   31 −15   40 −15   50 −12   63 −6   80 −3
```

Every band from 100 Hz up is flat. **The wedges have never been rung out.**
That remains the single biggest available gain, and it is worth far more than
the 0.8 dB here. Procedure: `checklists/ring-out-procedure.md`.

## Bus 1 fader

Left at −11.1 dB. Raise it by ear once you hear the cleaner wedge — do not
raise it before the ring-out.

## Verified

Every channel fader, main send, EQ, compressor and gate identical; mains and
all matrices identical; output patch identical; every FX slot identical;
buses 2–5 (other wedge mixes), 6/8/9 (P16 in-ears) and 7/13/16 (the stream)
all untouched. Only channel sends to Bus 1 changed.
