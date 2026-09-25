# 17 — The Logic Pro Broadcast Rig

**This document answers the open question from the console audit.** The broadcast
mix is not built on the WING. It is built in **Logic Pro**, in the session
`Live Stream Broadcast 03.15.26 – Broadcast Pastor`, and leaves the building
through a **Universal Audio Volt 276**.

That changes the architecture, and it resolves audit finding C4.

---

## Confirmed architecture

```
STAGE                    WING (GRACELAND)                 MAC / LOGIC PRO              VIDEO
─────                    ────────────────                 ───────────────              ─────

 32 ch ═══AES50-A═══►  ┌──────────────────┐
 8 ch  ═══Local═════►  │  40 channels     │
 4 ch  ═══AUX═══════►  │                  │
                       │  Main 1 ─► MTX1/2/3 ─► PA L/C/R
                       │          └─► MTX4 ──► SUBS
                       │                  │
                       │  USB out 1–44 ═══╪══════════►  INPUT DEVICE: WING
                       └──────────────────┘             (43 of 48 ports patched)
                                                                │
                                                        Broadcast mix session
                                                        Groups: Drums, Overheads,
                                                        Vocals, Crowds
                                                        Buses 3/5/7/9/41/51/53/55
                                                        Verb 1-3, Slap, Delay 3
                                                        → "Stream" output (limited)
                                                                │
                                                        OUTPUT DEVICE: Volt 276
                                                                │
                                                                └──► analog ──► OSEE ──► STREAM
```

**The WING's Bus 7 "BROADCAST" and Matrix 5 "STREAM" are therefore leftovers.** They
duplicate work that Logic is already doing. Do not delete them — repurpose them as
the failover path (see below).

---

## CRITICAL — two clock domains

From the Logic audio settings:

| Setting | Current value |
|---|---|
| **Input Device** | **WING** |
| **Output Device** | **Volt 276** |
| I/O Buffer Size | 256 samples |
| Resulting Latency | 14.3 ms roundtrip (5.9 ms output) |
| Recording Delay | 1 sample |
| Process Buffer Range | Medium |
| Multithreading | Playback & Live Tracks |
| Summing | High Precision (64-bit) |

**Input and output are two physically separate USB interfaces, each running its own
clock.** The WING is clocked internally at 48 kHz. The Volt 276 is clocked
independently at its own nominal 48 kHz. Two crystals never run at exactly the same
rate.

macOS builds an implicit aggregate device to bridge them. Over a 90-minute service,
the two rates diverge. What you get, in escalating order:

1. Occasional clicks and pops that "come and go"
2. Audio glitching under load that seems random
3. Slow, progressive lip-sync drift — fine at the start of the service, visibly
   wrong by the sermon
4. Dropouts, or Logic losing the device mid-service

If anyone has ever said "the stream sounded fine at the start and weird later," this
is the cause. It is not the encoder and it is not the network.

### Fix — use the WING for both input and output

The WING is a **48×48** interface. It can be the output device as well as the input
device. One device, one clock, no aggregate, no drift, and one fewer box in the
critical path.

| Step | Action |
|---|---|
| 1 | In Logic: `Settings → Audio → Devices`, set **Output Device = WING** |
| 2 | In Logic, set the **Stream** output object's outputs to **WING 1–2** (or any free USB return pair) |
| 3 | In the WING output patch, set **LCL out 5 ← USB.1** and **LCL out 6 ← USB.2** |
| 4 | Run those two local XLR outputs to the Osee, at line level, padded as needed (see `11-osee-video-integration.md`) |
| 5 | Keep the Volt 276 as a spare, or use it purely for headphone monitoring on a separate machine |

Do **not** insert the WING's Matrix 5 chain in this path — Logic already has a
limiter on the Stream bus, and double-processing will only cost headroom.

### If the Volt 276 must stay in the chain

Then make the clock explicit rather than implicit:

1. Open **Audio MIDI Setup** → create an **Aggregate Device**
2. Add both the WING and the Volt 276
3. Set the **WING as Clock Source (master)**
4. **Enable Drift Correction on the Volt 276** — this is the setting that matters
5. Point Logic at the aggregate for both input and output

This works, but it adds latency and an extra failure mode. The single-device
approach above is better, costs nothing, and uses gear you already own.

---

## HIGH — single point of failure

Right now, if the Mac crashes, the stream loses **all** audio. The house is fine
(it comes off Main 1 → Matrix 1/2/3), but the online congregation gets silence
until someone notices and improvises.

### Build the failover on the orphaned WING path

This is exactly what Bus 7 "BROADCAST" and Matrix 5 "STREAM" should be used for.
They already exist, they already have a mastering chain, and they are already
patched to nothing — so switching them on costs nothing and risks nothing.

| Step | Action |
|---|---|
| F1 | Unmute **Bus 7 BROADCAST** |
| F2 | Add the missing drum sends to Bus 7 — channels 1–7 currently do not feed it at all (see `16-remediation-plan.md` step 2.6) |
| F3 | Keep **Matrix 5 STREAM** fed from Bus 7 at 0 dB, with its existing Pulsar EQ / ECL33 / TAPE / LIMITER chain |
| F4 | Patch **Matrix 5 L/R → two spare outputs** wired to a **second input on the Osee** |
| F5 | Label that Osee input **"EMERGENCY AUDIO"** |
| F6 | Test it monthly. Switch the Osee to it, listen, switch back. |

Then the failure procedure is one button on the video switcher, not a scramble. Put
it in `14-troubleshooting.md` and teach it to every operator.

> This is the strongest argument for finishing the WING's broadcast path rather than
> deleting it. It is not a duplicate mix — it is your insurance policy.

---

## The USB map — and a mismatch to resolve

The authoritative mapping is in
[`../patch/wing-usb-to-logic-map.csv`](../patch/wing-usb-to-logic-map.csv), parsed
from the console file. Summary:

| | |
|---|---|
| USB outputs patched | **43 of 48** |
| Carrying real audio | **39** |
| Carrying junk | 4 — ports 43/44 (Bus 4 L, at −52 dB, same leg twice) and 47/48 (Main 4 L, muted) |
| Empty | 5 — ports 38, 41, 42, 45, 46 |

### What the WING actually sends

| Logic input | WING source | Connector label |
|---|---|---|
| 1 | A-1 | Kick |
| 2 | A-2 | Snare TOP |
| 3 | A-3 | SNARE BTTM *(channel is named "HH" — see audit M1)* |
| 4–6 | A-4, A-5, A-6 | Rack 1, Rack 2, Floor |
| 7–8 | A-7, A-8 | OHs L/R |
| 9 | A-9 | Bass |
| 10 | A-10 | E Gtr |
| 11–12 | A-11, A-12 | Keys 1 L/R |
| 13–14 | A-13, A-14 | Keys 2 L/R |
| 15 | A-15 | TRACK *(feeds channels named "Sax" and "LOOP")* |
| 16 | A-16 | ACOUSTIC |
| 17–20 | A-17 … A-20 | Martha, Elsie, Brenda, Raissa |
| 21–22 | A-25, A-26 | Pastor, Marie |
| 23–26 | LCL-3 … LCL-6 | Raissa, Peggy, Dehil, Gabriel |
| 27–30 | AUX-1 … AUX-4 | Jude, Brenda, Elsie, Martha |
| 31–32 | A-28, A-31 | House, David |
| 33 | LCL-1 | Kids Lapel |
| 34–37 | A-30, A-27, A-29, A-21 | Dehil, Gabby, Peggy, Jude |
| 39–40 | A-23, A-24 | Crowd 1, Crowd 2 |
| 38, 41, 42, 45, 46 | — | **empty** |
| 43, 44, 47, 48 | Bus 4 L / Main 4 L | **junk — clear these** |

### The mismatch

Your Logic session contains tracks named **Kick Out, Snare Up, Snare Up G, Snare
Down, Hi Hat, Loops, Drums 2, Bass Mic, Bass Synth, Classic Piano, EG 1L, EG 1R,
EG 2L, EG 2R, AG 1, AG 2, Keys 3L, Keys 3R, SPD L, SPD R, Extra 1–4, String 2** —
and **the WING is not sending most of those sources.** There is no kick-out mic, no
snare-down mic, no second electric guitar, no second acoustic, no third keyboard and
no SPD in the console's input list.

Two possible explanations, and you need to determine which:

1. **They are inactive leftovers** from a larger rig or another campus. Harmless,
   but they clutter the session and make it slower to navigate.
2. **The track input assignments have drifted** relative to what the WING sends. If
   that has happened, tracks are recording and mixing the wrong sources — for
   example Logic's "Kick Out" fed from A-2 (Snare Top).

**This is the first thing to check at the next mid-week session.** Open the Logic
mixer, put it in Input view, and compare each track's assigned input against the CSV
above. It is a twenty-minute job and it either confirms everything is fine or finds
a serious error.

---

## Logic settings to change

| Setting | Current | Change to | Why |
|---|---|---|---|
| **Output Device** | Volt 276 | **WING** | Single clock domain. This is the important one. |
| **Recording Delay** | 1 sample | **0** | 1 sample is 0.02 ms — meaningless, and it suggests someone was nudging it without measuring. Set it to zero unless you have measured an actual offset. |
| **Process Buffer Range** | Medium | **Large** | More stable under a heavy live mix session. You are not tracking through Logic, so the extra latency costs nothing. |
| I/O Buffer Size | 256 | **keep 256** | Correct for this role — stability over latency |
| Multithreading | Playback & Live Tracks | keep | Correct |
| Summing | 64-bit | keep | Correct |
| **Plugin Delay Compensation** | *not visible* | **All** | With verbs, limiters and bus processing, PDC must be set to All or the mix will be internally misaligned |

---

## Click and cue protection

The session contains **Keys Click, Drum Click, Drum Click and Cues** tracks. From the
screenshots their faders are at or near −∞, which is good practice but is **not
protection**. A fader can be nudged. A grouped fader can be nudged by accident from
another channel.

Make it structural:

| Step | Action |
|---|---|
| 1 | Set the output of every click and cue track to **No Output** |
| 2 | If they must stay routed for monitoring, send them to a dedicated bus that goes to **No Output**, never to the Stream bus |
| 3 | Colour them red and lock the tracks |
| 4 | Add it to the pre-service check: **solo the Stream bus and listen for click** |

One of your output strips already uses "No Out", so the mechanism is in use — apply
it consistently to all four.

---

## Loudness metering

I see a limiter on the Stream output, which is right, but **no loudness meter**. A
limiter tells you nothing about how loud the stream actually is to a viewer.

| Step | Action |
|---|---|
| 1 | Insert Logic's **Loudness Meter** on the **Stream** output object, after the limiter |
| 2 | Target **−16 LUFS integrated**, **−1.5 dBTP** true peak |
| 3 | Reset it at the start of each service and check it at the end |
| 4 | Check the sermon and a chorus against each other — they should read within about 1 LU |

Speech being quieter than worship is the most common church stream complaint, and it
is invisible without this meter. See `07-broadcast-mix.md`.

---

## Latency and lip-sync

Your broadcast audio path now has measurable delay:

| Stage | Latency |
|---|---|
| WING channel processing | ~0.8 ms |
| AES50 stage box | ~1.0 ms |
| USB to Logic + Logic buffer + output | **14.3 ms** (at 256 samples) |
| Plugin delay compensation | variable — depends on the limiter and verbs |
| **Total, mic to Osee** | **roughly 16–25 ms** |

Typical video processing through a switcher and encoder is **33–100 ms** (1–3 frames).
So your audio still arrives **ahead of** the video, and still needs delaying.

| Step | Action |
|---|---|
| 1 | Run the clap test in `11-osee-video-integration.md` |
| 2 | Apply the measured offset — either as a delay plugin on the Logic Stream bus, or on the Osee if it offers an audio offset |
| 3 | **Re-measure whenever the I/O buffer size changes.** Going from 256 to 128 samples changes the audio latency by ~6 ms and will shift your lip-sync. |
| 4 | Record the measured value here: `_____ ms`, measured `__________`, by `__________` |

---

## What is well built in this session

Worth saying plainly:

- **Groups are used properly** — Drums, Overheads, Vocals, Crowds, all active
- **The crowd mics are in the broadcast mix** (Crowd 1L/1R/2L/2R, on their own
  groups) — this is the thing most churches never do, and it is why your stream can
  sound like a live room
- **Reverb structure is real** — Verb 1, Verb 2, Verb 3, Slap Delay, Delay 3 as
  proper returns rather than inserts
- **Summing structure is sensible** — Band, Vocals, Extra feeding a master chain,
  with separate Master Burn / Master Aux / Stream outputs
- **Track naming matches the people** — Pastor, Marie, Raissa, Peggy, Dehil, Gabriel,
  Jude, Brenda, Elsie, Martha, House, David. Consistent with the console.
- **A limiter is on the Stream output**
- **Click and cue tracks are pulled to −∞**

This is a well-conceived broadcast session. The problems are the clock domain, the
lack of a failover, and the drift between the session's track list and what the
console is actually sending.

---

## Priority order

| # | Action | Time | Risk if ignored |
|---|---|---|---|
| 1 | **Output Device → WING** (single clock) | 10 min | Clicks, drift, mid-service dropouts |
| 2 | Verify every Logic track input against the USB map | 20 min | Wrong sources in the broadcast mix |
| 3 | Click/cue tracks → No Output | 10 min | Click on the stream |
| 4 | Loudness Meter on the Stream bus | 5 min | Sermon quieter than worship, invisibly |
| 5 | Build the WING failover path | 45 min | Mac dies, stream goes silent |
| 6 | Clear USB ports 43/44/47/48 | 5 min | Confusion, junk in the session |
| 7 | Measure and apply lip-sync delay | 20 min | Viewers find it uncomfortable and leave |
| 8 | Recording Delay → 0, Process Buffer → Large | 2 min | Minor stability |
