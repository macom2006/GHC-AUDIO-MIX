# 47 — Making the crowd read as a full house

**File:** `console/GHC BROADCAST V20.snap` (built on V19)
**Channels:** 29 CROWD L (A-23), 30 CROWD R (A-24)

## The scope, stated plainly

This makes the **real congregation** read full and present on the stream. That
is ordinary broadcast practice — every televised event does it.

It does not fabricate an audience. Canned crowd under a half-empty room is the
kind of thing viewers notice, and for a church the credibility cost is far
higher than the gain. Nothing here adds a single person who is not in the room.

## Why this is risk-free

| | |
|---|---|
| Crowd → Main 1 | **off** (−144) |
| Crowd → any other main | off |
| Crowd → any bus | **Bus 7 only** |
| Crowd → P16 | taps **A-23/A-24 direct off the stage box**, bypassing the console |

So channel processing on ch29/30 reaches **the stream and nothing else.** No
PA, no wedges, no in-ears, no feedback exposure. Verified before anything was
changed.

## What actually makes a room sound full

Not reverb. **Continuity.**

A sparse room peaks when people clap and falls silent between. A full room is a
*continuous bed* — breathing, shuffling, murmur, clap tails — that never drops
out. Your crowd compressor was set at −28, 2:1, which only catches the peaks and
leaves the bed below the threshold where nobody hears it.

### The changes, per channel

| | V19 | V20 | Why |
|---|---|---|---|
| Comp threshold | −28 | **−40** | Now works on the quiet bed, not just claps |
| Comp ratio | 2:1 | **4:1** | Lifts the bed, holds the peaks down |
| Comp attack | 80 ms | **150 ms** | Slow, so claps keep their snap |
| Comp release | 400 ms | **800 ms** | Long, so the room never falls silent |
| Comp makeup | +2.0 manual | **0.0** | Auto makeup does it now |
| High-pass | 254 Hz @ 24 dB/oct | **150 Hz** | 254 strips the chest out of a crowd; human mass lives 100–250 Hz |
| → Bus 7 | −12.0 | **−8.0** | +4 dB more of it in the stream |

Fourteen values. The compressor is doing upward levelling — the gain reduction
meter should sit busy and fairly static rather than jumping.

### Deliberately left alone

- **Parametric EQ.** The gentle cuts at 680 Hz and 4.2 kHz are defensible as
  they are, and tonal changes wait for a recording.
- **The gate stays OFF.** Gating ambience is precisely what makes a room sound
  empty. It was already off; it should stay off forever.
- **Pan hard L/R, width 0.** Already as wide as it goes.
- **Channel faders.** Untouched, so DCA 11 still works as before.

## If it is still not enough

In this order:

1. **Bus 7 send −8 → −6.** Simplest lever. Stop when the mix starts to smear —
   the crowd mics also hear the PA, and too much of them comb-filters against
   the direct feed. That smearing is the real limit here, not level.
2. **High-pass 150 → 120 Hz.** More body again, but more HVAC rumble too.
3. **Reverb.** `FX4` (ST-DL, a stereo delay) is the **only free FX slot** on the
   desk. A room reverb there, fed from the crowd, would genuinely enlarge the
   space. I have not done it: changing an FX slot's model replaces its entire
   parameter set, and choosing a decay time without hearing the room is the
   mistake that produced V11. **Send a full-band recording with congregation
   and I will set it against measurement.**

## The ceiling

Two crowd mics on a sparse room can be made to sound like a well-captured room.
They cannot be made to sound like twice as many people. If the congregation
genuinely needs to read bigger, **more microphones placed among the people** beat
any amount of processing — a second pair further back would do more than
everything in this document.
