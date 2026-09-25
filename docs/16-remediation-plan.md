# 16 — Remediation Plan

Ordered fix list for the GRACELAND WING, derived from
[`00-audit-2026-03-18.md`](00-audit-2026-03-18.md).

**Do this work mid-week, not on a Sunday.** Export the current show file to USB
first, and again after each stage, so every step is reversible.

**Before you start:** `Setup → Show → Save As` → `GHC-2026-03-18-PRE-REMEDIATION`.
Copy it to a USB stick and to the church server. Nothing below is dangerous, but
everything below is easier to undo from a backup than from memory.

---

## Stage 0 — Backup and label (30 min, zero risk)

Housekeeping first. It makes everything after it safer.

| Step | Action |
|---|---|
| 0.1 | Export the current show file to USB **and** the church server |
| 0.2 | Name **ch 33** (currently unnamed, live at −4.0 dB, sourced from LCL-1 "KIDS LAPEL"). Name it `KIDS LAPEL` and colour it with the speech group. |
| 0.3 | Name or clear ch 28, 31, 32, 35, 37, 38, 39. If a channel has no purpose: source `OFF`, fader −∞, muted. |
| 0.4 | Resolve **ch 3**: is A-3 a hi-hat or a snare bottom mic? Walk to the stage and look. Fix whichever label is wrong. If it is a hi-hat, raise the HPF from 82 Hz to **350 Hz**. If it is a snare bottom, set HPF **200 Hz** and **invert polarity**. |
| 0.5 | Resolve **ch 17 / 18 / A-15**. Both channels share one input labelled "TRACK". Decide what A-15 actually is and rename all three consistently. |
| 0.6 | **Ch 19 "LEAD1"** has no source but is routed to Main 1 and Bus 9. Either patch it to a real input or set it fully off. |
| 0.7 | **Ch 34 "PC PLAYBACK"** is sourced from USB-1 ("KICK"). The PC pair is USB-7/8. Repatch to USB-7 (and make it a stereo pair with USB-8). |
| 0.8 | Clear dead outputs: **LCL out 1** (sourced from non-existent A-33) and **AUX outs 1, 2, 5, 6, 7, 8** (all fed from muted Bus 5 L). Set them `OFF` or patch them to something real. |
| 0.9 | Turn **off** the disabled 40.5 ms delay stored on Main 1, or set it to 0. |

---

## Stage 1 — Scene safes (20 min) — **highest priority**

Nothing else is safe until this is done. `Setup → Global → Safes`.

### Set these safes ON

| Safe | Scope | Why |
|---|---|---|
| **Source / preamp** | **All groups** (LCL, AUX, A, B, C, SC, USB, CRD, MOD, PLAY, AES, USR, OSC) | Gain is set for the person on the mic today. No recall may ever change it. |
| **Output patch** | **All groups** | Physical routing is a property of the building, not of a scene. |
| **Bus 1** (STAGE MON) | Channel safe | Musicians' monitor mix must survive every recall |
| **Bus 8** (DRUMS) | Channel safe | Same |
| **Bus 9** (WL BUS P16) | Channel safe | Same |
| **Matrix 1, 2, 3** | Safe | PA room EQ and delay alignment |
| **Matrix 4** | Safe | Sub alignment |
| **Matrix 5** | Safe | Broadcast chain and lip-sync delay |
| **Main 1 master fader** | Safe | The operator owns the house level |
| **Ch 21** (Pastor Lapel) | Mute safe | Never muted by a scene change mid-sermon |

### Verify it works

1. Store the current state as a test scene.
2. Change a preamp gain by 10 dB, pull a monitor bus down, change the house master.
3. Recall the test scene.
4. **The gain, the monitor bus and the master must not move.** Everything else should.
5. Delete the test scene.

Do not skip step 4. An untested safe is not a safe.

---

## Stage 2 — Reconnect the broadcast path (45 min)

> **Resolved.** The broadcast mix is built in **Logic Pro** and leaves via a **Volt
> 276** into the Osee. Full detail, including the clock-domain problem that now
> outranks everything in this stage, is in
> [`17-logic-broadcast-rig.md`](17-logic-broadcast-rig.md).
>
> **Do doc 17 priority items 1–4 before this stage.** Then come back and use
> **Path C-revised** below, which converts the WING's orphaned broadcast path into
> your emergency failover rather than a duplicate mix.

### First, regardless of the answer — make the stream independent of the house

| Step | Action |
|---|---|
| 2.1 | `Main 1 → send to MX5`: change from **post-fader to PRE-fader**. The house master will then no longer move the stream. |

### Path A — the Osee is fed analog from the WING (recommended target)

| Step | Action |
|---|---|
| 2.2a | **Unmute Bus 7 "BROADCAST"** |
| 2.3a | Patch **Matrix 5 L/R → LCL out 5 and LCL out 6** (LCL 6 currently carries PA C — move PA C to a free local output or to a stage box output first) |
| 2.4a | Set the Matrix 5 output trim so the Osee's meters read **−12 dB average, −6 dB peak**. The WING is +4 dBu; most compact switchers are −10 dBV inputs. See `11-osee-video-integration.md`. |
| 2.5a | Decide whether Main 1 still feeds MX5 at all. Once Bus 7 carries a real mix, **turn `Main 1 → MX5` off** so the stream is purely the broadcast mix. Until then, leave it on but pre-fader. |

### Path B — the stream comes from a computer over USB

| Step | Action |
|---|---|
| 2.2b | **Unmute Bus 7 "BROADCAST"** |
| 2.3b | Repatch **USB out 43 ← Matrix 5 L** and **USB out 44 ← Matrix 5 R** (currently both carry Bus 4 L) |
| 2.4b | Clear USB out 47/48 (currently both carry muted Main 4 L) or repatch them to something real |
| 2.5b | In OBS, select the WING USB device, channels 43/44, 48 kHz stereo |

### Path C-revised — **use this one.** Broadcast lives in Logic; the WING path becomes failover

| Step | Action |
|---|---|
| 2.2c | **Unmute Bus 7 "BROADCAST"** |
| 2.3c | Add the missing drum sends to Bus 7 (step 2.6 below) — without them the failover mix has no kit |
| 2.4c | Keep Matrix 5 fed from Bus 7 at 0 dB with its existing chain |
| 2.5c | Patch **Matrix 5 L/R to two spare outputs**, wired to a **second Osee input** labelled "EMERGENCY AUDIO" |
| 2.6c | Clear the junk USB patches: outs **43, 44, 47, 48** |
| 2.7c | Decide about the MADI card — document what it connects to, or set ch 35 / ch 36 fully off |
| 2.8c | **Test the failover monthly.** Switch the Osee to the emergency input, listen, switch back. |

### Then — fix the broadcast bus content

**Bus 7 currently has no drums.** Channels 1–7 (Kick, Snare, HH, Rack 1, Rack 2,
Floor, OHs) send to Bus 8 (DRUMS) and Bus 14 (Inst Verb), but **not** to Bus 7. If
you unmute Bus 7 as it stands, the online mix will have no drum kit at all.

| Step | Action |
|---|---|
| 2.6 | Add drum sends to Bus 7, **post-fader**, at the broadcast offsets from `07-broadcast-mix.md`: Kick **+3 dB** relative to house, Snare **+2**, Toms **+2**, **Overheads +4**, HH +1 |
| 2.7 | Move the **crowd mics (ch 29, 30) into Bus 7** instead of direct to MTX5, so their level rides with the rest of the broadcast mix. Link them as a stereo pair. Sit them **12–18 dB under the music**. |
| 2.8 | Verify **nothing that should not be public** reaches Bus 7 — check ch 33 (Kids Lapel, currently sending −10 dB) and the talkback channels |

### Finally — lip-sync

| Step | Action |
|---|---|
| 2.9 | Run the clap test in `11-osee-video-integration.md` |
| 2.10 | Enable delay on **Matrix 5** and enter the measured value. Record it in this repo. |

---

## Stage 3 — Aux-fed subwoofers (45 min)

Currently Matrix 4 SUBS is fed the whole house mix. This is the biggest available
improvement to the sound in the room.

| Step | Action |
|---|---|
| 3.1 | Choose a free bus for the sub feed. **Bus 11** is free (unnamed, at −∞). Name it `SUB FEED`, set it **mono**. |
| 3.2 | **Turn off `Main 1 → MX4`.** |
| 3.3 | Feed Matrix 4 from **Bus 11** at 0 dB. |
| 3.4 | Add **post-fader** sends to Bus 11 from these channels only: |

| Channel | Send level |
|---|---|
| Ch 1 Kick | −3 dB |
| Ch 6 Floor | −8 dB |
| Ch 8 Bass | **0 dB** |
| Ch 11 Keys 1 | −12 dB (only if the patch carries real low end) |
| Ch 12 Keys 2 | −12 dB (same condition) |
| Ch 17/18 Track/Loop | −6 dB |
| **Everything else** | **nothing** |

| Step | Action |
|---|---|
| 3.5 | Check Matrix 4's LPF is set to your crossover point (90 Hz, 24 dB/oct is a good default) and add a 30 Hz HPF at 24 dB/oct for infrasonic protection |
| 3.6 | Run the sub/main alignment procedure in `06-house-mix.md` and set Matrix 4's delay |

Do this with pink noise and a measurement mic if you have one, and with a familiar
song if you do not. The difference will be obvious either way.

---

## Stage 4 — Operating structure (60 min)

### 4.1 Mute groups

| MG | Name | Members |
|---|---|---|
| 1 | **BAND** | Ch 1–12, 17, 18 |
| 2 | **VOX** | Ch 13–16, 20, 22, 25, 26, 27 |
| 3 | **SPEECH** | Ch 21, 23, 24, 33 |
| 4 | **MEDIA** | Ch 34 |
| **6** | **CROWD** | **Ch 29, 30** |

**Mute group 6 is the one that matters most.** One button, before every altar call,
every private prayer, every pastoral moment. See `07-broadcast-mix.md`.

### 4.2 Add a SPEECH DCA

| DCA | Name | Members |
|---|---|---|
| **10** | **SPEECH** | Ch 21 (Pastor Lapel), 23 (House), 24 (Wireless 3), 27 (Wireless 4), 33 (Kids Lapel) |
| 11 | CROWD | Ch 29, 30 |
| 12 | Repurpose from "DELAY" (unused, at −∞) or clear it | |

During the sermon, DCA 10 up and DCA 9 (BAND) down should be the whole job.

### 4.3 Automix

| Step | Action |
|---|---|
| 4.3.1 | Enable **Automix group X** |
| 4.3.2 | Add: ch 21 Pastor Lapel (weight **0 dB**), ch 23 House, ch 24 Wireless 3, ch 27 Wireless 4, ch 33 Kids Lapel (all 0 dB) |
| 4.3.3 | **Do not** add sung vocals (ch 13–16, 20, 22, 25, 26) — automix attenuates whatever is not loudest, which is exactly wrong for music |
| 4.3.4 | Test with two mics open and two people talking. The unused mic should duck audibly. |

### 4.4 Talkback

| Step | Action |
|---|---|
| 4.4.1 | Talkback is assigned to CH40 with **no destinations**. Enable destinations: **Bus 1 (STAGE MON), Bus 8 (DRUMS), Bus 9 (WL BUS P16)** |
| 4.4.2 | Confirm talkback is **not** enabled to any Main or to MX5. Test it by talking while watching the Main 1 and Matrix 5 meters. |

---

## Stage 5 — Virtual soundcheck (30 min)

The USB ports are already named for this. Finish it.

| Step | Action |
|---|---|
| 5.1 | Clear the stray alt source on **ch 12** (currently pointing at A-14, which is wrong) |
| 5.2 | For each channel 1–40, set **Alt Source = the matching USB return**. The USB input names already tell you the intended mapping. |
| 5.3 | Leave the **Main Source** as the live AES50-A / LCL input |
| 5.4 | Test: pull the Matrix 1/2/3 faders down (or power the amps off), flip **Alt Source** on, play last Sunday's recording from Logic, confirm the console responds exactly as it did live |
| 5.5 | **Flip back to Main Source.** Put a label on the console. An Alt Source left on for a Sunday means total silence and a panicking operator. |

Once this works, `10-logic-pro.md` explains how to use it for training. It is the
highest-return thing in this whole plan for building a volunteer team.

---

## Stage 6 — Tuning refinements (as time allows)

Judgement calls, not errors. Do them with material playing, one at a time, A/B'ing
each change.

| Step | Action |
|---|---|
| 6.1 | **Kick gate release** 400 ms → try **200 ms**. Listen for the gate hanging open on fast passages. |
| 6.2 | **Kick EQ** — currently −14.7 dB @ 295 Hz and −15.0 dB @ 900 Hz. Try easing both to −8 dB and compare. You may prefer the original; the point is to have chosen it deliberately. |
| 6.3 | **Speech compressor attack** on ch 21 (Pastor Lapel): 30 ms → **8 ms**. Speech holds more consistently with a faster attack. Leave the sung vocals at 30 ms. |
| 6.4 | **Ch 2 Snare LPF** is at 20 kHz (on, doing nothing). Set to ~12 kHz or switch it off. |
| 6.5 | **Ch 8 Bass** — consider moving the 76LA from the gate slot to the dynamics slot so the next operator finds it where they expect |
| 6.6 | **Unmute or remove** Bus 13 (Choir), Bus 14 (Inst Verb), Bus 16 (Slap). Instrument reverb and slap are currently loaded and silent. Decide which you want and delete the rest. |
| 6.7 | **Resolve the duplicate FX returns.** Buses 14/15 feed Main 1 directly *and* Aux 1–4 return the same effects. Pick one path, zero the other. |
| 6.8 | **WING-LIVE SD** is set to 32 tracks; you are using 40 channels. Either accept the 32 most important, or check whether your firmware and card support more. |

---

## Verification checklist

Work through this before declaring the remediation complete.

- [ ] Show file backed up before **and** after, to USB and the server
- [ ] Scene safes set, and **tested** by deliberately recalling over changed values
- [ ] Bus 7 BROADCAST unmuted and carrying drums
- [ ] Matrix 5 STREAM patched to a real output
- [ ] Stream verified on headphones **and** on a phone speaker
- [ ] Click / cue / talkback content confirmed absent from Matrix 5 — solo it and listen
- [ ] Crowd mics reaching the stream, absent from Main 1
- [ ] Mute group 6 (CROWD) tested
- [ ] Subs aux-fed; speech no longer rumbles the room
- [ ] Speech DCA in place and reachable without changing layers
- [ ] Automix ducking verified with two open mics
- [ ] Talkback reaching the stage and **not** the mains or the stream
- [ ] Virtual soundcheck tested and switched back to Main Source
- [ ] Lip-sync measured and applied
- [ ] Every live channel named on the surface
- [ ] New show file exported and committed to this repository

---

## Suggested sequence

| Session | Stages | Time |
|---|---|---|
| Mid-week 1 | Stage 0 + Stage 1 | ~1 hour |
| Mid-week 2 | Stage 2 (once C4 is answered) | ~1 hour |
| Mid-week 3 | Stage 3 | ~1 hour |
| Mid-week 4 | Stage 4 + Stage 5 | ~1.5 hours |
| Ongoing | Stage 6, one item at a time | — |

Stage 1 alone is worth doing tonight.
