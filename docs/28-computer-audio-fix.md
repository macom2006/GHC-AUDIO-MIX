# 28 — Computer Audio: No Fader Control, No Subs

Both symptoms trace to four faults on the same signal. Fixed in
`console/GHC BROADCAST V5.snap`.

---

## Fault 1 — the computer is running through **two** live paths at once

| Path | Source | Fader | To Main 1 |
|---|---|---|---|
| **ch 34 "PC PLAYBACK"** | USB-1 | −6.0 | **ON at 0.0 dB** |
| **AUX 8 "PC"** | USB-1 | −8.8 | **ON at +0.8 dB** |

**The same audio, from the same port, into the same bus, twice.**

That is your missing fader control. Pull one down and the sound barely changes,
because the other copy is still at full level. It is also summing about **3 dB
hotter** than either fader suggests, and the two copies are phase-identical so they
add coherently.

Whoever built this almost certainly created one, could not find it later, and built
the other.

## Fault 2 — DCA 8 "PC" has a name but no members

DCA 8 is called "PC", sits at −2.2, has a colour and its LED lit. It looks like a
working DCA. **It controls nothing.**

The console records DCA membership in each channel's tag field, and the marker it
actually reads is `#Dn`. Compare:

| Channel | Tags | Works? |
|---|---|---|
| ch 1 Kick | `#D1,#D9,BAND,Drums,MGRP.1` | Yes — `#D1` and `#D9` present |
| **AUX 8 PC** | `PC` | **No** — the DCA's *name* is there, but no `#D8` marker |
| ch 34 PC PLAYBACK | `MGRP.1` | No DCA at all |

So the PC DCA was labelled but never actually assigned. Another reason moving a
fader did nothing.

## Fault 3 — both paths are on the wrong USB port

The console's own port configuration already tells you where the computer belongs:

| Port | Mode | Name |
|---|---|---|
| USB-1 | Mono | **KICK** |
| USB-2 | Mono | SNARE |
| **USB-7** | **Stereo** | **PC** |
| **USB-8** | **Stereo** | **PC** |

**USB-7/8 are already set up as a stereo pair and named PC.** Somebody configured
that deliberately. But both PC paths point at **USB-1** — a mono port labelled KICK.

You are hearing the computer because a Mac's system output lands on the first two
channels of its interface by default. So it works, in mono, on the wrong port.

**There is a latent trap here too:** the moment you run a virtual soundcheck, Logic
outputs 40 channels and USB-1 becomes the kick drum. Your "PC" channel would become
a kick.

## Fault 4 — no send to the subs. **That one is mine.**

When I built the aux-fed sub feed in V1, my source list was kick, floor tom, bass,
keys 1, keys 2, sax and loop. **I left the computer out.** Playback material is
full-range and mixed — it should absolutely reach the subs.

That is why video audio, walk-in music and anything else from the Mac has no low end
in the room.

---

## What V5 does

| # | Change | Why |
|---|---|---|
| 1 | **AUX 8 source: USB-1 → USB-7** | The correct stereo PC pair, as the port labels already say. Gets you stereo instead of mono. |
| 2 | **ch 34 shut down** — source OFF, muted, unassigned, all sends off, renamed `(PC - see AUX 8)` | Removes the duplicate. One path, one fader. |
| 3 | **AUX 8 tags: `PC` → `#D8,PC`** | DCA 8 now actually moves the computer |
| 4 | **AUX 8 → Bus 11 SUB FEED at −6 dB** | The missing subs |
| 5 | **AUX 8 → Bus 6 BAND STEM at −8 dB** | So the band hears playback in their in-ears |
| 6 | **AUX 8 → Bus 7 BROADCAST at −6 dB** | So playback reaches the stream (ch 34 carried this before; it moves with the path) |
| 7 | **AUX 8 → Main 1: +0.8 → 0.0 dB** | One path now, so unity is correct |

**Verified untouched:** every other channel fader, all preamp and port settings, the
monitor and house masters, and the whole broadcast chain.

---

## If the computer goes silent after loading V5

That means your Mac is outputting on channels 1/2, not 7/8. Two ways to resolve it,
and the first is better:

**Option A — point the Mac at 7/8 (recommended).** In macOS, or in whichever
application is playing back, set the output to WING channels **7 and 8**. Everything
then matches the labels, and virtual soundcheck can never collide with it.

**Option B — point the console back at 1/2.** Set AUX 8's source back to **USB-1**,
then set **USB-1 and USB-2 to stereo mode** and rename them `PC L` / `PC R`. You get
stereo, but you lose USB 1/2 for virtual soundcheck and you will have to remember
why.

---

## Check it worked

- [ ] Play something from the computer. **DCA 8 "PC" now moves it.**
- [ ] It is in **stereo** — pan-check by playing something with obvious width
- [ ] Only one fader affects it — AUX 8. Channel 34 is dark.
- [ ] **You can feel it in the subs.** Play something with real low end.
- [ ] It reaches the stream — solo Bus 7 and confirm
- [ ] The band can hear it in their in-ears
- [ ] Level sits where you expect with DCA 8 near unity — if it is now much quieter
      than before, that is the duplicate copy no longer doubling it. Bring AUX 8 up.
