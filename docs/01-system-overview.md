# 01 — System Overview

## The one principle everything else serves

**The house mix and the broadcast mix are two different products for two different
audiences, and they must never be the same mix.**

The room has natural acoustic energy the microphones do not capture: the drum kit
bleeding acoustically off the stage, the congregation singing, the physical impact
of the subwoofers in your chest, the pastor's voice reinforced by the room itself.
Online, none of that exists. The viewer hears only what the console sends. A house
mix pushed straight to the stream is thin, drum-light, congregation-less and
speech-quiet — which is exactly what most churches sound like online.

So we build **two independent mixes from one set of inputs**:

| | House (in-room) | Broadcast (online) |
|---|---|---|
| Destination | Main 1 → PA | Main 2 → Osee / stream |
| Reference level | 88–92 dBA (music), 72–78 dBA (speech) | −16 LUFS integrated, −1.5 dBTP |
| Drums | Light — the kit is acoustically loud in the room | Full — kick, snare, toms, OH carry the whole groove |
| Bass | Subs carry it | Must be EQ'd for phone and laptop speakers |
| Congregation | Present naturally | Must be added via ambience mics |
| Speech | Intelligibility in a reverberant room | Intimacy, compression, broadcast EQ |
| Dynamics | Wide — let the music breathe | Controlled — viewers cannot ride a volume knob |

The WING is chosen for this job specifically because it has **four stereo main
buses**, and every input channel has an **independent send level and pan to each
main**. That means the broadcast mix is not a copy of the house mix with an EQ on
it — it is a genuinely separate fader mix, built from the same inputs, costing us
zero aux buses.

---

## Hardware inventory

> Fill in the serial numbers and firmware versions in the blank column during
> commissioning. This table is the asset register.

### Console and I/O

| Item | Model | Qty | Location | Notes | Serial / FW |
|---|---|---|---|---|---|
| Digital mixing console | Behringer WING | 1 | FOH | **40 mono input channels + 8 aux channels**, 16 stereo buses, 4 stereo mains, 8 stereo matrices, 16 DCAs, 16 FX slots | |
| Stage box | Behringer S32 (or DL32) | 1 | Stage left | 32 mic in / 16 line out, AES50-A | |
| Expansion card | WING-LIVE (SD multitrack) | 1 | Console slot | Backup recorder — see doc 10 | |
| DAW computer | Mac + Logic Pro | 1 | FOH | USB-B to WING, 48×48 @ 48 kHz | |
| Video switcher | Osee (streaming switcher) | 1 | Video position | Audio embed — see doc 11 | |

### Audio distribution

| Item | Purpose | Source | Notes |
|---|---|---|---|
| Main PA L/R | Congregation | Matrix 1 | Room EQ + delay live here, not on Main 1 |
| Subwoofers | Low frequency | Matrix 2 | **Aux-fed** from Bus 15 — see doc 06 |
| Front fills | Rows 1–3 | Matrix 3 | Delayed to mains |
| Lobby / overflow | Foyer | Matrix 4 | Speech-forward, −6 dB music |
| Nursery / cry room | Parents | Matrix 5 | Same feed as lobby, independent level |
| Broadcast feed | Osee switcher | Matrix 6 (from Main 2) | See doc 11 |
| Hearing assist | ADA compliance | Matrix 7 | Speech-forward, no FX |
| Green room | Pastor / next-up | Matrix 8 | Pre-service and service audio |

### Stage monitoring

| Item | Model | Qty | Assigned to | Bus |
|---|---|---|---|---|
| IEM transmitter | (fill in) | 8 | Band + WL | Bus 1–8 |
| Wedge | (fill in) | 2 | Pulpit, drums | Bus 9–10 |
| Talkback mic | (fill in) | 1 | FOH → stage | Aux ch |

---

## Design decisions — and why

**1. Aux-fed subwoofers.**
Only kick, floor tom, bass guitar, tracks and the low-end of keys go to the subs.
Vocals, guitars and cymbals do not. This single decision removes more mud from a
church PA than any amount of channel EQ. See `docs/06-house-mix.md`.

**2. Room EQ lives in the matrix, not on the main bus.**
Main 1 stays clean. The matrix carries the room correction, the delay, and the
limiter. This means the broadcast mix never inherits the room tuning, and swapping
a PA processor does not touch the mix.

**3. Ambience mics exist only for the stream.**
Two small-diaphragm condensers over the congregation, sent **only to Main 2** and
to the recording. They are never in the house PA — that is a feedback loop. They
are the difference between a stream that sounds like a live church and one that
sounds like a rehearsal room.

**4. Automix on speech only.**
The pastor's headset, handheld mics and lectern go into Automix group X. Whichever
mic is being spoken into stays up; the rest duck automatically. Gain-before-feedback
improves, open-mic hiss drops, and nobody has to ride four speech faders during a
panel discussion. Automix is never used on sung vocals or instruments.

**5. Scene recall is scoped, not global.**
Recalling a scene must never change preamp gain, never unmute the wrong thing and
never jump the house master. Safes and scope are defined in
`docs/12-scenes-snapshots.md`. A scene that surprises the operator is worse than no
scene at all.

**6. Everything records, every week.**
48 channels into Logic Pro, plus a backup to the WING-LIVE SD card. This gives us
virtual soundcheck (rehearse the mix mid-week with no band in the room), it gives
the media team clean stems for podcast and clips, and it gives the next operator a
way to learn without a live congregation in front of them.

---

## Standing levels — the numbers that do not change

| Parameter | Target | Ceiling |
|---|---|---|
| House music (A-weighted, slow, FOH position) | 88–92 dBA average | 98 dBA peak |
| House speech | 72–78 dBA average | 85 dBA peak |
| Channel input metering | −18 dBFS average | −10 dBFS peak |
| Main 1 (house) output | −12 dBFS average | −3 dBFS peak |
| Main 2 (broadcast) integrated loudness | −16 LUFS | −1.5 dBTP |
| Broadcast short-term range | −18 to −14 LUFS | |
| Logic Pro record level | −18 dBFS average | −6 dBFS peak |

These are the standard. An operator who is consistently outside them is not mixing
to taste — they are out of spec.
