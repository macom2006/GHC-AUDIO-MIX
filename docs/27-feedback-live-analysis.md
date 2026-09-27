# 27 — Feedback: What the Live File Shows

Read from `GHC BROADCAST V3.snap` as saved on the console **2026-09-26 18:10**.
V3 loaded correctly — Bus 7 BROADCAST is live, Bus 11 SUB FEED, Bus 13 BC VOX and
Bus 6 BAND STEM are all built, FX7 is a GEQ on the monitor bus, FX10 is the
multiband on the broadcast bus, automix group X is armed.

**And the feedback is worse, because of what has been done to it since.**

---

## The spiral, in the operators' own edits

Every one of these is a rational response to the previous one. Together they are a
death spiral, and the file records each step.

| Step | What was done | Reading |
|---|---|---|
| 1 | **Bus 1 STAGE MON pulled down 10.4 dB** (−0.7 → −11.1) | The wedges rang, so the whole wedge mix was choked |
| 2 | Musicians can now hear even less | Inevitable consequence of step 1 |
| 3 | **Four open mics pushed up 3.3 to 6.3 dB** on their Main 1 sends | Compensating for people not being heard |
| 4 | **The mains now ring too** | Those four mics are hot into the PA as well as the wedge |
| 5 | **Bus 2 pushed up 14.5 dB** (−14.8 → −0.3) | Trying to give someone monitor level another way |
| 6 | **Bus 2 is patched to no physical output** | That change did nothing at all |

### The four mics that are causing the mains to ring

| Ch | Name | Fader | Hidden Main-1 send | **Effective level** |
|---|---|---|---|---|
| **14** | Vox 2 (Dehil) | −0.9 | **+6.3** | **+5.5 dB** |
| **21** | Pastor Lapel | +2.5 | **+3.3** | **+5.8 dB** |
| **24** | Wireless 3 (Elsie) | −0.2 | **+4.5** | **+4.3 dB** |
| **23** | House | +0.7 | **+3.4** | **+4.1 dB** |

In March, not one microphone had a positive send to the main bus. Now four of them
are running **+4 to +6 dB hot**, and the gain is hidden in a send offset where nobody
looking at the faders would see it.

**That is why the mains started ringing.** It is not the room and it is not the EQ.

---

## You have no headroom left anywhere

| | Level |
|---|---|
| Main 1 master | **−0.08 dB** |
| Matrix 1 (PA L) | −0.5 dB |
| Matrix 2 (PA C) | −0.3 dB |
| Matrix 3 (PA R) | −0.7 dB |

Everything is at full output. There is nothing left to give. When a system is maxed
out and individual microphones are *still* being pushed up, the system is being asked
for more than it can deliver before it feeds back — and no arrangement of faders
fixes that.

**Open mics in the wedge mix: 13.** One more than in March, not fewer. That is
**11.1 dB** of gain before feedback surrendered before anyone touches a control.

---

## The two fixes that were shipped and never used

### The monitor GEQ is still perfectly flat

V3 put a 31-band graphic EQ on Bus 1 for exactly this. **Not one band has been
moved.** It is doing nothing, because a flat GEQ is a place to put notches, not a
fix in itself.

### Automix is armed but empty

`amix.x` is now **true** — good. But membership is set on the console and cannot be
carried in a snapshot, so unless somebody added channels 21, 23 and 33 to group X, it
is switched on and controlling nothing.

**Check this first. It is the fastest 6–9 dB available to you.**

---

## What is genuinely fine

So the search stays narrow:

- **Channel EQ is clean.** Across all thirteen open mics there is exactly one boost —
  a +1.1 dB high shelf on the Pastor. Nobody has been carving destructive EQ.
- **High-pass filters are correct** — 165 Hz on speech, 181–200 Hz on vocals.
- Preamp gains are unchanged since March.
- The broadcast chain is untouched and working.

This is purely a gain-structure and open-mic problem.

---

## `GHC BROADCAST V4.snap`

Three changes, built directly on your live file. **Nothing gets quieter.**

| # | Change | Effect |
|---|---|---|
| 1 | **The hidden Main-1 send offsets folded into the channel faders** on all six affected mics | Identical level — verified to 0.05 dB — but the gain is now visible on the fader instead of buried in a send page. Pastor now plainly reads **+5.8**, Vox 2 reads **+5.5**. |
| 2 | **Infrasonic high-pass on the Bus 1 GEQ** — 20–40 Hz at −15, 50 Hz at −12, 63 Hz at −6, 80 Hz at −3 | Wedges cannot reproduce these frequencies; all they do there is cause rumble, cone excursion and low-frequency ring. This is not speculative. **Every feedback-band slider is left flat for you to ring out.** |
| 3 | **Bus 2 returned to −14.8 dB** | It was pushed to unity but is patched to no output. Left at unity it is a trap for whoever patches it next. |

**Verified unchanged:** every preamp gain, every monitor send, Bus 1's level, the
whole broadcast chain, and the effective house level of all thirteen open mics.

V4 does not fix the feedback. It makes the problem visible and removes one trap. The
fix is the 90 minutes below.

---

## The 90 minutes that actually fixes it

Mid-week, empty room, nobody waiting.

### 1. Automix — 10 minutes, biggest single return

Add **ch 21 (Pastor), ch 23 (House), ch 33 (Kids Lapel)** to **automix group X**.
Pastor at weight 0. **No singers.** Test with two mics open and two people talking —
the idle mic must duck audibly.

**Expect 6–9 dB back on speech.**

### 2. Reduce the open mics — 30 minutes, second biggest

Thirteen mics in one wedge mix. Go through them with the musicians present:

- Anyone who is **not on the platform** during a given segment should not be in the
  wedge at all
- Anyone who can **hear themselves acoustically** does not need to be
- Anyone who needs the whole team belongs on **in-ears**, not the wedge

| Get down to | You recover |
|---|---|
| 8 mics | +1.8 dB |
| 6 mics | **+3.0 dB** |
| 4 mics | **+4.8 dB** |

### 3. Ring out the GEQ — 30 minutes

Everyone off the platform. One mic at a time, in its real position:

1. Raise its wedge send until it just rings
2. Find the frequency on the RTA
3. Pull **that GEQ band** down 3–6 dB — the graphic, not the parametric
4. Repeat. **Stop after 4–5 notches per mic.**
5. Back off 6 dB from the ring point

Log the frequencies in `08-monitors-iem.md`.

**Expect 3–6 dB back.**

### 4. Then, and only then, restore the levels — 20 minutes

Once the ceiling is raised:

- Bring **Bus 1** back up from −11.1 toward its proper level
- Bring the four hot mics back **down** toward 0 on their faders
- The Pastor at **+5.8 dB** is the number to watch. That is very hot for an open mic
  in a live room, and it is only that hot because there is no headroom. When the
  ceiling comes up, he should sit near unity.

---

## The thing behind all of it

Seven of your twelve singers still have no in-ear channel (doc 23). That is why
thirteen mics are in the wedge mix, which is why there is no headroom, which is why
the mics got pushed up, which is why the mains now ring.

**Bank B (doc 24) is already configured and waiting for the stage box.** Until that
arrives, steps 1 to 3 will hold the line. After it arrives, the problem stops being
something you manage.
