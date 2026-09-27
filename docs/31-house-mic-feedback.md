# 31 — House Mic (ch 23) Feedback

Fixed as far as a file can fix it, in `console/GHC BROADCAST V7.snap`. The rest is
fifteen minutes in the room.

---

## What the channel looks like

| | |
|---|---|
| Source | A-28, port named HOUSE |
| Preamp gain | **15.5 dB** |
| Phantom | off |
| HPF | 165 Hz, 24 dB/oct |
| Fader | **+4.1 dB** |
| Gate | EXP, −48 dB threshold |
| Compressor | 4:1, −35.5 dB, **30 ms attack** |
| Wedge send | −5.3 dB |
| EQ | three broad cuts — see below |

---

## Fault 1 — somebody has been fighting this mic with the wrong tool

| Band | Cut | Width |
|---|---|---|
| 250 Hz | −4.5 dB | **Q 2.50** |
| 646 Hz | **−5.9 dB** | **Q 1.68** |
| 2591 Hz | −4.1 dB | **Q 1.57** |

A **Q of 1.68 is nearly a full octave wide.** That −5.9 dB cut at 646 Hz is removing
most of the body from every voice that uses this microphone — and it is still
feeding back, because feedback lives in peaks a few hertz wide, not octaves.

This is the single most common mistake in church audio: reach for EQ, make the cut
too wide, lose the tone, keep the feedback. Fourteen and a half decibels of broad
subtraction have gone into this channel and it has bought almost nothing.

### What V7 does

**Keeps every cut's depth and frequency exactly. Narrows the Q.**

| Band | Before | After |
|---|---|---|
| 250 Hz | −4.5 dB, Q 2.50 | −4.5 dB, **Q 5.0** |
| 646 Hz | −5.9 dB, Q 1.68 | −5.9 dB, **Q 7.0** |
| 2591 Hz | −4.1 dB, Q 1.57 | −4.1 dB, **Q 7.0** |

This gives away **no feedback margin at all** — the attenuation at each ringing
frequency is identical. What it gives back is roughly two octaves of voice that was
being thrown away either side of each cut.

The mic should sound noticeably fuller and more intelligible immediately, with no
more tendency to ring than before.

## Fault 2 — the compressor is too slow

**30 ms attack** on a speech mic in a live room means the first 30 ms of every loud
syllable passes through uncompressed. That transient is exactly what starts a ring.

**V7 sets it to 8 ms.** Speech holds far more consistently, and the compressor now
catches the peak that was getting through.

## Fault 3 — the level. This one is yours to decide.

**The House mic sits at +4.1 dB.** It is the third hottest open microphone in the
building, behind the Pastor at +5.8 and Wireless 3 at +4.3.

I have not changed it, because someone pushed it up for a reason and quieter speech
is not a fix. But it is the largest single factor, and it is only that high because
the system has no headroom — see doc 27.

There is also a gain-staging point. The Pastor runs **25.5 dB** of preamp; the House
mic runs **15.5 dB** and makes up the difference on the fader. Gain belongs at the
preamp, where the gate and compressor can see it. Set the preamp so peaks reach
about **−10 dBFS**, and the fader should come back toward unity with the compressor
doing real work instead of the fader doing it.

## Fault 4 — a trap I created

**I unmuted Bus 16 "Slap" back in V1.** Six open microphones feed it at close to
unity — including this one at +0.1 dB — and it returns into Bus 1, the wedge mix.

Its fader is at −144, so it has been silent and is **not** causing your current
problem. But an open speech mic into a delay that returns to its own wedge is a
regenerative loop, and it was one fader move away from happening. Unmuting it
achieved nothing, because at −144 it fed nothing to the broadcast either.

**V7 re-mutes it.**

---

## Now do the fifteen minutes

V7 improves the tone and removes a trap. It does not remove the feedback, because
the ringing frequencies have never actually been measured.

### Ring out this one microphone

1. Everyone off the platform. All other channels muted.
2. Unmute **only ch 23**, placed exactly where it is really used.
3. Raise the main level slowly until it just begins to ring.
4. Solo the channel and read the **RTA**. Note the frequency.
5. Put a **narrow cut — Q 8 to 10, 3 to 6 dB** — at that frequency, on the
   **channel EQ** for mains feedback or on the **Bus 1 GEQ** for wedge feedback.
6. Raise again. Find the next one. **Stop after four.**
7. Back off 6 dB from the ring point.

Write the frequencies here so the next person inherits them:

| | Frequency | Depth | Where | Date |
|---|---|---|---|---|
| Notch 1 | | | | |
| Notch 2 | | | | |
| Notch 3 | | | | |
| Notch 4 | | | | |

### Check the automix

**Group X should contain ch 21, ch 23, ch 33 — and nothing else.** If ch 23 is not
in it, add it. With several speech mics open, automix is worth more on this channel
than any filter.

### Check the physical situation

Before any more EQ, answer these:

- **Where is this microphone actually used?** If it roams the room or gets carried
  toward the congregation, it will find every loudspeaker, and no console setting
  fixes that. A roaming mic needs mute discipline and a tight pattern, not EQ.
- **How close does the talker hold it?** Halving the distance is worth 6 dB — more
  than all four notches together.
- **Is it in front of a speaker?** Front fills and the centre cluster are the usual
  culprits.
- **What pattern is it?** If it is cardioid and it lives near the PA, a
  hypercardioid or supercardioid capsule will buy real rejection.

---

## Order of value for this microphone

| Action | Worth | Cost |
|---|---|---|
| Get the talker closer to it | **up to +6 dB** | free |
| Automix, if it is not already in group X | **+6 to +9 dB** on speech | 2 minutes |
| Ring it out with narrow notches | **+3 to +6 dB** | 15 minutes |
| Correct the preamp gain staging | +1 to +2 dB, better compression | 5 minutes |
| V7's narrower Q | 0 dB — but the voice comes back | done |
| More broad EQ | **roughly nothing** | costs you the tone |

The last line is why this channel has three octave-wide holes in it and still rings.
