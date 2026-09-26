# 24 — P16 Bank B: the Second Ultranet Feed

**Implemented in `console/GHC BROADCAST V3.snap`.** The console is now pre-configured
for a second personal-monitoring bank. It does nothing until the hardware arrives,
and it breaks nothing in the meantime.

---

## A correction to what I said in doc 23

I wrote that a second box gives you "thirty-two channels, every singer gets their
own." **That was misleading.** Two Ultranet hubs are two *separate* 16-channel buses.
A P16-M plugs into one hub and sees that hub's sixteen channels — it cannot see the
other bank's.

So this is not one 32-channel system. It is **two banks of sixteen, each of which
must stand on its own.** That changes the design, and the layout below reflects it:
Bank B carries a stereo **band stem** rather than discrete instruments, because the
vocal team on Bank B cannot reach Bank A's channels.

---

## The hardware you need

One AES50 stage box with a **P16 / Ultranet output port**, connected to the WING's
**AES50 port B** (currently completely unused — I verified, zero patches on it).

| Option | In / Out | Notes |
|---|---|---|
| **Behringer SD16** | 16 in / 8 out | Current generation. The one I would buy. |
| Behringer S16 | 16 in / 8 out | Older, widely available second-hand |
| Midas DL16 | 16 in / 8 out | Midas build, same function |

**Confirm the unit has a P16/Ultranet port before you buy.** Not every AES50 box does.

You are buying it for the Ultranet port, not the inputs — but those 16 extra inputs
are a useful bonus if you ever outgrow the S32.

Cabling: one shielded Cat5e from WING **AES50 B** to the box, then Cat5e from the
box's **Ultranet** port to a P16-D distributor or the first P16-M in the chain.

---

## Bank B channel layout

| P16 ch | Source | Who / what |
|---|---|---|
| **1** | Bus 6 L | **BAND STEM L** |
| **2** | Bus 6 R | **BAND STEM R** |
| 3 | A-26 | Marie *(ch 13)* |
| 4 | A-30 | Dehil *(ch 14)* |
| 5 | A-27 | Gabby *(ch 15)* |
| 6 | A-29 | Peggy *(ch 16)* |
| 7 | A-22 | **David — lead** *(ch 20)* |
| 8 | A-20 | Raissa *(ch 22)* |
| 9 | A-18 | Elsie *(ch 24)* |
| 10 | A-21 | Jude *(ch 25)* |
| 11 | A-19 | Brenda *(ch 26)* |
| 12 | A-17 | Martha *(ch 27)* |
| 13 | A-25 | Pastor *(ch 21)* |
| 14 | A-23 | Crowd 1 |
| 15 | A-24 | Crowd 2 |
| 16 | Bus 10 L | Talkback |

**All ten singers now have their own channel.** Each one can put their own voice
where they want it, hear the rest of the team at whatever level suits them, and get
the whole band from one stereo pair.

That is the fix. The seven singers who had nothing now have everything they need,
and the reason they were demanding wedge disappears.

### Why both output blocks are patched

The console patch fills **AES50-B outputs 1–16 *and* 33–48** with the identical
layout. Different stage boxes mirror different output blocks to their Ultranet port —
your S32 uses 33–48, but an S16 may use 1–16.

Rather than guess and hand you a dead feed, I patched both. Port B is otherwise
unused, so it costs nothing, and the Ultranet will work whichever block your new box
reads. Once you know which one it uses, clear the other sixteen for tidiness.

---

## The BAND STEM — Bus 6

Bus 6 was unnamed, muted, at −∞, with one stray send and no output patch. It is now
the band stem.

| | |
|---|---|
| Name | **BAND STEM** |
| Format | Stereo |
| Fader | 0 dB |
| Assigned to mains | **None** — monitors only, it can never reach the house or the stream |
| Send mode | **PRE-fader** — FOH fader moves cannot alter anyone's in-ear mix |

### Starting levels

| Ch | Source | Send |
|---|---|---|
| 1 | Kick | −4.0 |
| 2 | Snare | −5.0 |
| 3 | HH / Snr Btm | −10.0 |
| 4 | Rack 1 | −8.0 |
| 5 | Rack 2 | −8.0 |
| 6 | Floor | −8.0 |
| 7 | Overheads | −6.0 |
| 8 | **Bass** | **−3.0** |
| 9 | Electric Gtr | −6.0 |
| 10 | Acoustic Gtr | −6.0 |
| 11 | Keys 1 | −6.0 |
| 12 | Keys 2 | −6.0 |
| 17 | Sax | −8.0 |
| 18 | Loop | −6.0 |
| 34 | Playback | −8.0 |

Bass sits highest and kick close behind, because that is the rhythmic anchor singers
need. Adjust by ear at the first rehearsal with a singer wearing in-ears telling you
what they need — this is a starting point, not a verdict.

---

## Bank A is deliberately untouched

I verified AES50-A outputs 33–48 are **byte-identical** to your original file.
Nobody's existing P16 layout moves, nobody has to relearn channel numbers, and there
is zero risk to the musicians already using the system.

Bank A still has the faults in doc 23 — thirteen channels fed from raw inputs, and
the keys arriving as two mono left-legs. Those are worth fixing, but they are
separate decisions that affect people's working mixes, so they belong at a rehearsal
with those people present, not in a generated file.

---

## Who plugs into which bank

| Bank | Fed from | For |
|---|---|---|
| **A** — S32 Ultranet | AES50-A outs 33–48 | **The band.** Discrete drums, bass, guitars, keys, tracks. |
| **B** — new box Ultranet | AES50-B outs 1–16 | **The vocal team.** Discrete voices plus a band stem. |

A musician who needs both discrete instruments *and* discrete voices — a worship
leader who plays acoustic, for instance — should be on **Bank A**, with the vocal
stem on Bus 9 ("WL BUS P16", already built and fed by all the singers) giving them
the team.

---

## Commissioning, when the box arrives

- [ ] Shielded Cat5e from WING **AES50 B** to the new box. Confirm the WING shows the
      link as connected and green.
- [ ] Cat5e from the box's **Ultranet** port to the P16-D or first P16-M
- [ ] Power up a P16-M and check all sixteen channels show signal
- [ ] **If channels are silent**, the box mirrors the other output block — everything
      is already patched there too, so check the box's own Ultranet source setting
- [ ] Set the **BAND STEM** level with a singer wearing in-ears, at rehearsal
- [ ] Sit each singer down and build their mix with them, once. Twenty minutes each,
      and you will not have to do it again.
- [ ] **Then reduce the wedge mix.** This is the point of the whole exercise — see
      doc 22. With every singer hearing themselves properly, pull the vocal sends to
      Bus 1 down one at a time and find out who genuinely still needs a wedge.
- [ ] Re-ring the wedges once the open-mic count is down. You will find you have far
      more headroom than before.

---

## What this actually buys you

| | Before | After |
|---|---|---|
| Singers with their own in-ear channel | 5 of 12 | **12 of 12** |
| Open mics in the wedge mix | 12 | as few as you can negotiate |
| Gain before feedback lost to open mics | **−10.8 dB** | −6 dB at 4 mics, −4.8 dB at 3 |
| Band members hearing the vocal team | via Bus 9 stem | unchanged |
| Vocal team hearing the band | not at all, for 7 of them | stereo band stem |

The feedback problem, the monitor complaints and the wedge dependency are all one
problem with one cause. This is the fix for it.
