# 19 — Plan of Record

**Every open decision, closed. This is the build order. Work it top to bottom.**

Where earlier documents offered alternatives, this one chooses. If another document
disagrees with this one, this one wins.

---

## Where you actually stand

| | |
|---|---|
| **Your equipment** | Genuinely strong. WING full-size, 32-channel stage box, L/C/R PA with per-leg delay and graphic EQ, subs, crowd mics, MADI split, premium FX rack, 40 channels in use. This is better hardware than most churches your size own. |
| **Your house mix** | Competent. Properly high-passed, sensibly compressed, PA time-aligned. It works. |
| **Your broadcast mix** | Currently a Logic session on a Mac with a clock fault, a single point of failure, and no meter. |
| **Your console configuration** | Half-finished in several places, with no scene safes at all. |

**So: strong bones, unfinished build.** The gap between where you are and a
best-in-class system is about **five working sessions**, not new equipment. You do
not need to buy anything.

The one honest caveat: none of this has been dialled into the desk yet. Do not treat
the documentation as the system.

---

## The decisions, made

You asked me to decide. Here is every open question closed.

| # | Question | **Decision** | Reasoning |
|---|---|---|---|
| 1 | Logic or WING for the stream? | **WING.** Logic keeps recording and virtual soundcheck only. | One box, one clock, no Mac in the live path |
| 2 | Bus 7 or Main 2 for the broadcast master? | **Bus 7.** | It is already named, already fed by 20 channels, already routed to Matrix 5. Rebuilding on Main 2 would be cleaner in theory and slower in practice. Use what is built. |
| 3 | Pre- or post-fader sends to the broadcast bus? | **Post-fader.** | A fully independent mix needs a second operator all service. Post-fader with fixed offsets is the more reliable product for a volunteer desk. |
| 4 | Reclaim FX7 (MACH4) and FX11 (GEQ)? | **Yes, both.** | A premium processor and a 31-band graphic on a kids' lapel mic is not a defensible use of two of sixteen slots. If MACH4 turns out to matter, reload it later in place of SPKMAN on the monitor bus. |
| 5 | Is ch 23 "House" speech or vocal? | **Treat as speech.** | Routed with the speech group. Correct me if it sings. |
| 6 | Dedicated broadcast channels for pastor and lead vocal? | **Yes — Phase 4.** | You have four unused channels. This recovers the independent processing you had in Logic, for the two sources it matters on. |
| 7 | What is the emergency feed if the broadcast chain fails? | **Main 1, the house mix, to a second Osee input.** | Free, always live, one button on the switcher. Not as good as the broadcast mix — good enough that the service continues. |
| 8 | Aux-fed subs? | **Yes — Phase 2, Bus 11's sibling.** | The single largest audible improvement available to you in the room. |
| 9 | Automix? | **Yes, group X, speech only.** | Nine speech-capable channels is well past where manual management works. |
| 10 | LCR centre-cluster weighting for speech? | **Phase 5, optional.** | Real gain, real risk. Only with a measurement mic and time. |

---

## Phase 1 — Make the console safe

**~1 hour. Do this before anything else, including before the next service.**

Nothing else is worth building on a console where a scene recall can rewrite every
preamp gain and every in-ear mix. Today, yours can.

1. Export the show file to USB and the server. Name it `GHC-PRE-REBUILD`.
2. Set scene safes per `16-remediation-plan.md` Stage 1 — all preamp sources, all
   output patching, Buses 1/8/9, Matrices 1–5, Main 1 master, ch 21 mute.
3. **Test the safes**: change a gain, pull a monitor bus, recall a scene, confirm
   they did not move.
4. Name ch 33 (`KIDS LAPEL`). Clear ch 19, 28, 37, 38, 39, 40.
5. Settle ch 3 — hi-hat or snare bottom. Walk to the stage and look.

**Done when:** a scene recall changes the mix and nothing else.

---

## Phase 2 — Fix the room

**~1.5 hours. This is the phase the congregation will notice.**

1. **Aux-fed subs.** Turn off `Main 1 → MX4`. Name a free bus `SUB FEED`, mono, feed
   Matrix 4 from it. Send only kick, floor tom, bass, and tracks — nothing else.
   Details in `06-house-mix.md` and `16-remediation-plan.md` Stage 3.
2. Set Matrix 4's LPF to your crossover (90 Hz, 24 dB/oct) and a 30 Hz HPF.
3. Align the subs to the mains — polarity first, then delay.
4. Walk the room during a full-band song. Front, back, sides, under any balcony.

**Done when:** the pastor's voice no longer rumbles the room, and the kick has
definition instead of boom.

---

## Phase 3 — Build the broadcast mix on the WING

**~2 hours. Follow `18-wing-broadcast-build.md` exactly.**

1. Unmute Bus 7. Turn off `Main 1 → MX5`.
2. Build Bus 11 `BC DRUMS` and Bus 13 `BC VOX`.
3. Reassign FX7 → C5-CMB on Bus 7, FX11 → DE-S2 on Bus 13.
4. Move the crowd mics onto Bus 7 and stereo-link them.
5. Set the Bus 7 master EQ, SBUS compressor and multiband.
6. Patch Matrix 5 → LCL out 4/5 → Osee. Set the output trim for the switcher.
7. **Patch Main 1 → two more outputs → a second Osee input.** Label it
   `EMERGENCY AUDIO`. Test it.
8. Clap test. Set the Matrix 5 delay.

**Done when:** the stream sounds right on a phone speaker, and you can switch to the
emergency feed and back in under five seconds.

---

## Phase 4 — Make it operable by a volunteer

**~1.5 hours. This is what makes it survive you being away.**

1. **Mute groups.** MG1 Band, MG2 Vox, MG3 Speech, MG4 Media, **MG6 Crowd**.
2. **DCA 10 = SPEECH.** The pastor and every speech channel. The most important
   fader during the sermon currently does not exist.
3. **Automix group X** on the speech channels only. Pastor at weight 0.
4. **Talkback** — enable destinations. It is assigned to a channel and routed
   nowhere.
5. **Virtual soundcheck** — set every channel's Alt Source to its USB return. The
   groundwork is already done and unused.
6. **Dedicated broadcast channels**: ch 37 ← A-25 (Pastor), ch 38 ← A-22 (lead
   vocal), both to Bus 7 only, with broadcast-specific processing.
7. Build the custom fader layer: SPEECH, VOX, BGV, DRUMS, BASS, GUITARS, KEYS,
   TRACKS, FX, CROWD, MEDIA, BAND.

**Done when:** a Tier 2 volunteer can run a full service from one fader layer.

---

## Phase 5 — Refinement, ongoing

Only after Phases 1–4 are live and stable.

1. Kick gate release 400 ms → 200 ms. Kick EQ cuts eased from −15 dB to −8 dB, A/B it.
2. Pastor compressor attack 30 ms → 8 ms.
3. Resolve the duplicate FX return paths (Buses 14/15 and Aux 1–4 both return).
4. LUFS metering on the stream — via Logic, or a phone app on the actual stream.
5. **Optional, advanced: LCR speech weighting.** Your Matrix 2 "PA C" currently gets
   a sum of the house mix. Feeding the centre cluster a speech- and lead-vocal-
   weighted mix instead is the classic large-room intelligibility technique. It is a
   real improvement and a real risk. Do it with a measurement mic and an empty room,
   never on a Saturday.

---

## What "best" actually means here

Not the most processing. Three things, in this order:

**1. It survives the operator.**
A system a substitute can run on a Sunday morning without you is worth more than a
system that sounds 5% better with you at the desk. Scene safes, mute groups, a
speech DCA, named channels, a printed checklist. That is Phases 1 and 4, and they
matter more than any EQ curve in this repository.

**2. The message gets through.**
Speech intelligibility in the room, speech loudness online. The congregation
forgives a rough guitar tone. Nobody forgives not hearing the sermon. That is the
speech DCA, the automix, the 2.5 kHz band, and the +3 dB broadcast offset.

**3. Nothing takes the service off the air.**
No single box failure should stop the service or the stream. After Phase 3 the Mac
can die and nothing happens; the console can lose the broadcast chain and one button
on the Osee recovers it.

Everything else — the multiband, the tape stage, the reverb choices — is the last
10%. Worth having. Worth nothing if the first three are missing.

---

## The standing weekly rhythm

Once Phases 1–4 are in:

| When | What |
|---|---|
| **Mid-week, 1 hour** | Virtual soundcheck. Play last Sunday back, refine the mix, train a volunteer. This is the single highest-return hour in the week. |
| **Sunday, T−90 to T−15** | The checklist in `checklists/pre-service.md`. No shortcuts. |
| **Sunday, post-service** | Back up the recording before leaving the building. Fill in the service log. |
| **Monthly** | Export the show file to three places. Test the emergency Osee feed. Read the service log and act on any pattern. |

A team that rehearses its mix mid-week sounds dramatically better than one that only
ever mixes live under pressure. That is the difference, more than any setting in
these documents.

---

## Honest assessment

**After Phase 3** you will have an in-house and broadcast system that stands
comparison with churches many times your size. The L/C/R PA with per-leg alignment,
crowd mics properly integrated into a separate broadcast mix, multiband on the
stream, 40-channel multitrack every week — that is not a small-church setup.

**After Phase 4** you will have something rarer: a system that keeps working when
the person who built it is not in the building.

**What would still separate you from a genuinely large operation** is not the console.
It is room acoustics, a second trained operator, and a dedicated broadcast operator
on the weeks that warrant one. If reverberation time in the auditorium is over about
1.5 seconds, no console work will fix intelligibility — absorption on the rear wall
and ceiling will, permanently, for every service. That is the next real investment,
and it is a building project, not an audio purchase.
