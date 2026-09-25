# 11 — Osee Video Switcher Integration

Getting the broadcast mix into the video chain, at the right level, in sync.

## Recommendation

**Option A — analog feed into the Osee.** Take Matrix 6 (broadcast) out of the WING
as a balanced analog pair, into the Osee's line input, and let the switcher embed
and stream it.

**Why:** one path, no computer in the audio chain, no clock domain to drift, and if
the streaming computer dies the audio path is unaffected. It is the most reliable
configuration for a volunteer-operated system, which is what matters most.

Option B (below) is the upgrade path once the team is ready for it.

---

## Option A — Analog into the switcher

### Wiring

```
WING Local Out 5 (Matrix 6 L) ──┐
                                 ├──► [pad if needed] ──► Osee audio input
WING Local Out 6 (Matrix 6 R) ──┘
```

### Level matching — the step everyone gets wrong

The WING's outputs are **professional line level (+4 dBu, balanced)**. Most compact
streaming switchers have **consumer line inputs (−10 dBV, unbalanced)** on 3.5 mm or
RCA connectors. That is roughly a **12 dB mismatch**, and connecting them directly
gives you a distorted, crunchy stream that no amount of console EQ will fix.

Fix it in one of these ways, in order of preference:

1. **Reduce the WING's output trim.** Set the Matrix 6 output level to **−12 dB** in
   the console's output patch page. Free, clean, reversible.
2. **Inline attenuator pad** (−15 or −20 dB, XLR to 3.5 mm). A few dollars,
   completely reliable.
3. **Passive DI in reverse** (XLR line out → DI → unbalanced out). Works, but adds a
   box.

**Never** just turn the switcher's input gain all the way down — you will be
attenuating an already-clipped signal.

### Setting the level correctly

1. Play typical worship material at typical service level through Main 2.
2. Watch the Osee's audio meters.
3. Adjust the WING's Matrix 6 output trim until the switcher's meters read around
   **−12 dB average** with peaks touching **−6 dB**.
4. Then have the loudest possible moment happen (full band, congregation singing) and
   confirm nothing clips.
5. **Write the trim value here:** `_____ dB`
6. Once set, **do not touch it again.** Mix level changes happen on the Main 2 fader,
   not on the output trim.

### Switcher-side audio settings

| Setting | Value |
|---|---|
| Input type | **Line** (not mic — mic level will destroy the signal) |
| Input gain | Unity / 0 dB |
| Switcher EQ | **Off / flat** — all processing lives on the console |
| Switcher compressor / AGC | **OFF** | 
| Switcher limiter | On, as a safety net only |
| Audio follow video | **OFF** — the audio must never change when the camera cuts |
| Audio source | The line input only; disable any camera embedded audio |

> **"Audio follow video" is the single most damaging setting in a church video
> switcher.** If it is on, cutting from camera 1 to camera 2 changes or drops the
> audio mid-sentence. Turn it off and verify it is off.

> Mute or unassign every camera's embedded audio at the switcher. A camera's onboard
> microphone finding its way into the programme mix produces a hollow, echoing sound
> that is very hard to diagnose.

---

## Option B — USB into a computer running OBS

For when the team is ready for more control: graphics, multiple scenes, separate
recording and streaming, per-platform loudness.

```
WING USB (channels 1-2 = Main 2) ──► Mac ──► OBS ──► stream
Osee HDMI program out ──────────────► capture device ──► OBS (video only)
```

| Setting | Value |
|---|---|
| OBS audio device | WING USB, channels 1–2 |
| OBS sample rate | **48 kHz** |
| OBS channels | Stereo |
| Video capture | Osee program out, audio **disabled** on the capture device |
| Audio sync offset | Set in OBS "Advanced Audio Properties" — see the measurement below |
| Monitoring | Route OBS monitor back to WING Aux 6 for confidence |

**Advantage:** the sync offset lives in OBS, per-source, and can be positive or
negative. **Disadvantage:** a computer is now in the critical path.

---

## Lip-sync — measuring and fixing

Video processing always takes longer than audio processing. The switcher, the
cameras, the encoder and the scaler each add delay. Audio therefore arrives
**early**, and we fix it by **delaying the audio** to match the video.

### The clap test

1. Stand in front of a camera, in shot, with a microphone open.
2. **Clap sharply**, hands clearly visible, 5–10 times with gaps between.
3. Record the program output (or the actual stream).
4. Open the recording in Logic Pro.
5. Zoom in on one clap. Measure the gap between the **video frame where the hands
   meet** and the **audio transient**.
6. That gap, in milliseconds, is your required audio delay.

**Conversions:** 1 frame @ 30 fps = 33.3 ms · 1 frame @ 25 fps = 40 ms ·
1 frame @ 60 fps = 16.7 ms

### Applying the delay

| Path | Where to apply |
|---|---|
| Option A (analog to Osee) | **WING Matrix 6 delay** |
| Option B (USB to OBS) | **OBS sync offset** on the audio source |

**Measured offset:** `_____ ms`  ·  **Date measured:** `__________`  ·  **By:** `__________`

### Re-measure whenever

- The switcher firmware is updated
- A camera is added, replaced or reconfigured
- The streaming resolution or encoder settings change
- Anyone reports that lips look wrong

Lip-sync drift is the thing viewers notice fastest and complain about least — they
simply find it uncomfortable and stop watching.

### Tolerance

| Offset | Perception |
|---|---|
| Audio up to 40 ms **late** | Undetectable — this is natural (sound travels slower than light) |
| Audio 40–100 ms late | Noticeable to attentive viewers |
| Audio **early** by more than 20 ms | Immediately wrong-looking; the brain never accepts it |

**Always err on the side of audio slightly late.** We are used to that in the real
world; we are never used to hearing a word before the mouth moves.

---

## Confidence monitoring

Return the actual stream audio to the console on **Aux 6** so someone can hear what
the viewer hears — not what the console thinks it is sending.

Options, in order of usefulness:
1. A dedicated phone or tablet watching the live stream, its headphone output into
   Aux 6. This catches **everything**, including encoder problems.
2. The Osee's monitor output back into Aux 6. Catches switcher problems, not encoder
   problems.
3. Nothing. This is what most churches do, and it is why streams run for forty
   minutes with silent or distorted audio before anyone notices.

**Assign a person, every service, to listen to the stream on headphones for the
first five minutes and then spot-check every fifteen.** This is a role, not an
afterthought.

---

## Commissioning checklist for the video chain

- [ ] Sample rate 48 kHz confirmed everywhere in the chain
- [ ] Matrix 6 output trim set and written down
- [ ] Osee input set to **line**, not mic
- [ ] Switcher EQ / compressor / AGC **off**
- [ ] **Audio follow video OFF** — verified by cutting cameras during a talk
- [ ] Camera embedded audio muted or unassigned
- [ ] Clap test performed, delay measured and applied
- [ ] Confidence monitor working and assigned to a person
- [ ] Full-volume test: loudest worship moment does not clip the switcher
- [ ] Failure test: unplug the streaming computer — house PA must be unaffected
