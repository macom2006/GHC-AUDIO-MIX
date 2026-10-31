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
| ~~Pastor Lapel~~ | **WRONG — reverted in V16. See below.** |
| **House mic** (was −5.3) | Speech mic the singers don't need |
| KIDS LAPEL (was −12.0) | Speech, not in the brief |

**Two judgement calls to check on the first run-through:**

1. **Bass is out** because it wasn't in the brief. It's a DI, so it costs
   nothing in feedback, and singers often want it for pitch. One send to add it
   back if they ask.
2. ~~Pastor is out of this wedge.~~ **This was wrong — see "Corrected in V16".**

## Drums raised

Kick and Snare were at −32.1 and −30.2, about **27 dB under the vocals** —
inaudible, so there was no tempo reference at all. Now −18 and −16, roughly
12 dB under the vocals. Adjust by ear; this is a starting point.

## Correcting the open-mic count

Doc 00 and this session have carried three different numbers. The right one:

**12 microphones were in this wedge near unity. V15 made it 10; V16 restores
Pastor, so it is 11.** That is **+0.4 dB** of gain before feedback — real, but
very modest.

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

---

# Corrected in V16

**ch21 is a hand-held microphone, not a lapel.** The channel was labelled
"Pastor Lapel"; the stage box input has always read "PASTOR". I took the
channel name at face value and pulled it out of the wedge on that basis.

Both halves of that reasoning were wrong:

1. **He needs it.** A preacher has to hear himself on stage.
2. **The feedback argument did not apply.** A hand-held cardioid has far better
   gain before feedback than a chest-worn omni lapel. The thing I removed it
   for was not true of this microphone.

**V16 restores `ch21 → Bus 1` at −6.0 dB, byte-identical to its pre-V15 state,**
and renames the channel **"Pastor HH"** so the label cannot cause this again.

Open mics near unity: 11. The V15 cleanup is worth **+0.4 dB**, not +0.8.

## One interaction to watch

ch21's send to Bus 1 is **POST**, so the V11 leveller feeds the wedge:

| | |
|---|---|
| Leveller | −41 dB, 2:1, 400 ms release, **auto makeup on** |
| Expander | −54 dB — the only brake on makeup gain during pauses |

When he pauses, the leveller lifts gain and the wedge gets louder. That is the
moment a hand-held is most likely to ring, especially if it is set down or
pointed at the wedge.

Nothing is changed for it here — the levelling was asked for and it works. But
if his wedge starts ringing between sentences, that is the cause, and the fix is
his expander threshold, not the wedge EQ.
