# 03 — Input & Output Patch

This is the physical wiring standard. Every cable, every connector, every channel.
Machine-readable versions: [`../patch/input-patch.csv`](../patch/input-patch.csv),
[`../patch/output-patch.csv`](../patch/output-patch.csv).

**Label everything.** Every XLR at the stage box, every sub-snake tail, every IEM
pack. A patch that only exists in someone's head is a patch that fails on the one
Sunday that person is away.

---

## Input patch

### Stage box — S32 on AES50-A (console channels 1–32)

| Ch | Source | Input type | Phantom | Mic / DI |
|---|---|---|---|---|
| 1 | Kick In | Mic | No | Dynamic (inside drum) |
| 2 | Kick Out | Mic | No | Dynamic / sub-kick (outside head) |
| 3 | Snare Top | Mic | No | Dynamic |
| 4 | Snare Bottom | Mic | No | Dynamic — **polarity inverted** |
| 5 | Hi-Hat | Mic | Yes | Small-diaphragm condenser |
| 6 | Rack Tom 1 | Mic | No | Dynamic / clip-on |
| 7 | Rack Tom 2 | Mic | No | Dynamic / clip-on |
| 8 | Floor Tom | Mic | No | Dynamic / clip-on |
| 9 | Overhead L | Mic | Yes | Small-diaphragm condenser |
| 10 | Overhead R | Mic | Yes | Small-diaphragm condenser |
| 11 | Percussion / Cajon | Mic | Yes | Condenser |
| 12 | Drum spare | Mic | — | Ride / second snare / guest |
| 13 | Bass DI | DI | As required | Active DI from bass rig |
| 14 | Bass Amp Mic | Mic | No | Dynamic on cabinet |
| 15 | Electric Guitar 1 | Mic / DI | No | Dynamic on cab, or modeler DI |
| 16 | Electric Guitar 2 | Mic / DI | No | Dynamic on cab, or modeler DI |
| 17 | Acoustic Guitar 1 | DI | As required | Active DI |
| 18 | Acoustic Guitar 2 | DI | As required | Active DI |
| 19 | Keys L | DI | No | Stereo DI, left |
| 20 | Keys R | DI | No | Stereo DI, right |
| 21 | Pads / Aux Keys L | DI | No | Second keyboard / pad rig |
| 22 | Pads / Aux Keys R | DI | No | |
| 23 | Organ / Aux Instrument | DI | No | Mono — repatch as needed |
| 24 | Cues / Guide | Line | No | **Monitors only — never to any main** |
| 25 | Worship Leader Vox | Mic | Yes if wired | Wireless rx at stage or handheld |
| 26 | BGV 1 | Mic | Yes | |
| 27 | BGV 2 | Mic | Yes | |
| 28 | BGV 3 | Mic | Yes | |
| 29 | Vocal spare | Mic | Yes | Guest singer / 4th BGV |
| 30 | Tracks L | Line | No | Playback rig (Ableton / MultiTracks) |
| 31 | Tracks R | Line | No | |
| 32 | Click | Line | No | **Monitors only — never to any main** |

### Console local mic inputs 1–8 (console channels 33–40)

Wireless receivers live in the FOH rack, so they patch locally. Shortest path,
fewest failure points.

| Ch | Local in | Source | Phantom | Notes |
|---|---|---|---|---|
| 33 | 1 | **Pastor Headset** | As required | Primary speech channel. Highest priority on the desk. |
| 34 | 2 | Pastor Lav (backup) | As required | Live and gain-set every service, muted until needed |
| 35 | 3 | Handheld 1 | No | Worship leader / MC |
| 36 | 4 | Handheld 2 | No | Second speaker / guest |
| 37 | 5 | Lectern / Pulpit | Yes | Gooseneck condenser |
| 38 | 6 | Guest / Interview | No | Wireless or wired |
| 39 | 7 | Kids / Announcements | No | |
| 40 | 8 | Speech spare | — | Held for guest speakers |

### FOH rack box — SD16 on AES50-B (console channels 41–48)

| Ch | Input | Source | Phantom | Notes |
|---|---|---|---|---|
| 41 | 1 | **Ambience L** | Yes | SDC over congregation, left. **Broadcast + record only.** |
| 42 | 2 | **Ambience R** | Yes | SDC over congregation, right. **Broadcast + record only.** |
| 43 | 3 | Choir L | Yes | Choir / platform area mic |
| 44 | 4 | Choir R | Yes | |
| 45 | 5 | Media / Video L | Line | Audio from video playback |
| 46 | 6 | Media / Video R | Line | |
| 47 | 7 | Spare | — | |
| 48 | 8 | Spare | — | |

### Aux channels (WING AUX 1–8)

| Aux | Source | Purpose |
|---|---|---|
| 1–2 | USB return from Logic Pro | Walk-in music, virtual soundcheck playback |
| 3–4 | Bluetooth / 3.5 mm at FOH | Emergency playback, phone audio |
| 5 | Talkback mic at FOH | FOH → stage IEMs (Bus 1–8), **never to mains** |
| 6 | Osee stream return | Confidence monitor — listen to what the viewer hears |
| 7–8 | Spare | |

---

## Output patch

### Stage box S32 — outputs 1–16 (stage)

| Out | Destination | Source | Notes |
|---|---|---|---|
| 1–2 | IEM 1 — Worship Leader | Bus 1 L/R | |
| 3–4 | IEM 2 — BGVs | Bus 2 L/R | Shared mix for BGV 1–3 |
| 5–6 | IEM 3 — Keys | Bus 3 L/R | |
| 7–8 | IEM 4 — Bass | Bus 4 L/R | |
| 9–10 | IEM 5 — Electric Guitar | Bus 5 L/R | |
| 11–12 | IEM 6 — Drums | Bus 6 L/R | |
| 13 | Wedge 1 — Pulpit | Bus 9 | Mono, speech-focused |
| 14 | Wedge 2 — Stage / drum fill | Bus 10 | Mono |
| 15–16 | Spare (IEM 7/8) | Bus 7 L/R | Buses programmed, outputs free |

### Console local line outputs 1–8 (FOH)

| Out | Destination | Source | Level |
|---|---|---|---|
| 1 | Main PA Left | Matrix 1 L | +4 dBu |
| 2 | Main PA Right | Matrix 1 R | +4 dBu |
| 3 | Subwoofers | Matrix 2 (mono) | +4 dBu |
| 4 | Front fills | Matrix 3 (mono) | +4 dBu |
| 5 | **Broadcast L → Osee** | Matrix 6 L | See doc 11 for level |
| 6 | **Broadcast R → Osee** | Matrix 6 R | See doc 11 for level |
| 7 | Lobby / overflow | Matrix 4 (mono) | +4 dBu |
| 8 | Hearing assist transmitter | Matrix 7 (mono) | +4 dBu |

### FOH SD16 — outputs 1–8

| Out | Destination | Source |
|---|---|---|
| 1 | Nursery / cry room | Matrix 5 |
| 2 | Green room | Matrix 8 |
| 3–4 | Spare zone L/R | — |
| 5–6 | Backup broadcast feed (analog) | Matrix 6 L/R |
| 7–8 | Spare | — |

### Digital outputs

| Port | Carries | Destination |
|---|---|---|
| AES/EBU out | Matrix 6 (broadcast, stereo) | Osee or stream encoder, if it accepts AES |
| USB-B (48 ch) | All 48 channels, direct out | Logic Pro multitrack |
| USB-B returns 1–2 | Logic Pro output | Aux 1–2 (virtual soundcheck) |
| WING-LIVE SD card | All 48 channels | Independent backup recording |

---

## Patching rules

1. **Channel 24 (Cues) and channel 32 (Click) are never assigned to Main 1, Main 2,
   Main 3 or Main 4.** Unassign them at the channel and then **lock the channel**.
   A click track leaking into the stream is the single most common church broadcast
   embarrassment.
2. **Channels 41–42 (Ambience) are never assigned to Main 1.** Ambience in the house
   PA is a microphone pointed at a loudspeaker. It is a feedback loop.
3. **Talkback (Aux 5) goes to Bus 1–8 only.** Never to a main, never to a matrix.
4. Phantom power is switched **off** before patching or unpatching any microphone.
   Switch the channel to mute first, then patch, then unmute.
5. Any spare channel that is not in use is **muted and its fader pulled to −∞**, not
   just left down. Muted and down.
