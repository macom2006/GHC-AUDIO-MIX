# 20 — What Changed in `GHC BROADCAST V1.snap`

**The file:** [`../console/GHC BROADCAST V1.snap`](../console/GHC%20BROADCAST%20V1.snap)

Built directly from your own snapshot `TONY GHC MARCH 2026 PMAMB0.snap`, so
everything I did not deliberately change is **byte-identical to your console**.
**101 changes** in total.

---

## READ THIS BEFORE YOU LOAD IT

### 1. This is built on your MARCH 2026 snapshot

If anyone has changed the console since 18 March — new gain, a new patch, a tweaked
monitor mix — **loading this file reverts those changes.** It is now late September.

**Before loading:** save your current state as its own show file. Then load this,
compare, and if something you needed has gone backwards, take the change list below
and apply it by hand to your current state instead. Either route works; the list is
the real deliverable, the file is the convenience.

### 2. Save your current show first

`Setup → Show → Save As` → `GHC-PRE-BROADCAST-V1`. To USB **and** the server. If
anything about this file is wrong, that is your one-click way back.

### 3. Load it mid-week, never on a Sunday

Then run a full band rehearsal through it before it sees a congregation.

---

## What is NOT in this file

Four things cannot be written into a snapshot safely, or at all. They stay manual.

| Item | Why | Time |
|---|---|---|
| **Scene safes** | The safes block uses an opaque string encoding I will not guess at. Getting it wrong could corrupt your show file. | 20 min on the console UI — `16-remediation-plan.md` Stage 1. **Still the highest-priority job on the desk.** |
| **Automix** | Per-channel automix membership is not carried in the snapshot format | 10 min — group X, speech channels only |
| **Lip-sync delay** | Has to be measured against your actual video chain. A wrong delay is worse than none, so I left Matrix 5's delay **off**. | 20 min — clap test, `11-osee-video-integration.md` |
| **Osee output trim** | Has to be set against the switcher's own meters | 10 min — `18-wing-broadcast-build.md` Step 7 |

**DCA and mute-group membership** *is* written (via the channel tag field, following
the pattern your console already uses) — but verify it on the desk after loading.
That encoding is inferred, not documented.

---

## What the house will sound like

Everything that makes the room sound the way it does today is untouched, and I
verified it field by field:

| Verified unchanged | |
|---|---|
| Every preamp gain, phantom and polarity setting | PASS |
| Every channel fader | PASS |
| Every channel EQ, gate, compressor and filter | PASS |
| Every monitor bus level and mute | PASS |
| Every monitor send from every channel | PASS *(one exception: ch19 LEAD1, a dead channel with no input source, unrouted)* |
| PA L/C/R matrix EQ and delays (13.1 / 10.1 / 7.1 ms) | PASS |
| Main 1 master fader and EQ | PASS |
| Clock: 48 kHz internal, USB 48/48 | PASS |

**One deliberate exception: the subwoofers.** Matrix 4 was fed the full house mix; it
is now aux-fed from Bus 11 (kick, floor tom, bass, keys, tracks only). This is the
one change the congregation will hear, and it is the largest single improvement
available to you. Matrix 4's own EQ and crossover are untouched — only its source
changed. **Expect to re-set the sub level by ear**, because it is now being fed far
less material.

If you want to try the file without that change: turn `Main 1 → MTX4` back on and
`Bus 11 → MTX4` off. Two switches, and the subs behave exactly as before.

---

## The new signal path

```
ch 1-7    Drums        ──POST──┐
ch 8-12, 17, 18  Band  ──POST──┤
ch 21, 23, 33   Speech ──POST──┤
ch 29, 30   Crowd      ──POST──┼──►  Bus 7 "BROADCAST"  ──► MTX 5 "STREAM" ──► LCL 4/5 ──► OSEE
ch 13-16, 20, 22,               │     EQ + COMP 2:1          TAPE → PULSAR
   24-27  Singers ──► Bus 13 ───┤     + FX7 C5-CMB           → ECL33 → LIMITER
              "BC VOX"          │       multiband
              DE-S2 + F670      │
Bus 14/15/16  FX returns ───────┘

ch 1, 6, 8, 11, 12, 17, 18 ──► Bus 11 "SUB FEED" ──► MTX 4 ──► SUBS

Main 1 (house) ──► LCL 2/3 ──► OSEE input 2  "EMERGENCY AUDIO"
```

---

## First power-up checklist

In this order:

1. Load the file. **House PA first** — play something familiar and confirm the room
   sounds right. Reset the sub level.
2. Solo **Bus 7**. You should hear a full mix — drums, band, vocals, speech, crowd.
3. Solo **Matrix 5**. Same mix, mastered.
4. Confirm audio at **LCL out 4 and 5** with a meter or headphones.
5. Wire LCL 4/5 to the Osee. Set the input to **Line**. Set the output trim for
   −12 dB average on the switcher's meters.
6. Wire LCL 2/3 to a second Osee input. Label it **EMERGENCY AUDIO**. Test the switch.
7. Clap test → set the Matrix 5 delay.
8. Listen to the stream on **earbuds** and on a **phone speaker**.
9. Set the scene safes. Do not skip this.

---

## Every change, itemised

### BUS  (10)

| Item | Was | Now |
|---|---|---|
| Bus 7 name | `BROADCAST` | **BROADCAST** |
| Bus 7 mute | `True` | **False** |
| Bus 7 fader | `0.0` | **0.0** |
| Bus 13 name | `Choir Bus` | **BC VOX** |
| Bus 13 mute | `True` | **False** |
| Bus 13 fader | `-7.4` | **0.0** |
| Bus 14 Inst Verb | `MUTED` | **unmuted** |
| Bus 16 Slap | `MUTED` | **unmuted** |
| Bus 11 name | `''` | **SUB FEED** |
| Bus 11 fader | `-144.0` | **0.0** |

### BUS EQ  (2)

| Item | Was | Now |
|---|---|---|
| Bus 7 BROADCAST | `+2@90 -4@120 -1.5@250 +1@2k -2@5k -4@9k` | **-2@80shelf -1.5@120 -3@300 +1.5@1.2k +2@3.5k +1.5@8kshelf** |
| Bus 13 BC VOX | `(unset)` | **-3@250 -2@500 +2@3k +2@10k shelf** |

### BUS DYN  (2)

| Item | Was | Now |
|---|---|---|
| Bus 7 compressor | `COMP thr-20 2.5:1 att25` | **COMP thr-18 2:1 att30 rel150  (target 2-4 dB GR)** |
| Bus 13 BC VOX | `F670 (was muted bus)` | **F670 enabled, set for 3-4 dB GR by ear** |

### INSERT  (3)

| Item | Was | Now |
|---|---|---|
| Bus 7 post-insert | `none` | **FX7 = C5-CMB multiband** |
| Bus 13 pre-insert | `none` | **FX11 = DE-S2 de-esser** |
| ch33 inserts | `FX7 + FX11 on a lapel mic` | **cleared - slots reclaimed** |

### ROUTING  (2)

| Item | Was | Now |
|---|---|---|
| Main 1 -> MTX5 (STREAM) | `ON -0.02 post-fader` | **OFF** |
| Main 1 -> MTX4 (SUBS) | `ON 0.0 (full house mix)` | **OFF** |

### BUS SEND  (5)

| Item | Was | Now |
|---|---|---|
| Bus 13 -> 7 | `on=True lvl=-3.0` | **on=True lvl=-2.0** |
| Bus 14 -> 7 | `on=True lvl=-3.0` | **on=True lvl=-1.0** |
| Bus 15 -> 7 | `on=True lvl=-3.0` | **on=True lvl=-1.0** |
| Bus 16 -> 7 | `on=False lvl=-144.0` | **on=True lvl=-1.0** |
| Bus 11 -> MX4 | `on=False lvl=-144.0` | **on=True lvl=0.0** |

### CH SEND  (45)

| Item | Was | Now |
|---|---|---|
| ch13 -> Bus 13 | `on=True lvl=-7.8 POST` | **on=True lvl=0.0 POST** |
| ch13 -> Bus 7 | `on=True lvl=0.0 POST` | **on=False lvl=-144.0 POST** |
| ch14 -> Bus 13 | `on=True lvl=-8.4 POST` | **on=True lvl=0.0 POST** |
| ch14 -> Bus 7 | `on=True lvl=0.0 POST` | **on=False lvl=-144.0 POST** |
| ch15 -> Bus 13 | `on=True lvl=-8.3 POST` | **on=True lvl=0.0 POST** |
| ch15 -> Bus 7 | `on=True lvl=0.0 POST` | **on=False lvl=-144.0 POST** |
| ch16 -> Bus 13 | `on=False lvl=-19.5 PRE` | **on=True lvl=0.0 POST** |
| ch16 -> Bus 7 | `on=True lvl=0.0 POST` | **on=False lvl=-144.0 POST** |
| ch20 -> Bus 13 | `on=False lvl=-144.0 PRE` | **on=True lvl=2.0 POST** |
| ch22 -> Bus 13 | `on=True lvl=-144.0 PRE` | **on=True lvl=0.0 POST** |
| ch22 -> Bus 7 | `on=True lvl=0.0 POST` | **on=False lvl=-144.0 POST** |
| ch24 -> Bus 13 | `on=True lvl=-144.0 PRE` | **on=True lvl=0.0 POST** |
| ch24 -> Bus 7 | `on=True lvl=0.0 POST` | **on=False lvl=-144.0 POST** |
| ch25 -> Bus 13 | `on=False lvl=-144.0 PRE` | **on=True lvl=0.0 POST** |
| ch25 -> Bus 7 | `on=True lvl=0.0 POST` | **on=False lvl=-144.0 POST** |
| ch26 -> Bus 13 | `on=False lvl=-144.0 PRE` | **on=True lvl=0.0 POST** |
| ch26 -> Bus 7 | `on=True lvl=-3.0 POST` | **on=False lvl=-144.0 POST** |
| ch27 -> Bus 13 | `on=False lvl=-144.0 PRE` | **on=True lvl=0.0 POST** |
| ch27 -> Bus 7 | `on=True lvl=-6.0 POST` | **on=False lvl=-144.0 POST** |
| ch1 -> Bus 7 | `on=False lvl=-144.0 POST` | **on=True lvl=0.0 POST** |
| ch2 -> Bus 7 | `on=False lvl=-144.0 POST` | **on=True lvl=-1.0 POST** |
| ch3 -> Bus 7 | `on=False lvl=-144.0 POST` | **on=True lvl=-2.0 POST** |
| ch4 -> Bus 7 | `on=False lvl=-144.0 POST` | **on=True lvl=-1.0 POST** |
| ch5 -> Bus 7 | `on=False lvl=-144.0 POST` | **on=True lvl=-1.0 POST** |
| ch6 -> Bus 7 | `on=False lvl=-144.0 POST` | **on=True lvl=-1.0 POST** |
| ch7 -> Bus 7 | `on=False lvl=-144.0 POST` | **on=True lvl=1.0 POST** |
| ch21 -> Bus 7 | `on=True lvl=0.0 POST` | **on=True lvl=3.0 POST** |
| ch23 -> Bus 7 | `on=True lvl=0.0 POST` | **on=True lvl=3.0 POST** |
| ch33 -> Bus 7 | `on=True lvl=-10.0 POST` | **on=True lvl=-6.0 POST** |
| ch8 -> Bus 7 | `on=True lvl=-3.0 POST` | **on=True lvl=-2.0 POST** |
| ch10 -> Bus 7 | `on=True lvl=-6.0 POST` | **on=True lvl=-5.0 POST** |
| ch11 -> Bus 7 | `on=True lvl=-4.0 POST` | **on=True lvl=-5.0 POST** |
| ch12 -> Bus 7 | `on=True lvl=-4.0 POST` | **on=True lvl=-5.0 POST** |
| ch29 -> MX5 | `on=True lvl=0.0` | **on=False lvl=-144.0** |
| ch29 -> Bus 7 | `on=False lvl=-6.0 POST` | **on=True lvl=-12.0 POST** |
| ch30 -> MX5 | `on=True lvl=-0.0` | **on=False lvl=-144.0** |
| ch30 -> Bus 7 | `on=False lvl=-6.0 POST` | **on=True lvl=-12.0 POST** |
| ch1 -> Bus 11 | `on=False lvl=-144.0 PRE` | **on=True lvl=-3.0 POST** |
| ch6 -> Bus 11 | `on=False lvl=-144.0 PRE` | **on=True lvl=-8.0 POST** |
| ch8 -> Bus 11 | `on=False lvl=-144.0 PRE` | **on=True lvl=0.0 POST** |
| ch11 -> Bus 11 | `on=False lvl=-144.0 PRE` | **on=True lvl=-12.0 POST** |
| ch12 -> Bus 11 | `on=False lvl=-144.0 PRE` | **on=True lvl=-12.0 POST** |
| ch17 -> Bus 11 | `on=False lvl=-144.0 PRE` | **on=True lvl=-6.0 POST** |
| ch18 -> Bus 11 | `on=False lvl=-144.0 PRE` | **on=True lvl=-6.0 POST** |
| ch19 -> Bus 9 | `on=True lvl=-4.2 PRE` | **on=False lvl=-144.0 PRE** |

### CLEANUP  (3)

| Item | Was | Now |
|---|---|---|
| ch20 -> Bus 11 | `on lvl=-144.0` | **OFF (not a member of this group)** |
| ch23 -> Bus 13 | `on lvl=-144.0` | **OFF (not a member of this group)** |
| ch19 LEAD1 (no input source) | `routed to Main 1 + Bus 9` | **unrouted** |

### FX  (2)

| Item | Was | Now |
|---|---|---|
| FX7 model | `MACH4` | **C5-CMB (multiband, on Bus 7)** |
| FX11 model | `GEQ` | **DE-S2 (de-esser, on Bus 13)** |

### OUTPUT  (15)

| Item | Was | Now |
|---|---|---|
| LCL out 4 | `OFF.1` | **MTX.9 = Matrix 5 STREAM Left  -> OSEE** |
| LCL out 5 | `OFF.1` | **MTX.10 = Matrix 5 STREAM Right -> OSEE** |
| LCL out 2 | `OFF.1` | **MAIN.1 = Main 1 Left  -> OSEE input 2 (EMERGENCY)** |
| LCL out 3 | `OFF.1` | **MAIN.2 = Main 1 Right -> OSEE input 2 (EMERGENCY)** |
| LCL out 1 | `A.33` | **OFF - was sourced from non-existent A-33** |
| USB out 43 | `BUS.7` | **OFF - was junk (dead bus / muted main)** |
| USB out 44 | `BUS.7` | **OFF - was junk (dead bus / muted main)** |
| USB out 47 | `MAIN.7` | **OFF - was junk (dead bus / muted main)** |
| USB out 48 | `MAIN.7` | **OFF - was junk (dead bus / muted main)** |
| AUX out 1 | `BUS.9` | **OFF - all six fed from muted Bus 5** |
| AUX out 2 | `BUS.9` | **OFF - all six fed from muted Bus 5** |
| AUX out 5 | `BUS.9` | **OFF - all six fed from muted Bus 5** |
| AUX out 6 | `BUS.9` | **OFF - all six fed from muted Bus 5** |
| AUX out 7 | `BUS.9` | **OFF - all six fed from muted Bus 5** |
| AUX out 8 | `BUS.9` | **OFF - all six fed from muted Bus 5** |

### NAME  (4)

| Item | Was | Now |
|---|---|---|
| ch33 | `''` | **KIDS LAPEL** |
| ch29 | `'CRWD 1'` | **CROWD L** |
| ch30 | `'CRWD 2'` | **CROWD R** |
| ch40 | `'TB'` | **X-CRWD2 DUP** |

### DCA  (2)

| Item | Was | Now |
|---|---|---|
| DCA 10 | `DCA.10` | **SPEECH** |
| DCA 11 | `DCA.11` | **CROWD** |

### MUTE GRP  (1)

| Item | Was | Now |
|---|---|---|
| MGRP 6 | `MGRP.6` | **CROWD** |

### TAGS  (5)

| Item | Was | Now |
|---|---|---|
| ch21 | `''` | **#D10,SPEECH** |
| ch23 | `''` | **#D10,SPEECH** |
| ch33 | `'MGRP.1'` | **MGRP.1,#D10,SPEECH** |
| ch29 | `'MGRP.1'` | **MGRP.1,#D11,CROWD,MGRP.6** |
| ch30 | `'MGRP.1'` | **MGRP.1,#D11,CROWD,MGRP.6** |

---

## Rollback

Load `GHC-PRE-BROADCAST-V1` (the show you saved in step 2 above), or reload your
original `TONY GHC MARCH 2026 PMAMB0.snap`. Nothing here is one-way.
