# 05 — Buses, DCAs & Matrices

The console architecture. Program this **before** touching a single channel EQ —
everything else hangs off this structure.

## Main buses (4 stereo)

| Main | Name | Purpose | Processing |
|---|---|---|---|
| **1** | **HOUSE** | Everything the congregation hears | Clean. No EQ, no limiter. Correction lives in Matrix 1. |
| **2** | **BROADCAST** | Everything the online viewer hears | Full mastering chain — see doc 07 |
| 3 | ZONES | Source for lobby, nursery, green room | Speech-forward blend, music −6 dB |
| 4 | RECORD | Clean stereo reference recording | No limiting, no broadcast EQ |

Every input channel has an **independent send level and pan to each of these four
mains**. This is the architectural feature the whole design rests on.

### Setting up the broadcast mix without rebuilding it from scratch

1. Build the house mix on Main 1 as normal.
2. Select Main 2 and use **Sends on Fader**. The physical faders now show and
   control each channel's send to the broadcast mix.
3. Copy the house mix across as a starting point, then apply the broadcast offsets
   from doc 07.
4. Store it in the scene. From then on, the broadcast mix is a fader layer you can
   call up and adjust in seconds.

---

## Buses (16 stereo)

| Bus | Name | Type | Pre/Post | Destination |
|---|---|---|---|---|
| 1 | IEM WL | Stereo | **Pre-fader** | S32 out 1–2 |
| 2 | IEM BGV | Stereo | Pre-fader | S32 out 3–4 |
| 3 | IEM KEYS | Stereo | Pre-fader | S32 out 5–6 |
| 4 | IEM BASS | Stereo | Pre-fader | S32 out 7–8 |
| 5 | IEM EG | Stereo | Pre-fader | S32 out 9–10 |
| 6 | IEM DRUMS | Stereo | Pre-fader | S32 out 11–12 |
| 7 | IEM SPARE 1 | Stereo | Pre-fader | S32 out 15–16 |
| 8 | IEM SPARE 2 | Stereo | Pre-fader | — |
| 9 | WEDGE PULPIT | Mono | Pre-fader | S32 out 13 |
| 10 | WEDGE STAGE | Mono | Pre-fader | S32 out 14 |
| 11 | FX1 VOX HALL | Stereo | **Post-fader** | FX rack |
| 12 | FX2 VOX PLATE | Stereo | Post-fader | FX rack |
| 13 | FX3 VOX DELAY | Stereo | Post-fader | FX rack |
| 14 | FX4 DRUM ROOM | Stereo | Post-fader | FX rack |
| 15 | **SUB FEED** | Mono | **Post-fader** | Matrix 2 → subwoofers |
| 16 | UTILITY | Stereo | Post-fader | Spare / hearing assist source |

**Pre-fader vs post-fader — the rule that prevents disasters:**
- **Monitor buses are pre-fader.** If you pull a channel down at FOH, the musician's
  in-ear mix must not change. Their mix belongs to them.
- **FX and sub buses are post-fader.** When you pull a vocal down, its reverb comes
  down with it. When you pull the bass down, the sub content follows.

---

## DCAs (16)

DCAs are how you actually mix. Learn these and you can run the service from twelve
faders.

| DCA | Name | Members | Colour |
|---|---|---|---|
| **1** | **SPEECH** | Ch 33–40 | Red |
| **2** | **WSHP VOX** | Ch 25 | Yellow |
| 3 | BGV | Ch 26–29, 43–44 | Yellow |
| 4 | DRUMS | Ch 1–12 | Blue |
| 5 | BASS | Ch 13–14 | Blue |
| 6 | GUITARS | Ch 15–18 | Green |
| 7 | KEYS | Ch 19–23 | Green |
| 8 | TRACKS | Ch 30–31 | Purple |
| 9 | FX RETURNS | All FX returns | Cyan |
| 10 | AMBIENCE | Ch 41–42 | Orange |
| 11 | MEDIA | Ch 45–46 | Purple |
| 12 | **BAND (ALL)** | DCA 4, 5, 6, 7, 8 members | White |
| 13–16 | Spare | — | — |

**DCA 1 (SPEECH) and DCA 12 (BAND) are the two most important faders in the room.**
Sermon: DCA 1 up, DCA 12 down. Worship: DCA 12 up, DCA 1 down. Everything else is
detail.

### Custom layer (the layer the operator actually lives on)

Program a custom layer with exactly these, left to right:

```
1  DCA 1  SPEECH      5  DCA 5  BASS      9   DCA 9   FX RETURNS
2  DCA 2  WSHP VOX    6  DCA 6  GUITARS   10  DCA 10  AMBIENCE
3  DCA 3  BGV         7  DCA 7  KEYS      11  DCA 11  MEDIA
4  DCA 4  DRUMS       8  DCA 8  TRACKS    12  DCA 12  BAND (ALL)
```

A competent operator should be able to run an entire service without leaving this
layer. Channel layers are for soundcheck and for fixing problems.

---

## Mute groups

| MG | Name | Members | When used |
|---|---|---|---|
| 1 | **BAND** | Ch 1–23, 30–31 | Sermon, prayer, announcements |
| 2 | **VOX** | Ch 25–29, 43–44 | Sermon, instrumental moments |
| 3 | SPEECH | Ch 33–40 | During worship (leave the worship leader's handheld out of this) |
| 4 | MEDIA | Ch 45–46 | Default state — unmute only for video |
| 5 | ALL STAGE | Ch 1–32 | Emergency / between services |
| 6 | AMBIENCE | Ch 41–42 | Mute during confidential prayer |

**Mute group 6 matters more than it looks.** If someone prays a private, painful
prayer at the altar and the ambience mics broadcast it to the internet, that is a
pastoral failure caused by an audio decision. Have a reflex for that button.

---

## Matrices (8 stereo)

The matrices are where zone-specific processing lives — room EQ, delay, limiting.
Keeping it here rather than on the main buses means the broadcast mix never
inherits the room correction.

| MTX | Name | Source | Processing | Output |
|---|---|---|---|---|
| **1** | **PA L/R** | Main 1 | Room EQ (31-band GEQ), delay `___ ms`, limiter | Local out 1–2 |
| **2** | **SUBS** | Bus 15 | LPF 90 Hz 24 dB/oct, delay `___ ms`, limiter | Local out 3 |
| 3 | FRONT FILL | Main 1 | HPF 120 Hz, delay `___ ms`, −6 dB | Local out 4 |
| 4 | LOBBY | Main 3 | HPF 120 Hz, LPF 12 kHz, speech +3 dB @ 2.5 kHz | Local out 7 |
| 5 | NURSERY | Main 3 | Same as lobby, independent level | SD16 out 1 |
| **6** | **BROADCAST** | **Main 2** | Delay for lip-sync `___ ms`, true-peak limiter | Local out 5–6 + AES |
| 7 | HEARING ASSIST | Main 3 | HPF 150 Hz, speech +4 dB @ 3 kHz, compressor 4:1, **no FX** | Local out 8 |
| 8 | GREEN ROOM | Main 3 | Flat, −10 dB | SD16 out 2 |

Fill in the blank delay values during commissioning — see doc 06 for the
measurement procedure.

### Matrix 1 — house PA processing chain

```
Main 1 ──► 31-band GEQ (room correction) ──► Delay ──► Limiter ──► Local out 1-2
```

- **GEQ:** cuts only. If you find yourself boosting more than 3 dB anywhere, the
  problem is speaker placement, not EQ.
- **Limiter:** threshold set **3 dB below** the point at which your amplifiers clip.
  This protects the PA and the congregation's hearing. It is not a mix tool — if the
  limiter is working during normal service, the mix is too loud.

### Matrix 6 — broadcast processing chain

See doc 07 for the full chain. The delay value here is the lip-sync offset measured
against the Osee — see doc 11.
