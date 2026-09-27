# 30 — Recording and Playback Without Logic Pro

Logic is out of the system entirely — not just the live broadcast path, but recording
too. This document replaces `docs/10-logic-pro.md`.

**This is a simpler and more reliable system than what you had.** The console already
contains everything you need.

---

## Two consequences, one good and one to fix

### Good: the USB dropout problem goes away

With no multitrack recording, the Mac only has to play back two channels of audio.
And it does not need USB for that at all.

`GHC BROADCAST V6.snap` moves PC playback from **USB-7** to the **analog AUX IN 5/6**
stereo pair on the rear panel — currently free. No drivers, no sample rate to
negotiate, no aggregate device, no clock to drift, nothing for macOS to suspend.

**Wire the Mac's headphone or line output into AUX IN 5 and 6** with a
3.5 mm-to-dual-¼" cable. Set the Mac's output volume to about 75% and trim AUX 8 by
ear. Then set the Mac's system output back to its own hardware, not the WING.

That is the dropout fixed, permanently, by removing every part that could fail.

### To fix: nothing is recording your services

**Your WING-LIVE slots are empty.** I flagged this from the rear-panel photo; with
Logic gone it now matters a great deal. Right now no recording of any kind is being
made.

---

## Record on the console instead

The WING has two independent recorders built in. Neither needs a computer.

| | WING-LIVE SD | 2-track USB |
|---|---|---|
| Tracks | **32 per slot, two slots** | Stereo |
| Source | Channel direct outs | **Main 1 L/R** (already patched) |
| Format | 24-bit / 48 kHz | 24-bit / 48 kHz |
| Media | SD / SDHC card | USB stick |
| Needs a computer | **No** | **No** |
| Status | **Cards not fitted** | Ready |

Both are already configured in your show file — 32 tracks on each SD slot, and the
2-track patched from the house master. They just need media.

### What to buy

- **2 × SD cards, V30 / U3 rated, 128 GB.** The speed rating matters more than the
  size — a slow card will drop samples during 32-track writes.
- **1 × USB stick, 64 GB**, for the stereo recorder.

32 tracks × 24-bit × 48 kHz is roughly **330 MB per minute**, so a two-hour service is
about **40 GB**. A 128 GB card holds three services.

### Set-up, once

1. **Format both cards in the console.** Not on a computer.
2. Confirm both slots show 32 tracks
3. Insert the USB stick and confirm the 2-track recorder sees it
4. **Do a full-length test recording** and play it back before you rely on it

### Weekly

- Format the card before the service
- **Start both recorders 15 minutes before the service.** Disk is cheaper than a
  missed sermon.
- Stop and eject after
- **Copy to the church server before leaving the building**
- Archive: `/Archive/YYYY/YYYY-MM-DD/`

### Which 32 channels

You run 40 channels and the recorder takes 32, so eight have to go. Drop these:

| Drop | Why |
|---|---|
| ch 19 LEAD1 | No input source |
| ch 28, 31, 32, 35, 37, 38, 39 | Unnamed, unused or duplicates |

That leaves all the drums, bass, guitars, keys, tracks, every vocal, the speech
channels and both crowd mics — everything anyone would ever want.

---

## Virtual soundcheck still works

This is the part people assume they lose. You do not.

**The WING-LIVE card plays back as well as records.** Each slot has a `playmode`
setting, already set to PLAY on both.

1. Insert last Sunday's card
2. Set each channel's **Alt Source** to the matching SD playback track
3. **Pull the PA down** — you are about to play a full band into an empty room
4. Flip the global **Alt Source** switch
5. Press play. The console behaves exactly as it did on Sunday.
6. Mix, experiment, train a volunteer, ring out a microphone
7. **Flip back to Main Source when you finish.** Put a label on the console — an
   Alt Source left engaged on a Sunday morning means total silence and a panicking
   operator.

This is better than the Logic version: no computer, no USB, no session file, no
driver. Insert a card and press play.

**Use it every week.** A team that rehearses its mix mid-week sounds dramatically
better than one that only ever mixes live under pressure — and right now you have a
feedback problem that needs exactly this kind of unhurried, empty-room work.

---

## What the Mac is still for

| Job | How |
|---|---|
| Walk-in and playback music | Analog out → **AUX IN 5/6** |
| Video audio | Same path |
| Loudness metering on the stream | Optional — a meter plugin fed from the stream return |

The Mac is no longer in any critical path. If it fails mid-service, you lose walk-in
music. Nothing else.

---

## What this means for the rest of the documentation

| Document | Status |
|---|---|
| `10-logic-pro.md` | **Superseded by this document.** Kept for reference if multitrack ever returns. |
| `17-logic-broadcast-rig.md` | Already superseded — broadcast moved to the WING in doc 18 |
| `13-service-runsheet.md` | "Start Logic recording" now means "start both console recorders" |
| `checklists/pre-service.md` | Same |
| `21-stem-measurements.md` | Still valid; it measured the template's own stems |

---

## The honest trade

**What you lose:** 40-channel recording (you get 32), and the convenience of editing
in a DAW straight after the service. For podcast or clip production, you now copy
the card first.

**What you gain:** no computer in the recording path. No driver updates, no operating
system, no disk contention, no sample rate, no crash. A card goes in and a button
gets pressed.

For a volunteer-run church, that trade is strongly worth making. The recording that
actually happens every week beats the better recording that depends on a laptop
behaving.

---

## Do this week

- [ ] Buy 2 × 128 GB V30/U3 SD cards and a 64 GB USB stick
- [ ] Format both cards **in the console**
- [ ] Wire the Mac's output into **AUX IN 5/6** and set the level by ear
- [ ] Set the Mac's system output back to its own hardware
- [ ] Full-length test recording, then **play it back**
- [ ] Add "start both recorders" to the pre-service checklist
- [ ] Run one virtual soundcheck from the card to prove the workflow
