# 22 — Feedback: Diagnosis and Cure

You reported heavy feedback on the stage monitors and the mains. I found the cause
in the console file. **It is not an EQ problem.** EQ is what you reach for after you
have fixed the real cause, and in your system the real cause is arithmetic.

---

## The cause

**Your wedge mix has 22 sources in it, and 12 of them are live open microphones.**

| Ch | Name | Send to Bus 1 | High-pass |
|---|---|---|---|
| 13 | Vox 1 (Marie) | **−4.9 dB** | 200 Hz |
| 14 | Vox 2 (Dehil) | **−4.9 dB** | 200 Hz |
| 15 | Vox 3 (Gabby) | **−5.2 dB** | 200 Hz |
| 16 | Vox 4 (Peggy) | **−5.2 dB** | 200 Hz |
| 20 | LEAD2 (David) | **−5.0 dB** | 185 Hz |
| 21 | Pastor Lapel | **−6.0 dB** | 149 Hz |
| 22 | Raissa | **−5.7 dB** | 185 Hz |
| 23 | House | **−5.3 dB** | 147 Hz |
| 24 | Wireless 3 (Elsie) | **−5.6 dB** | 189 Hz |
| 25 | Jude | **−5.3 dB** | 181 Hz |
| 26 | Brenda | **−5.2 dB** | 185 Hz |
| 27 | Wireless 4 (Martha) | **−5.3 dB** | 183 Hz |

Every one of them is within 1.1 dB of the others. They are all, effectively, at full
level in the same wedge mix.

### The arithmetic

Every time you double the number of open microphones feeding a loudspeaker, you lose
**3 dB** of gain before feedback. It is not a rule of thumb; it is how correlated
acoustic energy sums.

| Open mics | Headroom lost |
|---|---|
| 1 | 0 dB |
| 2 | −3 dB |
| 4 | −6 dB |
| 8 | −9 dB |
| **12** | **−10.8 dB** |

**You are starting 10.8 dB in the hole before anyone touches a fader.** No graphic
EQ, no notch filter and no feedback suppressor recovers 10.8 dB without destroying
the tone of every microphone on the platform.

That is why it feels like "the EQ is bad." The EQ is not bad. It is being asked to
do something EQ cannot do.

---

## Three contributing faults I also found

### 1. There is no graphic EQ on the monitor bus

Bus 1 "STAGE MON" has a de-esser and a speaker-manager on it, but **no GEQ at all.**
There is nowhere to put a feedback notch. What tone shaping exists is four broad
cuts on the bus parametric at **Q 1.0** — that is roughly a full octave wide each.

Broad cuts are the wrong tool. A Q of 1.0 at 143 Hz removes the body from every
voice and instrument in the wedge while barely touching the narrow resonance that is
actually ringing. Feedback lives in peaks a few Hz wide. You need **Q 8–10**.

So the monitor mix has been dulled to buy headroom, and it still rings.

### 2. Automix is off

Nine of those open mics are speech-capable. Automix exists precisely to hold down
the microphones nobody is talking into. Running it on the speech channels typically
recovers **6–9 dB** of gain before feedback during announcements, prayer and the
sermon — the moments you are most likely to ring.

### 3. The house master has a broad bass boost

Main 1 carries a **+3 dB low shelf at 100 Hz**. A wide low-frequency boost on the
master raises low-mid ring across the whole room. Meanwhile your PA graphic EQs
(FX12/13/14) have **no correction at all below 315 Hz** — so nothing downstream is
taking that energy back out.

**A further note on those PA graphics:** all three are set identically. Left, centre
and right are three different loudspeakers covering three different parts of the
room, and they cannot share one correction curve. Only one zone was ever measured.

---

## The cure, in order of effect

### FIRST — reduce the number of open mics  (recovers up to 6 dB, costs nothing)

This is the fix. Everything below is secondary.

| Reduce wedge mix to | You get back |
|---|---|
| 8 open mics | +1.8 dB |
| 6 open mics | **+3.0 dB** |
| 4 open mics | **+4.8 dB** |
| 3 open mics | **+6.0 dB** |

**How to decide who stays.** Stand where each singer stands. Ask: *can they hear
themselves without the wedge?* Most cannot hear themselves and genuinely need it.
Most of the other eleven voices they do **not** need — they can hear those people
acoustically, standing three feet away.

The target is: each wedge carries **the voice of the person standing in front of it**,
plus the instruments they need, and little else.

Do this at rehearsal, with the musicians present, one at a time. It is their mix, so
they get a say — but explain the trade: every voice they add to the wedge costs the
whole platform headroom.

**If a singer needs to hear the whole team, that is what in-ear monitoring is for.**
You already have buses programmed for it.

### SECOND — ring out the monitors properly  (recovers 3–6 dB)

`GHC BROADCAST V2.snap` puts a **31-band graphic EQ on Bus 1**, flat and ready. The
procedure:

1. Everyone off the platform. All channels muted.
2. Unmute **one** microphone, placed exactly where it will actually be used.
3. Raise the wedge send slowly until it just begins to ring.
4. Find the frequency — solo the channel and read the RTA.
5. On the **GEQ**, pull that band down **3–6 dB**. Not the parametric, not broad.
6. Raise again. Find the next ring. Repeat.
7. **Stop after 4–5 notches.** More than that and you are destroying the microphone
   to solve a placement problem.
8. Back off 6 dB from the ring point. That is your working headroom.
9. Write the frequencies into the notch log in `08-monitors-iem.md`.

Repeat for each wedge position that matters.

### THIRD — turn on automix  (recovers 6–9 dB on speech)

Armed in V2, but **membership has to be set on the console** — it is not carried in
a snapshot file.

- Automix **group X**
- Members: **ch 21 (Pastor), ch 23 (House), ch 33 (Kids Lapel)** — and any other
  speech-only mic
- Pastor at weight **0 dB**
- **Do not add the singers.** Automix attenuates whatever is not loudest, which is
  exactly wrong for a vocal team singing together.

Test it: two mics open, two people talking. The idle mic should duck audibly.

### FOURTH — placement  (free, and more effective than any processing)

- **Get the microphone closer to the mouth.** Halving the distance gives 6 dB. That
  is more than any notch filter will ever return.
- **Get the wedge out of the microphone's pattern.** A cardioid mic rejects most
  strongly at 180° behind it. The wedge should be there, not off to the side.
- **Wedges belong on the floor angled up at the face**, not aimed across the platform.
- **Lower the wedge.** Musicians accept slightly less monitor far more readily than
  they accept a service interrupted by squealing.

---

## What `GHC BROADCAST V2.snap` changes

Eight changes on top of V1. Every musician's monitor send, every preamp gain, every
channel fader and all the PA room EQ are untouched — verified field by field.

| # | Change | Effect |
|---|---|---|
| 1 | **FX7** — a 5-band tone shaper set to **+4.3 dB "air"** sitting on the Kids Lapel mic → reassigned as a **31-band GEQ on Bus 1 STAGE MON**, flat | You now have somewhere to put monitor notches. An air boost on an open lapel mic was also working against you. |
| 2 | **FX11 restored to ch 33** | V1 removed this, which was my mistake — see below |
| 3 | **FX10** — SPKMAN was a *second* high-frequency tamer on the monitor bus, duplicating FX9 → reassigned as the **C5-CMB multiband on Bus 7 BROADCAST** | Frees a redundant slot, and the broadcast bus gets its multiband |
| 4 | **ch 21 Pastor** high-pass 149 → **165 Hz** | Free gain before feedback; no useful speech energy down there |
| 5 | **ch 23 House** high-pass 147 → **165 Hz** | Same |
| 6 | **ch 33 Kids Lapel** high-pass 133 → **165 Hz** | Same |
| 7 | **Main 1 low shelf +3.0 → +1.0 dB @ 100 Hz** | Reduces low-mid ring in the room |
| 8 | **Automix group X armed** | Membership still to be set on the console |

### A correction to V1

**V1 removed FX11 from ch 33, and that was wrong.** That slot held a graphic EQ with
genuine ring-out work in it — notches at 125, 160, 1.6k and 2 kHz plus a steep
low-frequency rolloff. Somebody had already tuned that lapel mic against feedback,
and I took it away to free a slot. **V2 restores it byte-identical.**

If you have already loaded V1, load V2 — it contains everything V1 did, with this
fixed.

### A correction to what I told you about SPKMAN

I described FX10 "SPKMAN" as a Sound Maxer / exciter and said it was questionable on
a monitor bus. Having now read its parameters, it is a **speaker-management
processor** — high-pass, low-pass, tilt, phase, polarity, distortion, dynamic EQ and
limiter — and on your monitor bus it was configured as a dynamic high-frequency
*reducer* at 7.35 kHz, not a booster. It was not causing feedback. It was reclaimed
because **FX9 (DE-S2) on the same bus already does that job**, not because it was
harmful.

---

## What I deliberately did NOT change

**Every monitor send from every channel.** Musicians' mixes belong to musicians.
Reducing the twelve open mics is the single most effective fix available to you, and
I am not making that decision from a data file — it has to be made at rehearsal,
with the people who have to hear it.

I also left the monitor bus parametric EQ alone. Those broad cuts are the wrong tool,
but they may be load-bearing right now. Ring out properly with the new GEQ first,
then come back and widen those cuts back toward flat one at a time, listening.

---

## Realistic expectation

| Action | Recovered |
|---|---|
| Reduce to 4–6 open mics in the wedge | **+3 to +5 dB** |
| Ring out with the new GEQ | **+3 to +6 dB** |
| Automix on speech | **+6 to +9 dB** on speech passages |
| Higher speech high-pass | +1 to +2 dB |
| Microphone placement | **+3 to +6 dB** |

Done together, that is **15–20 dB** of gain before feedback. Your problem will be
gone, not managed.

Done as EQ alone, you will get perhaps 3 dB and a duller monitor mix. That is the
road you are currently on, and it is why it feels like the EQ is the problem.

---

## The one thing that is not a console fix

If the room itself is highly reverberant — hard walls, hard ceiling, reverberation
time over about 1.5 seconds — feedback will keep returning no matter what you do at
the desk, because the microphones are hearing the room as much as the source.

Absorption on the rear wall and ceiling fixes it permanently, for every service,
forever. It is a building project rather than an audio purchase, and at some point
it becomes the only remaining answer.
