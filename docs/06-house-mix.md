# 06 — House Mix (In-Room)

## Targets

| Content | Average (dBA, slow, at FOH) | Peak ceiling |
|---|---|---|
| Pre-service walk-in music | 72–76 dBA | 82 dBA |
| Contemporary worship | **88–92 dBA** | 98 dBA |
| Quiet/reflective worship | 80–85 dBA | 90 dBA |
| Sermon / speech | **72–78 dBA** | 85 dBA |
| Video playback | 78–82 dBA | 88 dBA |
| Altar call / prayer | 70–75 dBA | 82 dBA |

Measure with an SPL meter at the FOH position, A-weighted, slow response. Keep a
meter permanently at FOH and glance at it — opinions about loudness are unreliable
after twenty minutes of mixing; a meter is not.

**On hearing safety:** 90 dBA is safe for hours. 100 dBA is safe for about fifteen
minutes. A worship set that peaks at 100 dBA is not more anointed; it is louder. If
the congregation is covering their ears or the children's area is complaining, the
answer is not a better EQ.

---

## Aux-fed subwoofers

This is the single highest-impact decision in the house configuration.

**Conventional (wrong) approach:** the subs get a copy of the full main mix, so
every vocal, guitar, cymbal and handclap dumps low-frequency energy into them. The
result is a muddy, boomy room where the pastor's voice rumbles and the kick has no
definition.

**Aux-fed (correct) approach:** only the channels that *should* have low-frequency
content are sent to the subs.

### Bus 15 (SUB FEED) membership

| Ch | Source | Send level | Reason |
|---|---|---|---|
| 1 | Kick In | −3 dB | Attack and weight |
| 2 | Kick Out | 0 dB | Primary sub content |
| 8 | Floor Tom | −8 dB | Body |
| 13 | Bass DI | **0 dB** | The foundation |
| 14 | Bass Amp | −10 dB | Blend |
| 19/20 | Keys L/R | −12 dB | Only if the piano/synth patch carries real low end |
| 30/31 | Tracks L/R | −6 dB | Programmed sub content |
| **Everything else** | **OFF** | | |

Vocals, guitars, overheads, hi-hat, percussion, speech, ambience and media
**never** go to the subs.

### Matrix 2 (SUBS) processing

| Stage | Setting |
|---|---|
| Source | Bus 15, mono |
| LPF | 90 Hz, 24 dB/oct (match your crossover point) |
| HPF | 30 Hz, 24 dB/oct — infrasonic protection |
| Polarity | Check against the mains — see alignment below |
| Delay | Measured value: `_____ ms` |
| Limiter | 3 dB below amplifier clip |

### Sub/main alignment procedure

1. Play pink noise through mains only, measure with a measurement mic at FOH.
2. Play pink noise through subs only, same position.
3. Play both. If the response **dips** at the crossover frequency, the subs are out
   of polarity or out of time.
4. Flip sub polarity. If the dip fills in, leave it flipped.
5. Still dipping? Adjust sub delay in 0.5 ms steps until the crossover region is
   flat. Write the value into the table above.

A misaligned crossover costs you 6–10 dB of impact in the most important octave of
the mix. It is worth twenty minutes with a measurement rig.

---

## Room EQ (Matrix 1 GEQ)

### Procedure

1. Measurement mic at FOH position, pink noise through the mains at ~85 dBA.
2. Average several measurement positions — one point in a room is a lie.
3. Target curve: **flat from 100 Hz to 2 kHz, gently falling above 2 kHz** to about
   −4 dB at 16 kHz. A perfectly flat house curve sounds harsh and fatiguing.
4. **Cuts only.** Boosting a null wastes amplifier power and cannot fix it —
   nulls are caused by reflections and cannot be EQ'd away.
5. Keep every filter under 6 dB of cut. More than that is a physical problem.

### Typical church room problems and their fix

| Symptom | Frequency | Usual cause | Fix |
|---|---|---|---|
| Boomy, one-note bass | 100–200 Hz | Room mode, subs in a corner | Narrow cut, then move the subs |
| Muddy, unclear | 250–400 Hz | Buildup from too many sources | Channel HPFs (doc 04), then a broad −3 dB |
| Honky, nasal | 500–800 Hz | Speaker horn resonance | Narrow cut, 2–4 dB |
| Harsh, fatiguing | 2–4 kHz | Horn drivers, hard surfaces | Broad −2 to −3 dB |
| Sibilant, splashy | 6–10 kHz | Overbright PA, hard ceiling | Gentle shelf, −2 dB |
| No intelligibility | — | Reverberation time too long | **Acoustic treatment. EQ cannot fix this.** |

> If speech intelligibility is poor and the room reverberation time is over about
> 1.5 seconds, no amount of console work will solve it. The fix is absorption on the
> rear wall and the ceiling. Budget for it; it will improve every service forever.

---

## Delay rings

Any loudspeaker that is not at the stage must be delayed so its sound arrives with
the main PA, not before it.

**Formula:** `delay (ms) = distance (metres) × 2.9` — or `distance (feet) × 0.885`

Then **add 10–15 ms** on top. This is the Haas effect: the listener's brain
localises to the first arrival, so a slightly late fill speaker still sounds like it
is coming from the stage.

| Zone | Distance from main PA | Calculated | +Haas | **Final** |
|---|---|---|---|---|
| Front fills | `___ m` | `___ ms` | +10 ms | `_____ ms` |
| Under-balcony | `___ m` | `___ ms` | +12 ms | `_____ ms` |
| Rear delays | `___ m` | `___ ms` | +15 ms | `_____ ms` |

Measure with a tape or a laser, not by eye.

---

## House mix priorities, in order

When the mix is fighting you, fix in this order. Do not skip steps.

1. **Is the speech intelligible?** Nothing else matters if the answer is no.
2. **Can you hear the lead vocal clearly, always?** The congregation is following
   the melody. If they cannot hear it, they will not sing.
3. **Is the kick and bass relationship clear?** Kick attack, bass sustain. They
   should occupy different spaces, not the same one.
4. **Is the mix too loud?** Check the meter, not your feelings.
5. **Only then:** guitars, keys, effects, polish.

## Common house mix failures at GHC-type venues

| Problem | Real cause | Fix |
|---|---|---|
| "I can't hear the pastor" | Speech competing with HVAC; 2.5 kHz not present enough | Doc 04 speech EQ; check the DCA 1 level against the SPL target |
| "The music is too loud" | Usually the 2–4 kHz region, not the overall level | Pull the harshness before you pull the master |
| "It sounds muddy" | Too many sources with no HPF | Every channel gets a HPF. Every one. |
| "The congregation isn't singing" | Mix too loud to sing over, or the leader is buried | Drop 3 dB, push the worship leader 2 dB |
| Feedback during the sermon | Wedge level, lectern mic gain | Doc 08 |
