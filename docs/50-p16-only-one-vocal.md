# 50 — Why only one vocal reaches the P16

**File:** `console/GHC BROADCAST V23.snap` (built on V22)

## Two separate problems

### 1. Bank B holds all ten singers and delivers nothing

| Bank | Port | Vocals patched | Reaches anyone? |
|---|---|---|---|
| A | AES50-**A** Ultranet (the S32's P16 port) | **4 of 10** | yes — this is the live bank |
| B | AES50-**B** outputs 33–48 | **all 10** | **no — nothing is fitted on AES50-B** |

All the careful Bank B work — Vox 1–4, LEAD2, Raissa, Wireless 3, Jude, Brenda,
Wireless 4 — goes to a port with no hardware on it. Recorded in doc 24 at the
time; the patch has sat there since.

### 2. The live bank only ever had four singers in it

Bank A, as found:

| P16 | Source |
|---|---|
| 1–2 | Bus 8 DRUMS stem |
| 3–6 | Bass, E Gtr, Keys 1, Keys 2 |
| 7–8 | Crowd L / R |
| 9 | Talkbacks |
| **10** | **Raissa** |
| **11** | **Wireless 4 — MARTHA** |
| **12** | **LEAD2 — DAVID** |
| **13** | **Vox 2 — DEHIL** |
| 14–15 | TRACK, AC Gtr |
| 16 | Pastor HH |

**Six singers were never in the live bank at all:** Marie, Gabby, Peggy, Elsie,
Jude, Brenda.

Nothing is muted and every gain is set — checked all fourteen stage-box inputs.
Of the four that *are* patched, Raissa is simply the one that was live; the other
three are wireless and were presumably off or not singing.

## The fix was already built and never connected

**Bus 9, "WL BUS P16"** — fourteen sources at a deliberate −6 dB each:

```
Vox 1, Vox 2, Vox 3, Vox 4, LEAD2, Raissa, Wireless 3,
Jude, Brenda, Wireless 4, Pastor HH, House, Sax, LOOP
```

Bus fader −3.0, unmuted. Patched to **nothing** — no output, no bus send, no
main. Somebody built the vocal stem for the in-ears and never patched it. It was
flagged in doc 43's addendum; this is the thing that fixes it.

## What V23 changes

Three values in the output patch.

| | Was | Now |
|---|---|---|
| P16 **11** | A-17 Wireless 4 — one singer | **Bus 9 WL BUS P16 — L** |
| P16 **12** | A-22 LEAD2 — one singer | **Bus 9 WL BUS P16 — R** |

**All ten singers plus Pastor now reach every P16 unit** on one stereo pair.

Chosen deliberately:

- **The crowd stays** on P16 7/8 — musicians on isolating in-ears want the
  congregation.
- **Raissa (10) and Dehil (13) stay** as individual channels, so anyone who
  wants one of them louder than the blend still can.
- Martha and David lose their individual channels but are both in the stem.

All 40 channels, every bus, the mains, matrices, FX, AUX and the whole input
patch are byte-identical. Within the A outputs only 43 and 44 changed — the
wedge feeds on A-1 to A-4 are untouched.

## One thing to decide later

**Bus 9's sends are mostly POST fader.** Every FOH fader move changes what the
musicians hear. For in-ears that is usually the wrong choice — PRE gives them a
stable mix regardless of what happens out front. Sax and LOOP are already PRE.

Switching the twelve vocal sends to PRE is a real change to what the band hears
mid-service, so it is not in V23. Worth doing at a rehearsal, with the band
listening, rather than sprung on them on a Sunday.

## And the other half of the problem remains

Bank B is still patched to a port with nothing on it. **An S16 or SD16 on
AES50-B** would light up a second 16-channel bank that already has all ten
singers mapped — the cheapest possible upgrade to the in-ear system, because the
configuration work is already done.
