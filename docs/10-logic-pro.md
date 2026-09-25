# 10 — Logic Pro: Multitrack Recording & Virtual Soundcheck

Recording every service costs nothing once it is set up, and it pays for itself
three ways: **virtual soundcheck**, **content for media**, and **training**.

## Connection

| Setting | Value |
|---|---|
| Connection | WING USB-B → Mac (use a USB-B cable rated for data; not a charging cable) |
| Channel count | 48 in / 48 out |
| Sample rate | **48 kHz** — must match the console and the video chain |
| Bit depth | 24-bit |
| Clock | **WING is the master.** Logic slaves to it. |
| Driver | Class-compliant on macOS; no driver installation needed |

### Logic Pro audio preferences

| Setting | Value | Why |
|---|---|---|
| Output device | WING | |
| Input device | WING | |
| I/O Buffer Size | **256 samples** for recording | Stability over latency; we are not monitoring through Logic |
| Recording Delay | 0 | Leave alone unless a measured offset exists |
| Process Buffer Range | Large | Stability |
| ReWire behaviour | Off | |
| Sample Rate | 48 kHz | |

**Never monitor the band through Logic.** Monitoring happens on the console. Logic
is a tape machine, nothing more, during a service.

---

## Direct out tap point — the decision that makes or breaks virtual soundcheck

Set every channel's USB direct out to **post-preamp, pre-processing**.

| Tap point | Records | Good for virtual soundcheck? |
|---|---|---|
| **Post-preamp, pre-EQ** | Raw microphone signal | **Yes — use this** |
| Post-EQ | EQ'd signal | No — you cannot re-EQ what is already EQ'd |
| Post-fader | Mixed signal | No |

Recording raw means that when you play it back into the console, every EQ, gate,
compressor and fader responds exactly as it did with the live band in the room. That
is the whole point.

---

## Session template

Create a template file: `GHC-Service-Template.logicx`

### Track list

| Tracks | Input | Name |
|---|---|---|
| 1–12 | 1–12 | Drums (Kick In, Kick Out, Snr Top, Snr Bot, HiHat, Tom1, Tom2, Floor, OH L, OH R, Perc, Spare) |
| 13–14 | 13–14 | Bass DI, Bass Amp |
| 15–18 | 15–18 | EG1, EG2, AG1, AG2 |
| 19–23 | 19–23 | Keys L, Keys R, Pads L, Pads R, Organ |
| 24 | 24 | Cues |
| 25–29 | 25–29 | WL, BGV1, BGV2, BGV3, Vox Spare |
| 30–32 | 30–32 | Tracks L, Tracks R, Click |
| 33–40 | 33–40 | Pastor HS, Pastor Lav, HH1, HH2, Lectern, Guest, Kids, Spare |
| 41–48 | 41–48 | Amb L, Amb R, Choir L, Choir R, Media L, Media R, Spare, Spare |

Track names must match `patch/input-patch.csv` exactly. A stem named "Audio 27" is
useless to the media team six months later.

### Template settings
- All 48 tracks record-enabled
- Track colours matching the DCA colours in doc 05 (drums blue, vocals yellow,
  speech red, and so on)
- Project tempo irrelevant; recording is free-running
- **Save as a template**, not as a project you keep overwriting

---

## Weekly recording workflow

### Before the service
1. Open the template, **Save As**: `YYYY-MM-DD_GHC_Service.logicx`
2. Confirm the WING appears as the audio device
3. Confirm all 48 tracks are armed and showing signal
4. Check free disk space — **48 tracks × 24-bit × 48 kHz ≈ 415 MB per minute**.
   A two-hour service is roughly **50 GB**. Confirm you have at least 100 GB free.
5. Record-arm and hit record **fifteen minutes before** the service starts. Disk is
   cheaper than a missed sermon.

### During the service
- Do not touch Logic. Do not stop and restart between segments.
- Glance at the record timer every ten minutes to confirm it is still running.
- If Logic crashes, **do not panic** — the WING-LIVE SD card is recording the same
  48 channels independently.

### After the service
1. Stop recording. Save.
2. **Immediately** back up to the church NAS or external drive. Two copies, minimum.
3. Bounce a stereo reference mix from Main 2 for the media team.
4. Archive: `/Archive/YYYY/YYYY-MM-DD_GHC_Service/`

### Storage policy

| Age | What to keep |
|---|---|
| 0–8 weeks | Full 48-track session (for virtual soundcheck) |
| 2–12 months | Stems: drums bounce, bass, guitars, keys, vocals, speech, ambience |
| Permanent | Stereo mix of the sermon + stereo mix of worship |

Two months of full multitracks is about 400 GB. Budget for a 4 TB drive and rotate.

---

## Virtual soundcheck

This is the feature that makes a volunteer team competent. Mid-week, with an empty
room, you can rehearse the entire mix with last Sunday's band.

### Setup (once)

1. In the WING, set each channel's **Alt Source** to the corresponding **USB return
   channel** (Ch 1 → USB 1, Ch 2 → USB 2, and so on through 48).
2. Leave the **Main Source** as the live AES50/local input.
3. Confirm the global **Alt Source** switch toggles all channels at once.

> The exact naming of this feature varies slightly by firmware — look for the
> channel source page with "Main" and "Alt" source selectors, plus a global toggle.
> This is the standard WING virtual-soundcheck mechanism.

### Running a virtual soundcheck

1. Open last Sunday's Logic session.
2. Route Logic's outputs 1–48 to the WING's USB returns 1–48 (one-to-one).
3. **Mute the house PA** — Matrix 1 fader down, or power the amps down. You are
   about to play a full band into an empty room.
4. Flip the console to **Alt Source**.
5. Press play in Logic. The console now behaves exactly as it did on Sunday.
6. Mix. Experiment. Break things. Try the broadcast mix on headphones. Ring out a
   new microphone. Train a volunteer.
7. Save any improvements into the scene.
8. **Flip back to Main Source** when finished. Write this on a label and stick it to
   the console — an Alt Source left engaged on a Sunday morning means total silence
   and a panicking operator.

### What virtual soundcheck is for

| Use | Value |
|---|---|
| **Training volunteers** | A new operator can make every mistake with nobody listening |
| Testing changes | Try a new compressor setting against real material before Sunday |
| Building the broadcast mix | Refine the stream mix properly, on headphones, with time |
| Diagnosing complaints | "The vocals were buried last week" — play it back and find out |
| Ringing out mics | Set notches against real programme material |

**Use it every week.** A team that rehearses its mix mid-week sounds dramatically
better than one that only ever mixes live under pressure.

---

## Backup recording (WING-LIVE SD card)

| Setting | Value |
|---|---|
| Channels | All 48 |
| Tap point | Same as USB — post-preamp, pre-processing |
| Card | Use a card rated for sustained multitrack write (V30 / U3 minimum) |
| Format | Format **in the console**, not on a computer |
| Routine | Format before each service; copy off and archive after |

This recorder runs entirely independently of the computer. If the Mac crashes, dies,
or someone trips over its cable, the service is still captured. It has saved more
sermons than any other single feature on the desk.
