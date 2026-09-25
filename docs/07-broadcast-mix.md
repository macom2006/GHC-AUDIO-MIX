# 07 — Broadcast Mix (Online)

The online mix is not a copy of the house mix. It is a separate product, built on
**Main 2**, for a listener wearing earbuds on a phone in a noisy kitchen.

## Who you are actually mixing for

| Where they listen | Share (typical) | What it means for the mix |
|---|---|---|
| Phone speaker | ~40% | No bass below 300 Hz at all. Midrange is everything. |
| Earbuds / headphones | ~30% | Stereo width and reverb read clearly. Sibilance is punishing. |
| Laptop speakers | ~20% | Thin, boxy, 400–800 Hz heavy. |
| TV / soundbar | ~10% | Closest to a real system. |

**Design the mix for the phone speaker and check it on headphones.** If it works on
both, it works everywhere.

---

## Loudness targets

| Metric | Target | Why |
|---|---|---|
| **Integrated loudness** | **−16 LUFS** | The standard for streaming platforms and podcast delivery |
| **True peak** | **−1.5 dBTP** | Leaves headroom for lossy encoding artifacts |
| Short-term range | −18 to −14 LUFS | Consistent enough that nobody reaches for the volume |
| Speech loudness | −16 LUFS, no quieter | Speech should be **as loud as the music**, not quieter |
| Loudness range (LRA) | 6–9 LU | Wider sounds amateur; narrower sounds lifeless |

> **The most common church stream failure is speech being 6–10 dB quieter than
> worship.** Viewers turn the volume up for the sermon, then get blasted by the
> closing song and leave. Match them.

Measure with a LUFS meter — either a plugin on the Logic Pro monitor path or a
metering insert on Main 2. Do not guess.

---

## Main 2 offsets from the house mix

Start from the house mix using Sends on Fader, then apply these:

| Group | Offset | Reason |
|---|---|---|
| **Kick (ch 1–2)** | **+3 dB** | No acoustic kick in the room online |
| **Snare (ch 3)** | **+2 dB** | Same |
| Toms (ch 6–8) | +2 dB | Same |
| **Overheads (ch 9–10)** | **+4 dB** | Online, the overheads *are* the drum kit |
| Hi-hat (ch 5) | +1 dB | |
| Bass DI (ch 13) | +1 dB, more 800 Hz | Phone speakers have no fundamental |
| Electric guitars | 0 dB, pan wider (50%) | Stereo width reads well on headphones |
| Acoustic guitars | +1 dB | |
| Keys / pads | −1 dB | Pads clutter a small speaker |
| **Worship leader (ch 25)** | **+2 dB** | Must be unambiguously the lead |
| BGVs | 0 dB | |
| **Speech (ch 33–40)** | **+3 dB** | Intimacy; the viewer has no room reinforcement |
| Tracks | −1 dB | |
| **Ambience (ch 41–42)** | **Present, 12–18 dB under the music** | The difference between "live church" and "rehearsal room" |
| FX returns | +3 dB | The room's natural reverb is missing online |

Store these offsets in the scene so they recall every week.

---

## Main 2 mastering chain

Process in this order:

```
Main 2 ──► HPF ──► EQ ──► Multiband/Bus Comp ──► De-ess ──► Limiter ──► Matrix 6
```

### 1. High-pass filter
**40 Hz, 24 dB/oct.** Removes energy that no viewer's device can reproduce and that
only wastes encoder bitrate.

### 2. Broadcast EQ (Main 2 bus EQ)

| Band | Frequency | Gain | Q | Purpose |
|---|---|---|---|---|
| 1 | 80 Hz | −2 dB | 1.0 | Tighten — the room isn't there to absorb it |
| 2 | 300 Hz | −3 dB | 1.5 | **The single most important cut.** Removes the "boxy laptop" sound |
| 3 | 1.2 kHz | +1.5 dB | 1.2 | Presence for small speakers |
| 4 | 3.5 kHz | +2 dB | 1.5 | Intelligibility |
| 5 | 8 kHz | +1.5 dB | shelf | Air, sparkle on headphones |
| 6 | 16 kHz | −2 dB | shelf | Reduce encoder artifacts |

### 3. Bus compression
| Parameter | Value |
|---|---|
| Threshold | −18 dB |
| Ratio | **2.5:1** |
| Attack | 30 ms |
| Release | Auto, or 200 ms |
| Knee | Soft |
| Target reduction | **3–5 dB on peaks** — visible movement, not pumping |
| Makeup | To restore level |

Glue, not squash. If the gain reduction meter is pinned, back off.

### 4. De-esser
7 kHz, threshold for 3–4 dB reduction on the loudest sibilance. Earbuds make
sibilance painful in a way a PA never does.

### 5. True-peak limiter (last in the chain)
| Parameter | Value |
|---|---|
| Ceiling | **−1.5 dBTP** |
| Lookahead | On |
| Release | Auto |
| Target reduction | 1–3 dB on peaks |

This limiter is a **safety net**, not a loudness tool. If it is working constantly,
Main 2 is running too hot — pull the master down and let the limiter idle.

---

## Ambience mic technique

This is the skill that separates a good church stream from a great one.

| Moment | Ambience level | Effect |
|---|---|---|
| Pre-service | −18 dB under music | Room feels alive, people are arriving |
| Worship — verse | −18 dB | Subtle |
| **Worship — chorus, congregation singing** | **−10 to −12 dB** | The viewer hears the church singing. This is the moment. |
| Sermon | **−24 dB or muted** | Avoid coughs, crying babies, side conversations |
| Sermon — congregation responds ("Amen") | Push to −15 dB briefly | Carries the room's energy |
| Prayer / altar call | **MUTED (Mute Group 6)** | Privacy. Non-negotiable. |
| Post-service | −15 dB | Warmth as people leave |

**The privacy rule:** if someone is praying at the altar, weeping, or receiving
counsel, the ambience mics are muted. A live stream is a permanent public record. A
pastoral moment broadcast without consent is a breach of trust, and no amount of
production value is worth it. Build the reflex: **altar call = MG6 in.**

---

## Reverb for broadcast

The house gets very little reverb because the room supplies its own. The stream gets
none of that, so it needs help.

| Source | House send | Broadcast send |
|---|---|---|
| Worship leader | −12 dB (Hall) | **−9 dB** |
| BGVs | −10 dB (Plate) | −8 dB |
| Snare | −10 dB (Drum Room) | −8 dB |
| **Speech** | **OFF** | **−24 dB short room only** |

That tiny amount of room on the speech matters. Completely dry speech sounds like a
voiceover recorded in a closet, not a pastor standing in a church. But keep it
short — under 0.8 s decay — or intelligibility suffers.

---

## Broadcast QC checklist

Run this every week. It takes four minutes.

- [ ] Main 2 metering active, integrated loudness reading near −16 LUFS
- [ ] True peak never exceeding −1.5 dBTP
- [ ] **Listen on actual earbuds**, not studio monitors, not the console headphone amp
- [ ] **Listen on a phone speaker** — the worst case, and the most common one
- [ ] Click (ch 32) and cues (ch 24) confirmed absent — solo Main 2 and listen
- [ ] Speech and music at matched loudness — A/B a sermon clip against a chorus
- [ ] Ambience present but not distracting
- [ ] No clipping anywhere in the chain
- [ ] Lip-sync verified against the video — see doc 11
- [ ] Confidence monitor (Aux 6) returning the actual stream, and someone listening to it

## Broadcast mix failures and fixes

| Symptom | Cause | Fix |
|---|---|---|
| Stream sounds thin and lifeless | House mix pushed to Main 2 unchanged | Apply the offsets above; add ambience |
| Sermon too quiet vs worship | No loudness matching | Push speech +3 dB; verify with the LUFS meter |
| Muddy, boxy, "laptop speaker" sound | 300 Hz buildup | The −3 dB at 300 Hz on Main 2 |
| Harsh, sibilant on earbuds | No de-esser | Add it at 7 kHz |
| Distorted at loud moments | Limiter ceiling too high, or Main 2 overdriven | Ceiling to −1.5 dBTP; pull the master |
| Congregation inaudible | No ambience mics, or they are too low | That is what channels 41–42 are for |
| Audio and video out of sync | No delay compensation | Doc 11 |
| Click track audible online | Ch 32 assigned to a main | Unassign and **lock** it. Then check ch 24. |
