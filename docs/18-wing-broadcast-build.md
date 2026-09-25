# 18 — WING-Native Broadcast Build

**Decision: the broadcast mix moves onto the WING. Logic Pro comes out of the live
signal path entirely.** The stream is built on Bus 7, mastered on Matrix 5, and
leaves the console as two analog XLRs into the Osee.

Logic keeps one job: **multitrack recording and virtual soundcheck.** Nothing live
depends on the Mac any more, which also removes the two-clock problem in doc 17 and
the single point of failure.

---

## A correction to what I told you earlier

I said Multipressor, Match EQ, Exciter and Adaptive Limiter have no WING equivalent.
**That was wrong**, and it matters because it changes what this build can achieve.
Having now read the FX rack in your console file, your firmware has direct
counterparts for all four:

| Logic stock plugin | WING equivalent | Confirmed in your file |
|---|---|---|
| Multipressor | **C5-CMB** (5-band multiband dynamics) | FX6 |
| Adaptive Limiter | **LIMITER** (precision limiter) | FX8, FX16 |
| Exciter | **SPKMAN** (Sound Maxer) | FX10 |
| Match EQ | **DEQ3** (dynamic EQ) — not a true match EQ, but the practical substitute | FX5 |
| DeEsser | **DE-S2** | FX9 |
| Compressor (circuit types) | **COMP, 76LA, LA, F670, ECL33, D241C, SBUS, NSTR, CMB** | throughout |
| Noise Gate | **GATE, EXP** | throughout |
| Channel EQ | **STD** (6-band) / **PULSAR** on buses and matrices | throughout |
| Space Designer / ChromaVerb | **VSS3, V-ROOM** | FX1, FX2 |
| Stereo Delay | **ST-DL** | FX3, FX4 |
| Tape saturation | **TAPE** | FX15 |

There is nothing in that template you cannot rebuild here. The WING's processing is
not a compromise — VSS3 and the 76LA/LA/F670 emulations are better than Logic's
stock equivalents.

---

## The one real constraint

In Logic, the broadcast mix worked from the **raw USB split**, so every channel had
completely independent EQ and compression from the house.

On the WING, the broadcast bus taps **after** the channel strip. Channel EQ, gating
and compression are **shared** between house and broadcast. Only three things can
differ:

1. The **send level** to the broadcast bus, per channel
2. **Group processing** on the broadcast subgroups
3. **Master processing** on the broadcast bus and matrix

That is enough to build an excellent stream — the offsets, the crowd mics, the
multiband and the mastering chain are all still available. But it means the channel
strips must be set **neutral and broadcast-friendly**, with room-specific correction
living in the PA matrix GEQs (FX12/13/14), where it already does.

**For the two channels where this matters most — the pastor and the lead vocal —
there is a workaround: duplicate the input onto a spare channel** with its own
processing, sent only to broadcast. See "Optional: dedicated broadcast channels" at
the end. You have four spare channels for this.

---

## Architecture

```
CHANNELS                          GROUPS                    MASTER              OUT

ch 1–7   Drums      ──POST──►  Bus 11 "BC DRUMS" ──┐
                                 COMP glue          │
                                                    │
ch 8–12, 17, 18                                     │
Bass/Gtr/Keys/Trk   ──POST──────────────────────────┤
                                                    │
ch 13–16, 20, 22,                                   │
24–27  Singers      ──POST──►  Bus 13 "BC VOX" ─────┤
                                 DE-S2 + F670       │
                                                    ├──►  Bus 7 "BROADCAST"  ──►  MTX 5 "STREAM"  ──►  LCL 4/5  ──►  OSEE
ch 21, 23, 33                                       │      EQ + SBUS comp          TAPE → PULSAR EQ
Speech              ──POST──────────────────────────┤      + C5-CMB multiband      → ECL33 → LIMITER
                                                    │                              + lip-sync DELAY
ch 29, 30  Crowd    ──POST──────────────────────────┤
                                                    │
Bus 14 Inst Verb    ──────────────────────────────  ┤
Bus 15 Vox Verb     ──────────────────────────────  ┤
Bus 16 Slap         ──────────────────────────────  ┘
```

Most of this already exists in your file. Bus 7 is already named BROADCAST, already
fed by the instruments, singers and speech, and already feeds Matrix 5 at unity. The
work is: unmute it, add what's missing, add the group processing, and patch the
output.

---

## Step 1 — Routing changes

| # | Change | Why |
|---|---|---|
| 1.1 | **Unmute Bus 7 "BROADCAST"** | It is the broadcast master |
| 1.2 | **Turn OFF `Main 1 → MX5`** | The stream must be the broadcast bus, not a copy of the house mix |
| 1.3 | Name **Bus 11** → `BC DRUMS`, unmute, fader to 0 | Free bus, becomes the drum subgroup |
| 1.4 | Rename **Bus 13** "Choir Bus" → `BC VOX`, **unmute**, fader to 0 | It is already fed by Vox 1–3 and already sends to Bus 7 at −3 |
| 1.5 | **Unmute Bus 14 (Inst Verb) and Bus 16 (Slap)** | Both already send to Bus 7 at −3 and are currently silent |
| 1.6 | Move **ch 29 / ch 30 (Crowd)** off their direct MX5 sends and onto **Bus 7** | So crowd level rides with the rest of the broadcast mix |
| 1.7 | **Stereo-link ch 29 / 30** | They are a stereo pair and are currently unlinked mono |
| 1.8 | Patch **MTX5 L → LCL out 4** and **MTX5 R → LCL out 5** | Currently Matrix 5 goes nowhere |
| 1.9 | **Enable delay on MTX5** | Lip-sync — measure it, see doc 11 |
| 1.10 | Clear USB outs **43, 44, 47, 48** | Junk: a −52 dB bus and a muted main, each duplicated |

### Send mode: keep POST-fader

All existing channel sends to Bus 7 are **post-fader**. Keep them that way.

Post-fader means the broadcast follows your house moves — pull a howling mic and it
leaves both mixes. Pre-fader would give you the fully independent mix Logic had, but
it requires someone actively maintaining a second mix all service. For a
volunteer-run desk, post-fader with good offsets is the more reliable product.

The crowd mics are effectively independent anyway, because they are not in the house
at all — their channel fader **is** their broadcast fader.

---

## Step 2 — FX rack reallocation

All 16 slots are currently in use. Two are being wasted:

| Slot | Currently | Currently on | Verdict |
|---|---|---|---|
| **FX7** | MACH4 | ch 33 (unnamed — this is the Kids Lapel) | **Reclaim.** A premium processor on a kids' lapel mic. |
| **FX11** | GEQ | ch 33 (same channel) | **Reclaim.** A 31-band graphic on a lapel mic is not a good use of a slot. |

### Reassign

| Slot | Change model to | Insert on | Role |
|---|---|---|---|
| **FX7** | **C5-CMB** | **Bus 7 BROADCAST** — post-insert | The Multipressor equivalent. The single most valuable processor in this build. |
| **FX11** | **DE-S2** | **Bus 13 BC VOX** — pre-insert | De-essing the whole vocal group at once, before it hits the broadcast master |

### Leave alone

| Slot | Model | On | Keep because |
|---|---|---|---|
| FX1 | VSS3 | Bus 15 Vox Verb | Premium reverb, correctly placed |
| FX2 | V-ROOM | Bus 14 Inst Verb | Correctly placed |
| FX3 / FX4 | ST-DL | Bus 16 Slap / Aux 4 Delay | Correctly placed |
| **FX5 / FX6** | **DEQ3 / C5-CMB** | **ch 21 Pastor Lapel** | Dynamic EQ plus multiband on the pastor's channel is excellent, and it serves both house and broadcast. Leave it. |
| FX8 | LIMITER | Main 1 | PA protection |
| FX9 / FX10 | DE-S2 / SPKMAN | Bus 1 STAGE MON | De-esser on IEMs is sensible. SPKMAN on monitors is debatable — if you later need a slot, this is the one to take. |
| FX12/13/14 | GEQ | MTX1/2/3 | PA room correction |
| FX15 / FX16 | TAPE / LIMITER | MTX5 STREAM | The mastering stage, already correct |

> Verify your firmware allows premium models in every slot. Yours already has DE-S2
> in slot 9, SPKMAN in 10, TAPE in 15 and LIMITER in 16, so there appears to be no
> restriction — but confirm before committing.

---

## Step 3 — Bus 11 "BC DRUMS"

The drums currently have **no send to Bus 7 at all**. Unmute the broadcast bus as it
stands today and the stream has no kit. This group fixes that.

### Sends into Bus 11 (post-fader)

Start here, then balance by ear against the vocals. The offsets are relative to the
house drum balance, which carries over through the post-fader tap.

| Ch | Source | Send to Bus 11 | Offset vs house | Why |
|---|---|---|---|---|
| 1 | Kick | **0.0 dB** | +3 | No acoustic kick in the room online |
| 2 | Snare | **−1.0** | +2 | Same |
| 3 | HH / Snr Btm | **−2.0** | +1 | Resolve this channel's identity first (audit M1) |
| 4 | Rack 1 | **−1.0** | +2 | |
| 5 | Rack 2 | **−1.0** | +2 | |
| 6 | Floor | **−1.0** | +2 | |
| 7 | OHs | **+1.0** | +4 | **Online, the overheads are the drum kit.** Biggest single offset in the build. |

### Bus 11 processing

| Stage | Setting |
|---|---|
| EQ (STD) | 200 Hz **−2 dB** Q 1.2 — clears space for the bass |
| | 400 Hz **−3 dB** Q 2.0 — boxiness |
| | 5 kHz **+2 dB** Q 1.5 — attack |
| | 12 kHz **+2 dB** shelf — cymbal air |
| Dyn | **COMP** · thr **−20 dB** · **3:1** · attack 15 ms · release 120 ms · soft knee · **target 3–4 dB GR** · makeup +3 dB |
| Output | → **Bus 7 at −3 dB** |

> Flavour alternative: swap COMP for **F670** (Fairchild) on this group for more
> obvious glue. Set it for 2–3 dB of reduction and no more. COMP is the safer
> default; F670 is the better sound if you have time to set it properly.

---

## Step 4 — Bus 13 "BC VOX"

Currently named "Choir Bus", muted, and fed only by Vox 1–3. Expand it to the whole
vocal team.

### Sends into Bus 13 (post-fader)

| Ch | Name | Person | Send |
|---|---|---|---|
| 13 | Vox 1 | Marie | **0.0 dB** |
| 14 | Vox 2 | Dehil | 0.0 |
| 15 | Vox 3 | Gabby | 0.0 |
| 16 | Vox 4 | Peggy | 0.0 |
| 20 | LEAD2 | David | **+2.0** — lead vocal sits above the group |
| 22 | Raissa | Raissa | 0.0 |
| 24 | Wireless 3 | Elsie | 0.0 |
| 25 | Jude | Jude | 0.0 |
| 26 | Brenda | Brenda | 0.0 |
| 27 | Wireless 4 | Martha | 0.0 |

> **Verify this list.** I have inferred who sings and who speaks from the connector
> labels and the USB map. If "House" (ch 23) is a sung vocal rather than a house mic,
> move it in here. If any of the above only ever speak, move them to the speech group.

### Bus 13 processing

| Stage | Setting |
|---|---|
| Pre-insert | **FX11 → DE-S2** · 6.5–7 kHz · threshold for **3–4 dB reduction** on the loudest sibilance |
| EQ (STD) | 250 Hz **−3 dB** Q 2.0 — proximity mud across the group |
| | 500 Hz **−2 dB** Q 2.5 — boxiness |
| | 3 kHz **+2 dB** Q 1.5 — intelligibility |
| | 10 kHz **+2 dB** shelf — air |
| Dyn | **F670** (already the model on this bus) set for **3–4 dB GR** — or **COMP** thr −22, 3:1, attack 10 ms, release 100 ms |
| Output | → **Bus 7 at −2 dB** |

Group compression here is what makes a ten-person vocal team sound like one
instrument online. It is doing more work than any single channel compressor.

---

## Step 5 — Speech and the rest, direct to Bus 7

These already exist. Adjust the levels:

| Ch | Name | Current send | **Set to** | Why |
|---|---|---|---|---|
| 21 | Pastor Lapel | 0.0 | **+3.0** | Speech must be as loud as music online. Most churches get this wrong. |
| 23 | House | 0.0 | **+3.0** | If this is a speech mic |
| 33 | Kids Lapel | −10.0 | **−6.0** | And **name this channel** |
| 8 | Bass | −3.0 | **−2.0** | Phone speakers need the harmonic |
| 9 | E Gtr | −6.0 | −6.0 | keep |
| 10 | AC Gtr | −6.0 | **−5.0** | |
| 11 | Keys 1 | −4.0 | **−5.0** | Pads clutter a small speaker |
| 12 | Keys 2 | −4.0 | **−5.0** | |
| 17 | Sax | −6.0 | −6.0 | keep |
| 18 | LOOP | −6.0 | −6.0 | keep |
| 34 | PC Playback | −6.0 | −6.0 | keep |
| **29** | **Crowd 1** | *(direct to MX5)* | **Bus 7 at −12.0** | **Move it here** |
| **30** | **Crowd 2** | *(direct to MX5)* | **Bus 7 at −12.0** | **Move it here** |
| 19 | LEAD1 | — | — | Dead channel, no input source. Fix or disable (audit M3). |

### Crowd mic technique — the thing that makes this sound like a live church

| Moment | Crowd level relative to music |
|---|---|
| Pre-service | −18 dB |
| Worship — verse | −18 dB |
| **Worship — congregation singing** | **−10 to −12 dB** |
| Sermon | **−24 dB or muted** |
| Congregation responds ("Amen") | push briefly to −15 dB |
| **Prayer / altar / ministry** | **MUTED** |
| Post-service | −15 dB |

**Build a mute group for the crowd mics** (Mute Group 6, per the remediation plan).
Private prayer broadcast to the internet is a pastoral failure caused by an audio
decision. One button, every altar call.

### FX returns into Bus 7

Already wired at −3 dB from Bus 14, 15 and 16. Once unmuted, verify by ear — the
stream needs **more** reverb than the house, because the room's own acoustics do not
exist online. Expect to push these to about **−1 dB**.

---

## Step 6 — Bus 7 "BROADCAST" master

| Stage | Setting |
|---|---|
| Filter | **HPF 40 Hz, 24 dB/oct** — removes what no viewer's device can reproduce |
| EQ band 1 | 80 Hz **−2 dB** Q 1.0 — tighten; the room is not there to absorb it |
| EQ band 2 | **300 Hz −3 dB Q 1.5** — the single most important cut. This is what removes the "boxy laptop speaker" sound. |
| EQ band 3 | 1.2 kHz **+1.5 dB** Q 1.2 — presence on small speakers |
| EQ band 4 | 3.5 kHz **+2 dB** Q 1.5 — intelligibility |
| EQ band 5 | 8 kHz **+1.5 dB** shelf — air on headphones |
| EQ band 6 | 16 kHz **−2 dB** shelf — reduces encoder artifacts |
| Dyn | **SBUS** bus compressor · thr **−18 dB** · **2:1** · attack 30 ms · release auto · **target 2–4 dB GR** |
| Post-insert | **FX7 → C5-CMB** (see below) |
| Fader | 0 dB — drive the level from the sends, not the master |

> Use **PULSAR** for the bus EQ instead of STD if your firmware offers it on buses —
> it is the broader, more musical curve, and you already run it on Matrix 5.

### C5-CMB multiband — the Multipressor replacement

This is what keeps a stream consistent through the swing from a quiet prayer to a
full band. Set each band for **gentle** reduction; the goal is consistency, not
loudness.

| Band | Range | Ratio | Target GR | Controls |
|---|---|---|---|---|
| 1 | below ~120 Hz | 2.5:1 | 2–3 dB | Kick and bass energy — stops low end pumping the whole mix |
| 2 | ~120–500 Hz | 2:1 | 1–2 dB | Mud and boxiness |
| 3 | ~500 Hz–3 kHz | 2:1 | 2 dB | Body and vocal core |
| 4 | ~3–8 kHz | 2.5:1 | 2–3 dB | Presence and harshness |
| 5 | above ~8 kHz | 2:1 | 1–2 dB | Sibilance and cymbals |

Adjust the crossover points to whatever the unit actually offers. Makeup gain back to
unity — this stage should change the **consistency**, not the level.

**If any band shows more than 5 dB of reduction, something upstream is too hot.** Fix
it there, not here.

---

## Step 7 — Matrix 5 "STREAM" mastering

Mostly already built — this is the part of your console that was done well. Keep it.

| Stage | Setting |
|---|---|
| Source | **Bus 7 only.** Confirm `Main 1 → MX5` is off. |
| Input trim | Currently **+5.3 dB** — re-set after the chain above is in place. Aim for the EQ and dynamics to see a sensible level. |
| Pre-insert | **FX15 TAPE** — light drive only. This is warmth and glue, not distortion. |
| EQ | **PULSAR** — already on. Keep your settings; they look sensible (low boost at 30 Hz, high boost at 12 k, gentle 200 Hz / 2 k shaping). |
| Dyn | **ECL33** — already on. Limiter thr −1, comp thr −15, ratio 2, gain +3. Keep. |
| Post-insert | **FX16 LIMITER** — ceiling **−1.5 dBTP**, target 1–3 dB reduction on peaks only |
| **Delay** | **Enable.** Enter the measured lip-sync value. |
| Output | **LCL out 4 (L) and LCL out 5 (R)** → Osee |

### Level into the Osee

The WING outputs +4 dBu balanced. Most compact streaming switchers have −10 dBV
inputs — a 12 dB mismatch that will sound crunchy no matter what you do upstream.

1. Set the Matrix 5 **output trim to −12 dB**, or fit a −15/−20 dB inline pad
2. Set the Osee input to **Line**, not Mic
3. Adjust until the Osee meters read **−12 dB average, −6 dB peak** on loud worship
4. Turn **off** the switcher's own EQ, compressor and AGC
5. Turn **off** "audio follow video"
6. Record the trim value here: `_____ dB`

---

## Loudness targets

| Metric | Target |
|---|---|
| Integrated loudness | **−16 LUFS** |
| True peak | **−1.5 dBTP** |
| Short-term range | −18 to −14 LUFS |
| **Speech vs music** | **within 1 LU of each other** |

The WING has metering but no LUFS meter. Two options:

1. **Keep Logic as the meter.** It is still recording the multitrack anyway. Put a
   Loudness Meter on a track fed from the stream return and watch it. Costs nothing.
2. A phone app on the stream itself — less precise, but it measures what the viewer
   actually gets, including the encoder.

Speech being quieter than worship is the most common church stream complaint and it
is invisible without a meter.

---

## Gain-staging the whole chain

Work outward, in this order. Do not skip.

1. **Channel strips first.** Peaks at −10 dBFS, average around −18 dBFS.
2. **Group buses.** Bus 11 and Bus 13 faders at 0. Set their compressors for the
   target GR above and no more.
3. **Bus 7.** Fader at 0. Build the balance with the **send levels**. Bus 7's meter
   should average around −18 dBFS with peaks near −10.
4. **Matrix 5.** Set the input trim so the EQ and ECL33 see a sensible level. The
   final limiter should be idling, catching only occasional peaks.
5. **Output trim.** Set for the Osee, then never touch it again.

Every stage compresses a little. Cumulatively that is a lot. The rule: **channel
2–4 dB, group 3–4 dB, bus 2–4 dB, master limiter 1–3 dB.** If any stage is working
harder than that, the problem is upstream.

---

## Optional: dedicated broadcast channels

For the two sources where shared channel processing costs you the most, duplicate the
input onto a spare channel with broadcast-only processing.

You have four spare channels: **ch 28, 37, 38, 39** (all at −∞, no live routing).

| Spare ch | Patch to | Assign to | Processing |
|---|---|---|---|
| **37** | **A-25** (same input as ch 21, Pastor) | **Bus 7 only** — not Main 1 | Speech-optimised: HPF 120 Hz 18 dB/oct, comp **8 ms attack** 4:1 thr −24, 2.5 kHz **+4 dB**, DE-S2 if a slot frees up. Then mute ch 21's send to Bus 7. |
| **38** | **A-22** (same input as ch 20, LEAD2/David) | **Bus 7 only** | Broadcast vocal: more compression, more 3 kHz, more air than the house wants |

This gives the pastor and the lead vocal genuinely independent broadcast processing —
the thing you had in Logic — for two channels you were not using anyway.

Do this **after** the main build is working. It is a refinement, not a prerequisite.

---

## Labelling to fix while you are in here

| Item | Problem | Fix |
|---|---|---|
| **ch 40 "TB"** | Named talkback but sourced from **A-24, which is Crowd 2**. ch 32 is the real talkback (A-32). | Rename or clear. Anyone routing "TB" today would be routing a crowd mic. |
| **ch 39** | Muted duplicate of **A-23 (Crowd 1)** | Clear it, or use it as a spare broadcast channel |
| **ch 33** | Unnamed, live at −4 dB, feeding Bus 1 and Bus 7 | Name it **KIDS LAPEL** |
| **ch 3** | Named "HH", sourced from A-3 labelled "SNARE BTTM" | Walk to the stage and settle it |
| **ch 17 / 18** | Both from A-15, labelled "TRACK", named "Sax" and "LOOP" | Three names for one input |
| **ch 19 "LEAD1"** | No input source, but routed to Main 1 and Bus 9 | Patch it or disable it |

---

## Commissioning checklist

Work through this before the first live Sunday on the new path.

- [ ] Show file backed up before starting
- [ ] Bus 7 unmuted; `Main 1 → MX5` **off**
- [ ] Bus 11 BC DRUMS built and feeding Bus 7
- [ ] Bus 13 BC VOX renamed, unmuted, whole vocal team routed
- [ ] Buses 14 and 16 unmuted
- [ ] Crowd mics on Bus 7, stereo-linked, **still unassigned from Main 1**
- [ ] FX7 → C5-CMB on Bus 7; FX11 → DE-S2 on Bus 13
- [ ] MTX5 patched to LCL out 4/5 and physically wired to the Osee
- [ ] Osee input set to **Line**, its EQ/comp/AGC **off**, audio-follow-video **off**
- [ ] **Solo Bus 7 and listen for click, cues and talkback.** Nothing should be there.
- [ ] Listened on **headphones** and on a **phone speaker**
- [ ] Loudness verified near −16 LUFS, peaks under −1.5 dBTP
- [ ] Speech and worship loudness-matched — A/B a sermon clip against a chorus
- [ ] Lip-sync measured with the clap test and the MTX5 delay set
- [ ] Mute Group 6 (crowd) built and tested
- [ ] House PA verified **unchanged** — Main 1 and Matrix 1/2/3 must sound exactly as before
- [ ] Logic still recording multitrack, now with no live responsibility
- [ ] New show file exported to USB, the server, and this repository

---

## What this gets you

- One box. No Mac in the live path, no second clock, no Volt 276, no aggregate device.
- The template's processing philosophy intact — multiband, de-essing, group
  compression, tape, limiting — using better emulations than Logic's stock plugins.
- Crowd mics properly integrated, which is what makes a stream sound like a church
  rather than a rehearsal room.
- A mix a volunteer can run, because it follows the house mix with fixed offsets
  rather than needing a second operator.

Logic stays for what it is genuinely good at: recording 40 channels every week, and
letting you rehearse the mix mid-week with nobody in the building.
