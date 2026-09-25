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
| **Loading the new console file** | **`console/IMPLEMENTATION.md`** — the printable step-by-step, 90 minutes at the desk |
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
| 10 | [Logic Pro](docs/10-logic-pro.md) | Multitrack recording + virtual soundcheck |
| 11 | [Osee video integration](docs/11-osee-video-integration.md) | Audio embed, levels, lip-sync |
| 12 | [Scenes & snapshots](docs/12-scenes-snapshots.md) | The show file, scope and safes |
| 13 | [Service run sheet](docs/13-service-runsheet.md) | Minute-by-minute operating procedure |
| 14 | [Troubleshooting](docs/14-troubleshooting.md) | Fast diagnosis under pressure |
| 15 | [Volunteer training](docs/15-volunteer-training.md) | Three-tier competency path |
| **16** | **[Remediation plan](docs/16-remediation-plan.md)** | **Ordered fix list for the current console, stage by stage** |
| **17** | **[Logic Pro broadcast rig](docs/17-logic-broadcast-rig.md)** | How the stream was built in Logic, and why it is being retired |
| **18** | **[WING broadcast build](docs/18-wing-broadcast-build.md)** | The broadcast mix rebuilt natively on the WING, step by step |
| **19** | **[Plan of record](docs/19-plan-of-record.md)** | Every decision closed, five phases, in build order |
| **20** | **[What changed in the console file](docs/20-what-changed.md)** | **THE FILE — `console/GHC BROADCAST V1.snap`, ready to load, with all 101 changes itemised** |
| **21** | [Stem measurements](docs/21-stem-measurements.md) | Measured analysis of the template's reference stems, and what it confirms |
| A1 | [X32/M32 mapping](docs/appendix-x32-m32-mapping.md) | If the desk is actually an X32, not a WING |

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
| DAW | Logic Pro — **multitrack recording and virtual soundcheck only** once doc 18 is built. No live dependency on the Mac. |
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
