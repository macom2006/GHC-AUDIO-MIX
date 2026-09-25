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
| Programming the console from scratch | `docs/01-system-overview.md` → then follow docs in order |
| Running Sunday service | `checklists/pre-service.md` |
| A new volunteer | `docs/15-volunteer-training.md` |
| Troubleshooting mid-service | `docs/14-troubleshooting.md` |
| Fixing the stream audio | `docs/07-broadcast-mix.md` |

## Document index

| # | Document | What it covers |
|---|---|---|
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
| A1 | [X32/M32 mapping](docs/appendix-x32-m32-mapping.md) | If the desk is actually an X32, not a WING |

Machine-readable patch data: [`patch/input-patch.csv`](patch/input-patch.csv),
[`patch/output-patch.csv`](patch/output-patch.csv)

---

## Assumptions I made (correct these and I will revise)

This repository was empty, so there were no existing settings to audit. Everything
here is designed from scratch against a standard contemporary-worship template. I
have assumed:

1. **Console:** Behringer **WING** (full-size). There is no product called a
   "WING 32" — the family is WING / WING Compact / WING Rack, all sharing the same
   48-channel DSP engine, so this document applies to any of them. If you actually
   have an **X32/M32**, read `docs/appendix-x32-m32-mapping.md` first — the
   architecture changes materially.
2. **Stage box:** one 32-in/16-out box on AES50-A (S32, SD16 pair, or DL32).
3. **Band:** drums, bass, electric guitar, acoustic guitar, keys, playback tracks
   with click and cues, worship leader + 3 BGVs.
4. **Speech:** pastor's headset (primary), handheld wireless ×2, lectern mic.
5. **Monitors:** in-ear monitoring for the band, two wedges for stage/pulpit.
6. **DAW:** Logic Pro on a Mac connected to the WING over USB-B (48×48 @ 48 kHz).
7. **Video:** Osee switcher with built-in streaming, audio fed in from the console.
8. **Room:** single auditorium, main PA plus subs, lobby and nursery feeds.

## What I need from you to finalize

Minimum information required — everything else I can hold as a sensible default:

- Exact console model and firmware version
- Stage box model(s) and count
- PA make/model (mains, subs, fills) and whether there is an external DSP
- Actual instrument and vocal lineup, and wireless mic models
- Whether you stream **from the Osee** or from **OBS on a computer**
- Room dimensions and approximate seating capacity

---

*Maintained for Graceland Harvest Church. Update this file whenever the system changes.*
