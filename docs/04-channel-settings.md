# 04 — Channel Settings

Starting points for every channel, ready to be dialled in during commissioning.

**These are starting points, not laws.** They are chosen to be safe, musical and
immediately usable with a typical church PA and a typical worship band. Adjust to
your room and your players — then write the changes back into this document.

## How to read these tables

- **Gain** — analog preamp. Set it so the channel meter sits around **−18 dBFS**
  on average material with peaks no higher than **−10 dBFS**. The values given
  assume a typical source at typical volume; your gain will differ.
- **HPF** — high-pass filter, 12 dB/oct unless stated. The single most valuable
  control on the desk. Almost every channel should have one.
- **Gate** — `threshold / range / attack / hold / release`. Range is how far the
  gate closes. We never close a gate fully on a drum; 20–25 dB of reduction is
  plenty and sounds natural.
- **EQ** — `frequency / gain / Q`. Cuts before boosts, always. A cut that solves a
  problem beats a boost that masks one.
- **Comp** — `threshold / ratio / attack / release / makeup`, with the WING
  compressor model where it matters.

## Gain staging procedure (do this first, every time)

1. All faders down, all mutes in.
2. Channel by channel: have the source produce its **loudest realistic** sound —
   the drummer hitting hard, the vocalist at full voice, the pastor's laugh.
3. Raise the preamp until peaks read **−10 dBFS**. Not −6. Not 0. **−10.**
4. Leave 10 dB of headroom above that for surprises. Sunday always has surprises.
5. Record the final gain value in the table below. Gain is **safed from scene
   recall** — see doc 12.

> **Why −18 dBFS average?** It matches the nominal operating level of the analog
> outputs, it leaves headroom for the dynamics processors to work in their intended
> range, and it gives Logic Pro a recording level that will never clip. Chasing a
> hotter meter buys nothing in a 24-bit digital console and costs everything when
> someone screams into a handheld.

---

## Drums

### Ch 1 — Kick In

| Parameter | Setting |
|---|---|
| Gain | ~+20 dB (start), target −10 dBFS peaks |
| Phantom | Off |
| HPF | 30 Hz, 12 dB/oct |
| Gate | −35 dB / 20 dB range / 0.5 ms attack / 40 ms hold / 200 ms release |
| EQ 1 | 60 Hz, **+3 dB**, Q 1.2 — weight |
| EQ 2 | 350 Hz, **−6 dB**, Q 2.5 — box/cardboard |
| EQ 3 | 3.5 kHz, **+4 dB**, Q 1.5 — beater click |
| EQ 4 | 8 kHz LPF or shelf −3 dB — remove cymbal bleed |
| Comp | −20 dB / 4:1 / 10 ms attack / 120 ms release / +4 dB makeup |
| Sends | Bus 15 (SUB) **ON**, post-fader, −3 dB |
| Broadcast | **+3 dB** relative to house — the stream has no acoustic kick in the room |

### Ch 2 — Kick Out

| Parameter | Setting |
|---|---|
| Gain | ~+18 dB |
| HPF | 25 Hz |
| Gate | Keyed from Ch 1 (gate side-chain source = Kick In) — **this is important**, it keeps the two kick mics gating together |
| EQ 1 | 50 Hz, **+4 dB**, Q 1.0 — sub weight |
| EQ 2 | 250 Hz, **−4 dB**, Q 2.0 |
| EQ 3 | 6 kHz LPF — this mic is for low end only |
| Comp | −18 dB / 4:1 / 15 ms / 150 ms |
| Sends | Bus 15 (SUB) **ON**, post-fader, 0 dB |
| Notes | **Check polarity against Ch 1.** Flip and listen; keep whichever is louder in the low end. |

### Ch 3 — Snare Top

| Parameter | Setting |
|---|---|
| Gain | ~+24 dB |
| HPF | 100 Hz, 12 dB/oct |
| Gate | −30 dB / 20 dB range / 0.3 ms attack / 30 ms hold / 150 ms release |
| EQ 1 | 200 Hz, **+2 dB**, Q 1.5 — body |
| EQ 2 | 600 Hz, **−4 dB**, Q 3.0 — honk |
| EQ 3 | 5 kHz, **+4 dB**, Q 1.5 — crack |
| Comp | −18 dB / 4:1 / 5 ms / 100 ms / +3 dB |
| Sends | Bus 11 (Vocal Hall) OFF; Bus 14 (Drum Room) **ON**, −10 dB |
| Broadcast | **+2 dB** relative to house |

### Ch 4 — Snare Bottom

| Parameter | Setting |
|---|---|
| Gain | ~+26 dB |
| Polarity | **INVERTED** — non-negotiable, it is pointed the opposite way to the top mic |
| HPF | 200 Hz |
| Gate | Keyed from Ch 3 (side-chain = Snare Top) |
| EQ 1 | 400 Hz, **−4 dB**, Q 2.0 |
| EQ 2 | 8 kHz, **+5 dB**, shelf — snare wires |
| Comp | Off |
| Notes | Blend to taste under the top mic — typically 10–14 dB below it. If it does not add sizzle, mute it and move on. |

### Ch 5 — Hi-Hat

| Parameter | Setting |
|---|---|
| Gain | ~+22 dB |
| Phantom | On |
| HPF | **400 Hz, 12 dB/oct** — aggressive, and correct |
| Gate | Off — gating a hi-hat sounds unnatural |
| EQ 1 | 1 kHz, **−4 dB**, Q 2.0 — clank |
| EQ 2 | 10 kHz, **+2 dB**, shelf — air |
| Comp | Off |
| Notes | In most rooms the overheads already carry the hi-hat. Start with this channel down 8 dB and only bring it up if the hat genuinely disappears. |

### Ch 6–8 — Toms (Rack 1, Rack 2, Floor)

| Parameter | Rack 1 | Rack 2 | Floor |
|---|---|---|---|
| Gain | ~+22 dB | ~+22 dB | ~+20 dB |
| HPF | 80 Hz | 70 Hz | 50 Hz |
| Gate | −32 dB / 25 dB / 1 ms / 80 ms / 250 ms | same | −34 dB / 25 dB / 1 ms / 120 ms / 350 ms |
| EQ 1 | 120 Hz **+3 dB** Q 1.2 | 100 Hz **+3 dB** Q 1.2 | 80 Hz **+4 dB** Q 1.0 |
| EQ 2 | 400 Hz **−5 dB** Q 2.5 | 400 Hz **−5 dB** Q 2.5 | 350 Hz **−5 dB** Q 2.5 |
| EQ 3 | 4 kHz **+3 dB** Q 1.5 | 4 kHz **+3 dB** Q 1.5 | 3.5 kHz **+3 dB** Q 1.5 |
| LPF | 8 kHz | 8 kHz | 7 kHz |
| Comp | −16 dB / 3:1 / 10 ms / 200 ms | same | same |
| Floor tom → Bus 15 (SUB) | — | — | **ON**, −8 dB |

> **Tom gates are the most common mis-set processors in church audio.** If the gate
> chatters during quiet passages, raise the threshold. If toms disappear on soft
> fills, lower it and lengthen the hold. Set them with the drummer playing a full
> song, never with isolated hits.

### Ch 9/10 — Overheads L/R

| Parameter | Setting |
|---|---|
| Gain | ~+28 dB |
| Phantom | On |
| Link | **Stereo linked** |
| HPF | **250 Hz, 12 dB/oct** — the overheads are for cymbals, not for kick |
| Gate | Off |
| EQ 1 | 800 Hz, **−3 dB**, Q 1.5 — clutter |
| EQ 2 | 3 kHz, **−2 dB**, Q 2.0 — harshness |
| EQ 3 | 12 kHz, **+3 dB**, shelf — sheen |
| Comp | −22 dB / 2.5:1 / 20 ms / 250 ms — gentle glue only |
| Pan | Hard L / hard R for broadcast; narrow to 70% for house |
| Broadcast | **+4 dB** relative to house — online, the overheads *are* the drum kit |

### Ch 11 — Percussion / Cajon

| Parameter | Setting |
|---|---|
| Gain | ~+26 dB, phantom on |
| HPF | 80 Hz (cajon) / 200 Hz (shaker, tambourine) |
| Gate | Off |
| EQ | 300 Hz −3 dB Q 2.0; 4 kHz +3 dB Q 1.5 |
| Comp | −18 dB / 3:1 / 10 ms / 150 ms |

---

## Bass

### Ch 13 — Bass DI (primary)

| Parameter | Setting |
|---|---|
| Gain | ~+12 dB (DI level) |
| HPF | **35 Hz** — protects the subs from sub-audible rumble |
| Gate | Off |
| EQ 1 | 80 Hz, **+2 dB**, Q 1.0 — fundamental |
| EQ 2 | 250 Hz, **−4 dB**, Q 2.0 — mud, the biggest single win on this channel |
| EQ 3 | 800 Hz, **+2 dB**, Q 1.5 — definition (this is what makes bass audible on a phone) |
| EQ 4 | 5 kHz LPF, 12 dB/oct — string noise |
| Comp | −20 dB / **4:1** / 20 ms attack / 120 ms release / +5 dB makeup |
| Sends | Bus 15 (SUB) **ON**, post-fader, 0 dB |
| Broadcast | **+1 dB**, and **more 800 Hz** — laptop and phone speakers reproduce no fundamental at all, so the harmonic is the only thing the viewer hears |

### Ch 14 — Bass Amp Mic

| Parameter | Setting |
|---|---|
| Gain | ~+24 dB |
| HPF | 50 Hz |
| Polarity | **Check against Ch 13.** Time-align if the console offers delay on the channel; even 1 ms matters here. |
| EQ | 300 Hz −3 dB Q 2.0; 2 kHz +3 dB Q 1.5 (grit) |
| Comp | −18 dB / 3:1 / 20 ms / 150 ms |
| Notes | This channel is a *flavour* layer under the DI, usually 8–12 dB below it. If the band uses a modeler, mute it. |

---

## Guitars

### Ch 15/16 — Electric Guitar 1 & 2

| Parameter | Setting |
|---|---|
| Gain | ~+20 dB (cab mic) / ~+6 dB (modeler DI) |
| HPF | **120 Hz** — guitars do not need low end; the bass does |
| Gate | Off (use the player's own noise gate on their pedalboard) |
| EQ 1 | 400 Hz, **−3 dB**, Q 2.0 — boxiness |
| EQ 2 | 2.5 kHz, **−3 dB**, Q 3.0 — the "ice pick" that fatigues a congregation |
| EQ 3 | 6 kHz, **+2 dB**, Q 1.5 — presence |
| LPF | 10 kHz |
| Comp | −18 dB / 3:1 / 15 ms / 150 ms |
| Pan | EG1 at 30% L, EG2 at 30% R |
| Broadcast | Pan wider (50%) — stereo width reads well on headphones |

### Ch 17/18 — Acoustic Guitar 1 & 2

| Parameter | Setting |
|---|---|
| Gain | ~+14 dB (active DI) |
| HPF | **100 Hz** |
| Gate | Off |
| EQ 1 | 180 Hz, **−5 dB**, Q 2.0 — piezo boom, the classic acoustic DI problem |
| EQ 2 | 900 Hz, **−3 dB**, Q 2.5 — quack |
| EQ 3 | 8 kHz, **+3 dB**, shelf — sparkle |
| Comp | −20 dB / 3.5:1 / 10 ms / 120 ms / +4 dB |
| Notes | If the acoustic is the only harmonic instrument in a quiet moment, ease the 180 Hz cut back to −2 dB. |

---

## Keys

### Ch 19/20 — Keys L/R, Ch 21/22 — Pads L/R

| Parameter | Keys | Pads |
|---|---|---|
| Gain | ~+10 dB | ~+10 dB |
| Link | Stereo linked | Stereo linked |
| HPF | 60 Hz | **150 Hz** — pads must not fight the bass |
| EQ 1 | 300 Hz **−3 dB** Q 2.0 | 400 Hz **−4 dB** Q 2.0 |
| EQ 2 | 2 kHz **−2 dB** Q 2.0 | 1.5 kHz **−2 dB** Q 2.0 |
| EQ 3 | 10 kHz **+2 dB** shelf | 12 kHz **+2 dB** shelf |
| Comp | −20 dB / 3:1 / 20 ms / 200 ms | −24 dB / 2:1 / 30 ms / 300 ms |
| Sends | Bus 15 (SUB) ON at −12 dB if the piano patch carries low end | SUB **OFF** |
| Pan | Full stereo | Full stereo |

> **Pads are the glue of modern worship and the enemy of clarity.** Keep the 150 Hz
> HPF. If the mix ever sounds "cloudy" and you cannot find the cause, pull the pads
> down 3 dB and the fog usually lifts.

---

## Vocals

### Ch 25 — Worship Leader

The most important sung channel on the desk.

| Parameter | Setting |
|---|---|
| Gain | ~+35 dB (dynamic handheld) / ~+28 dB (condenser) |
| HPF | **110 Hz, 12 dB/oct** |
| Gate | −38 dB / 12 dB range / 1 ms / 100 ms / 300 ms — gentle, just to close between songs |
| EQ 1 | 250 Hz, **−3 dB**, Q 2.0 — proximity mud |
| EQ 2 | 500 Hz, **−2 dB**, Q 2.5 — boxiness |
| EQ 3 | 3 kHz, **+3 dB**, Q 1.5 — intelligibility |
| EQ 4 | 8 kHz, **+2 dB**, shelf — air |
| De-ess | Insert a de-esser: 6.5 kHz, 4 dB reduction threshold |
| Comp | −22 dB / **3.5:1** / 8 ms attack / 90 ms release / +5 dB makeup |
| Sends | Bus 11 (Hall) −12 dB, Bus 13 (Delay) −18 dB, both post-fader |
| Broadcast | **+2 dB**, more compression (see doc 07), reverb send **+3 dB** — the room is not doing the work online |

### Ch 26–28 — BGV 1, 2, 3

| Parameter | Setting |
|---|---|
| Gain | ~+35 dB |
| HPF | **120 Hz** |
| Gate | −36 dB / 15 dB range / 1 ms / 100 ms / 250 ms |
| EQ 1 | 300 Hz, **−4 dB**, Q 2.0 |
| EQ 2 | 3 kHz, **+2 dB**, Q 1.5 |
| EQ 3 | 10 kHz, **+2 dB**, shelf |
| Comp | −20 dB / 4:1 / 10 ms / 100 ms / +5 dB |
| Sends | Bus 12 (Plate) −10 dB |
| Pan | BGV1 20% L, BGV2 centre, BGV3 20% R |
| Notes | BGVs sit **6–8 dB below** the worship leader. If you cannot tell who the leader is, the BGVs are too loud. |

### Ch 43/44 — Choir L/R

| Parameter | Setting |
|---|---|
| Gain | ~+40 dB, phantom on, stereo linked |
| HPF | 150 Hz |
| Gate | Off |
| EQ | 400 Hz −4 dB Q 2.0; 4 kHz +3 dB Q 1.5; 12 kHz +2 dB shelf |
| Comp | −24 dB / 3:1 / 20 ms / 250 ms |
| Notes | Choir mics are the highest feedback risk in the building. Ring them out during commissioning and note the notch frequencies here: `_____ Hz`, `_____ Hz`, `_____ Hz` |

---

## Speech — the highest-priority channels in the building

People forgive a rough music mix. Nobody forgives not being able to hear the sermon.

### Ch 33 — Pastor Headset (primary)

| Parameter | Setting |
|---|---|
| Gain | ~+30 dB — **re-verify every single service**, headset placement changes everything |
| HPF | **120 Hz, 18 dB/oct** — steeper than on sung vocals, speech has no useful energy below this |
| Gate | −42 dB / 10 dB range / 1 ms / 150 ms / 400 ms — shallow, to reduce open-mic room noise without chopping word beginnings |
| EQ 1 | 200 Hz, **−4 dB**, Q 2.0 — chest boom |
| EQ 2 | 400 Hz, **−3 dB**, Q 2.5 — muddiness |
| EQ 3 | 2.5 kHz, **+4 dB**, Q 1.5 — **consonant clarity, the intelligibility band** |
| EQ 4 | 6 kHz, **+2 dB**, Q 1.5 — articulation |
| De-ess | 7 kHz, 5 dB reduction |
| Comp | −24 dB / **4:1** / 5 ms attack / 80 ms release / +6 dB makeup |
| Automix | **Group X, weight 0 dB** |
| Sends | FX **OFF** — no reverb on speech in the house. Bus 9 (Pulpit wedge) at −10 dB. |
| Broadcast | **+3 dB**, plus broadcast compression (doc 07), plus a *touch* of short room reverb (−24 dB) so it does not sound like a voiceover booth |

### Ch 34 — Pastor Lav (backup)

Same settings as Ch 33, with these differences:

| Parameter | Setting |
|---|---|
| EQ 1 | 300 Hz, **−5 dB**, Q 2.0 — lavs are chestier than headsets |
| EQ 3 | 4 kHz, **+5 dB**, Q 1.5 — lavs lose presence under clothing |
| State | **Gain set, channel muted.** Unmute only if the headset fails. |
| Automix | Group X, weight **−10 dB** (so it never wins over the headset) |

> **This channel is live insurance.** Test it at soundcheck every week. The one
> Sunday you skip it is the Sunday the headset battery dies mid-sermon.

### Ch 35/36 — Handheld 1 & 2

| Parameter | Setting |
|---|---|
| Gain | ~+32 dB |
| HPF | 120 Hz, 18 dB/oct |
| Gate | −40 dB / 12 dB range / 1 ms / 150 ms / 350 ms |
| EQ | 250 Hz −4 dB Q 2.0; 2.5 kHz +3 dB Q 1.5; 8 kHz +2 dB shelf |
| Comp | −24 dB / 4:1 / 5 ms / 80 ms / +5 dB |
| Automix | Group X, weight 0 dB |
| Notes | Handhelds get passed between people with wildly different voices and mic technique. The compressor is doing more work here than anywhere else on the desk — leave it alone. |

### Ch 37 — Lectern

| Parameter | Setting |
|---|---|
| Gain | ~+36 dB, phantom on |
| HPF | **150 Hz, 18 dB/oct** — the highest HPF of any speech channel; lecterns are mounted on resonant furniture |
| Gate | −40 dB / 15 dB range / 1 ms / 200 ms / 400 ms |
| EQ 1 | 300 Hz, **−5 dB**, Q 2.5 — lectern body resonance |
| EQ 2 | 2.5 kHz, **+4 dB**, Q 1.5 |
| EQ 3 | Notch as required after ringing out: `_____ Hz` |
| Comp | −24 dB / 4:1 / 5 ms / 80 ms |
| Automix | Group X, weight 0 dB |

### Ch 38–40 — Guest, Kids, Spare

Copy the Handheld 1 settings. These channels exist so that an unexpected speaker
never means a scramble. Keep them gain-staged, processed and muted.

---

## Playback & media

### Ch 30/31 — Tracks L/R

| Parameter | Setting |
|---|---|
| Gain | ~+6 dB (line), stereo linked |
| HPF | 40 Hz |
| EQ 1 | 400 Hz, −2 dB, Q 1.5 — carve space for the live band |
| EQ 2 | 3 kHz, −2 dB, Q 2.0 — let the live vocals sit above the tracks |
| Comp | Off — the tracks are already mastered |
| Sends | Bus 15 (SUB) **ON**, −6 dB |
| Notes | Tracks arrive pre-mixed and loud. If they are fighting the band, the answer is the fader, not more EQ. |

### Ch 45/46 — Media / Video Playback

| Parameter | Setting |
|---|---|
| Gain | ~+6 dB, stereo linked |
| HPF | 50 Hz |
| EQ | 2.5 kHz +3 dB Q 1.5 — dialogue intelligibility in a reverberant room |
| Comp | −20 dB / 3:1 / 10 ms / 150 ms — video audio is wildly inconsistent |
| Notes | **Always check a video's audio before the service.** Every week. |

### Ch 41/42 — Ambience L/R (broadcast only)

| Parameter | Setting |
|---|---|
| Gain | ~+40 dB, phantom on, stereo linked |
| HPF | **200 Hz** — removes HVAC rumble and stage spill |
| Gate | Off |
| EQ 1 | 500 Hz, −4 dB, Q 2.0 |
| EQ 2 | 2 kHz, −3 dB, Q 2.0 — reduces PA spill, keeps congregation voices |
| EQ 3 | 10 kHz, +2 dB, shelf |
| Comp | −30 dB / **6:1** / 30 ms / 400 ms — heavily compressed; we want a consistent bed, not dynamics |
| Main 1 | **UNASSIGNED — and locked** |
| Main 2 | Assigned, sitting **12–18 dB below** the music |
| Notes | Push these up during congregational singing and the response to an altar call; pull them down during the sermon so audience noise does not distract. This is the highest-value fader move in the entire broadcast mix. |

---

## Channels that must never reach a main bus

| Ch | Name | Enforcement |
|---|---|---|
| 24 | Cues / Guide | Unassigned from Main 1–4, channel locked |
| 32 | Click | Unassigned from Main 1–4, channel locked |
| Aux 5 | Talkback | Assigned to Bus 1–8 only |

Verify this at the start of every commissioning session and after every firmware
update. Firmware updates have been known to reset assignment states.

---

## Automix configuration (Group X — speech)

| Setting | Value |
|---|---|
| Members | Ch 33, 34, 35, 36, 37, 38, 39, 40 |
| Weight — Pastor Headset (33) | **0 dB** |
| Weight — Pastor Lav (34) | −10 dB |
| Weight — Handheld 1, 2 (35, 36) | 0 dB |
| Weight — Lectern (37) | −2 dB |
| Weight — Guest, Kids, Spare (38–40) | 0 dB |
| Group Y | Unused — reserved for a future panel/drama setup |

**Automix is never applied to sung vocals, instruments or ambience mics.** It works
by attenuating channels that are not the loudest, which is exactly wrong for music.
