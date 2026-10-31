# GHC Audio — Graceland Harvest Church Sound System Configuration

The complete, pre-programmed mix specification for Graceland Harvest Church:
**Behringer WING** console → **house PA** and **broadcast/stream**, with
**Logic Pro** multitrack + virtual soundcheck and an **Osee** video switcher.

This repository is the single source of truth for the sound system. If a setting
is changed on the console, it gets changed here too. If it isn't written here,
it isn't approved.

---

## Start here

| If you are... | Read this |
|---|---|
| **Fixing the current console** | **`docs/00-audit-2026-03-18.md` → then `docs/16-remediation-plan.md`** |
| **Feedback on monitors or mains** | **`docs/27-feedback-live-analysis.md`** — current state; then docs 22 and 23 for the underlying cause |
| P16 / in-ear monitoring | `docs/23-p16-ultranet.md` and `docs/24-p16-bank-b.md` |
| Stream sounds mono, or distorted | `docs/25-osee-gostream-settings.md` |
| **Hum or buzz on the stream** | **`docs/26-hum-and-clipping-fix.md`** |
| Loading the new console file | `console/IMPLEMENTATION.md` — the printable step-by-step, 90 minutes at the desk |
| Understanding what the file changed | `docs/20-what-changed.md` |
| Anything at all | `docs/19-plan-of-record.md` — the decisions, and the order to do them in |
| Building the stream mix | `docs/18-wing-broadcast-build.md` |
| Programming the console from scratch | `docs/01-system-overview.md` → then follow docs in order |
| Running Sunday service | `checklists/pre-service.md` |
| A new volunteer | `docs/15-volunteer-training.md` |
| Troubleshooting mid-service | `docs/14-troubleshooting.md` |
| Fixing the stream audio | `docs/07-broadcast-mix.md` |

## Document index

| # | Document | What it covers |
|---|---|---|
| **00** | **[Console audit](docs/00-audit-2026-03-18.md)** | **What your live console actually does today, and what is wrong with it** |
| 01 | [System overview](docs/01-system-overview.md) | Design philosophy, hardware inventory, the dual-mix principle |
| 02 | [Signal flow](docs/02-signal-flow.md) | End-to-end block diagram, clocking, latency budget |
| 03 | [Input & output patch](docs/03-patch.md) | Every physical connector, every channel |
| 04 | [Channel settings](docs/04-channel-settings.md) | Gain, HPF, gate, EQ, compression — per source |
| 05 | [Buses, DCAs & matrices](docs/05-buses-dcas-matrices.md) | Console architecture and naming |
| 06 | [House mix](docs/06-house-mix.md) | PA tuning, SPL targets, aux-fed subs |
| 07 | [Broadcast mix](docs/07-broadcast-mix.md) | The online mix, loudness targets, mastering chain |
| 08 | [Monitors & IEMs](docs/08-monitors-iem.md) | Stage mixes, wedges, feedback control |
| 09 | [FX rack](docs/09-fx-rack.md) | Reverbs, delays, and where they live |
| 10 | [Logic Pro](docs/10-logic-pro.md) | *Superseded by doc 30* — Logic is out of the system |
| 11 | [Osee video integration](docs/11-osee-video-integration.md) | Audio embed, levels, lip-sync |
| 12 | [Scenes & snapshots](docs/12-scenes-snapshots.md) | The show file, scope and safes |
| 13 | [Service run sheet](docs/13-service-runsheet.md) | Minute-by-minute operating procedure |
| 14 | [Troubleshooting](docs/14-troubleshooting.md) | Fast diagnosis under pressure |
| 15 | [Volunteer training](docs/15-volunteer-training.md) | Three-tier competency path |
| **16** | **[Remediation plan](docs/16-remediation-plan.md)** | **Ordered fix list for the current console, stage by stage** |
| **17** | **[Logic Pro broadcast rig](docs/17-logic-broadcast-rig.md)** | How the stream was built in Logic, and why it is being retired |
| **18** | **[WING broadcast build](docs/18-wing-broadcast-build.md)** | The broadcast mix rebuilt natively on the WING, step by step |
| **19** | **[Plan of record](docs/19-plan-of-record.md)** | Every decision closed, five phases, in build order |
| **20** | **[What changed in the console file](docs/20-what-changed.md)** | **THE FILE — `console/GHC BROADCAST V9.snap` — current, built on the V5 in service** |
| **21** | [Stem measurements](docs/21-stem-measurements.md) | Measured analysis of the template's reference stems, and what it confirms |
| **22** | **[Feedback: diagnosis and cure](docs/22-feedback-diagnosis.md)** | **Why the monitors and mains ring, and the four fixes in order of effect** |
| **23** | **[P16 Ultranet monitoring](docs/23-p16-ultranet.md)** | The 16 personal-mixer channels, and why seven singers are missing from them |
| **24** | **[P16 Bank B](docs/24-p16-bank-b.md)** | The second Ultranet feed — implemented in V3, plug-and-play when the box arrives |
| **25** | [Osee GoStream settings](docs/25-osee-gostream-settings.md) | Correct audio settings on the switcher — stereo, and stopping the clipping |
| **26** | [Ground hum and clipping](docs/26-hum-and-clipping-fix.md) | Resolved — Matrix 5 at −30.5 dB. Diagnosis, and why the DI boxes are now optional |
| **27** | **[Feedback: live file analysis](docs/27-feedback-live-analysis.md)** | **The spiral in the operators' own edits, and the 90 minutes that fixes it** |
| **28** | [Computer audio fix](docs/28-computer-audio-fix.md) | Duplicate paths, an empty DCA, the wrong USB port, and the missing sub send |
| **29** | [Computer audio dropouts](docs/29-pc-audio-dropouts.md) | Why it cut intermittently — resolved by moving playback to analog in V6 |
| **30** | **[Recording without Logic](docs/30-recording-without-logic.md)** | **Console SD recording, virtual soundcheck from the card, and PC playback on analog** |
| **31** | [House mic feedback](docs/31-house-mic-feedback.md) | Octave-wide cuts that never worked, a slow compressor, and the ring-out that is still owed |
| **32** | [Copilot file review](docs/32-copilot-file-review.md) | Why not to load it, what it got right, and the three-point check before loading any file |
| **33** | **[Stream EQ and comfort](docs/33-stream-eq-and-comfort.md)** | **+8 dB of stacked treble, a limiter used as a maximiser, and gain staging the wrong way round** |
| **34** | [Recording measurement](docs/34-recording-measurement.md) | Measured analysis of an actual clip: −12.5 LUFS, clipping at +0.1 dBTP, stereo confirmed working |
| **35** | **[Live OSC control](docs/35-wing-osc-control.md)** | **Corrected WING address map, a read-only verifier, and the six-step sequence** |
| **36** | **[Singer shout control](docs/36-singer-shout-control.md)** | **Dehil, Elsie and Peggy: quieter but more audible — V10** |
| **37** | **[Pastor's mic levelling](docs/37-pastor-mic-levelling.md)** | **Steady when soft, still alive when he lifts — V11** |
| **38** | **[Stream vocal level](docs/38-stream-vocal-level.md)** | **The one fader that lowers stream vocals without touching FOH** |
| **39** | **[Bullhorn correction](docs/39-bullhorn-correction.md)** | **V10's narrow-Q error measured and undone — V12** |
| **40** | **[BC BAND stream fader](docs/40-bc-band-stream-fader.md)** | **One fader for the band on the stream — V13** |
| **41** | **[Stream master chain](docs/41-stream-master-chain.md)** | **Six compressors found in series; balance set — V14** |
| **42** | **[Vocalist wedge mix](docs/42-vocalist-wedge-mix.md)** | **Vocals, a little keys, drums for tempo — V15, corrected in V16** |
| **43** | **[System status run-down](docs/43-system-status.md)** | **Full audit of stream, wedges, FOH and P16 against V16 — start here** |
| — | [`tools/coupling_check.py`](tools/coupling_check.py) | Run before shipping any snapshot: finds dead-end buses, shared faders, wet/dry drift, duplicate inputs, wrong labels |
| — | **[Ring-out procedure](checklists/ring-out-procedure.md)** | **Printable step-by-step for ringing out the wedges and mains, with a notch log** |
| A1 | [X32/M32 mapping](docs/appendix-x32-m32-mapping.md) | If the desk is actually an X32, not a WING |

**Tools:** [`tools/WING-OSC-REFERENCE.md`](tools/WING-OSC-REFERENCE.md) ·
[`tools/wing-osc-map.json`](tools/wing-osc-map.json) ·
[`tools/wing_probe.py`](tools/wing_probe.py) ·
[`tools/wing-tools.ts`](tools/wing-tools.ts)

**As-built data**, parsed from the live console file:
[`patch/as-built-channels.csv`](patch/as-built-channels.csv) ·
[`patch/as-built-outputs.csv`](patch/as-built-outputs.csv) ·
[`patch/wing-usb-to-logic-map.csv`](patch/wing-usb-to-logic-map.csv)

**Target-state patch**, proposed in docs 01–15:
[`patch/input-patch.csv`](patch/input-patch.csv) ·
[`patch/output-patch.csv`](patch/output-patch.csv)

---

## As-built vs. target state — read this before using docs 01–15

There are two layers of documentation in this repository, and they are not the same
thing.

| Layer | What it is | Files |
|---|---|---|
| **As-built** | What the GRACELAND console actually does today, read directly out of the snapshot `TONY GHC MARCH 2026 PMAMB0.snap` (2026-03-18) | `docs/00-audit-2026-03-18.md`, `patch/as-built-*.csv` |
| **Target state** | The system design we are working toward | `docs/01-15`, `patch/input-patch.csv`, `patch/output-patch.csv` |
| **The bridge** | How to get from one to the other, in order | `docs/16-remediation-plan.md` |

Docs 01–15 were written before the console file was available. Their **principles,
targets and processing values apply as-is** — gain structure, SPL and LUFS targets,
the dual-mix philosophy, aux-fed subs, feedback procedure, scene safes, broadcast
offsets. Their **channel numbers and patch layout do not** — those describe a
proposed 48-channel layout, while your console runs 40 channels with a different
patch and a people-based naming convention.

When the two disagree about *where something is*, the as-built files are correct.
When they disagree about *how something should be set*, the target-state docs are
the standard we are moving to.

## Confirmed system facts

Read from the console file, not assumed:

| | |
|---|---|
| Console | Behringer **WING full-size**, serial `S240100078BV2`, named **GRACELAND** |
| Firmware | 3.1-0 (release) |
| Clock | 48 kHz, internal — correct |
| USB | 48×48 |
| Stage I/O | 32 inputs on AES50-A, plus 8 local mic inputs |
| Expansion | **WING-MADI** card (SFP1 mode) — feeds an external system and returns "AL FOH" / "AL BCAST" |
| Recording | WING-LIVE SD, 32 tracks per slot; 2-track 24-bit off Main 1 |
| Channels in use | 40 |
| PA | Three zones — Matrix 1 "PA L", Matrix 2 "PA C", Matrix 3 "PA R", each delayed and GEQ'd |
| Subs | Matrix 4, mono, **fed the full house mix** (see audit C5) |
| Stream | **Moving to WING-native** — Bus 7 → Matrix 5 → LCL out 4/5 → Osee. See doc 18. Previously built in Logic Pro out via a Volt 276 (doc 17), now being retired from the live path. |
| Recording | **Console WING-LIVE SD, 32 tracks** — no computer. Cards not yet fitted. See doc 30. |
| Channels | 40 mono input channels + 8 aux (WING's actual architecture) |

## Open items

The broadcast path is decided: **WING-native, Logic out of the live chain.** The
build is `docs/18-wing-broadcast-build.md`. What still needs confirming:

- **Who sings and who speaks.** Doc 18 step 4 assumes ch 13–16, 20, 22, 24–27 are
  the vocal team and ch 21, 23, 33 are speech. Correct me if "House" (ch 23) is a
  sung vocal, or if any of the wireless channels only ever speak.
- **What is `MACH4`?** It is loaded in FX7 on the Kids Lapel channel and I cannot
  identify it from the file. Doc 18 reclaims that slot for the broadcast multiband —
  check what it is before overwriting it.
- **Verify every Logic track's input assignment** against
  `patch/wing-usb-to-logic-map.csv`, for the recording session that remains.
- **Is ch 3 (A-3) a hi-hat or a snare bottom mic?** The connector says one, the
  channel says the other.
- **What is A-15?** It is labelled "TRACK" and feeds channels named "Sax" and "LOOP".
- PA make/model, and whether there is an external DSP after Matrix 1/2/3
- What the MADI card connects to, and who operates it
- Room dimensions and seating capacity

---

*Maintained for Graceland Harvest Church. Update this file whenever the system changes.*
