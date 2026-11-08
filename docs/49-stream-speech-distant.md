# 49 — Stream speech sounds "picked up", not direct

**File:** `console/GHC BROADCAST V22.snap` (built on V21 — includes the Pastor
low-end fix, so load this instead of V21)

## Cause: V20. Mine.

| Into Bus 7 | V19 | V20 |
|---|---|---|
| Pastor HH, direct | +3.0 | +3.0 |
| Crowd L | −12.0 | **−8.0** |
| Crowd R | −12.0 | **−8.0** |
| Crowd, summed | −9.0 | **−5.0** |
| **Separation** | **12.0 dB** | **8.0 dB** |

The crowd mics hear Pastor **through the PA** — delayed by the distance from
speaker to microphone, and carrying the room's reverb. At only 8 dB below the
direct feed, that delayed reverberant copy sets the character of his voice. The
result is comb filtering and a distant, room-captured sound instead of a close
one.

Ruled out: **Pastor feeds none of the reverbs** — his sends to Bus 14, 15 and 12
are all off. The room sound is arriving entirely through the crowd mics.

Three things in V20 contributed, all mine:

1. **Send −12 → −8.** +4 dB of room.
2. **High-pass 254 → 150 Hz.** Added the low-mid room energy that muddies a
   voice most.
3. **Levelling: threshold −40, 4:1, 800 ms release.** This is the subtle one and
   possibly the largest. It made the crowd a *continuous* bed. For worship that
   is exactly right — it was the brief. Behind speech, a continuous bed of room
   sound is precisely what makes a voice sound distant.

I flagged risk 1 in doc 47 — *"stop when the mix starts to smear… that smearing
is the real limit here, not level"* — and then shipped −8 without hearing it.

## What V22 changes

| | V20/V21 | V22 |
|---|---|---|
| Crowd → Bus 7 | −8.0 | **−14.0** |
| Crowd high-pass | 150 Hz | **180 Hz** |

Separation goes from 8.0 dB to **14.0 dB** — wider than before V20, which is
deliberate: the V20 levelling raises the crowd's *average* level a long way at
any given send, so it needs to sit lower than it used to for the same presence.

**The levelling is kept.** It is right for worship and it is what makes a sparse
room read full. The problem was never the levelling, it was the level.

## The real fix is operational, not a snapshot

**A single crowd level cannot serve both worship and preaching.** Full and
continuous is right for one and wrong for the other.

You already have both tools, and neither needed building:

| Tool | Contents | Use |
|---|---|---|
| **Mute Group 6, named CROWD** | exactly ch29 + ch30 | **One-button crowd kill for the sermon** |
| **DCA 11, named CROWD** | exactly ch29 + ch30 | Ride it up for worship, down for speech |

Recommended: **hit Mute Group 6 when he starts preaching, release it for the
music.** That gives a full house during worship and a close, direct voice during
the message — which no fixed level can do.

If you would rather not mute it entirely, pull **DCA 11 down 10–12 dB** for the
sermon instead.

## Add to the pre-service checklist

> Crowd DCA 11 / Mute Group 6 — up for worship, down or muted for preaching.

## If speech is still not forward enough

In this order:

1. **Mute Group 6 during the sermon** — do this before changing any value.
2. **Crowd → Bus 7 to −18** if it is still smearing with the crowd in.
3. Only then look at Pastor's own chain. His direct send is already +3.0 dB,
   the hottest single source in the stream, so the problem is what sits behind
   him rather than how loud he is.
