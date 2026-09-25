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
| A1 | [X32/M32 mapping](docs/appendix-x32-m32-mapping.md) | If the desk is actually an X32, not a WING |

**As-built data**, parsed from the live console file:
[`patch/as-built-channels.csv`](patch/as-built-channels.csv) ·
[`patch/as-built-outputs.csv`](patch/as-built-outputs.csv)

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
| Stream | Matrix 5 "STREAM", full mastering chain built, **not patched to any output** (see audit C3) |

## The one question I need answered

**How does the Osee actually get audio today?** The snapshot shows Matrix 5
"STREAM" patched to nothing, Bus 7 "BROADCAST" muted, and the USB outputs carrying
a near-silent bus. So the audio reaching your stream is coming from somewhere the
console file does not explain — most likely a PA leg on a local output, or an
external system on the MADI card. Confirm which, and Stage 2 of the remediation
plan can be completed.

Secondary, useful but not blocking:

- PA make/model, and whether there is an external DSP downstream of Matrix 1/2/3
- What the MADI card connects to, and who operates it
- Whether ch 3 (A-3) is a hi-hat or a snare bottom mic
- What A-15 actually is — it is labelled "TRACK" and feeds channels named "Sax" and "LOOP"
- Room dimensions and seating capacity

---

*Maintained for Graceland Harvest Church. Update this file whenever the system changes.*
