# 52 — P16 Bank A, instruments first

**File:** `console/GHC BROADCAST V25.snap` (built on V24, supersedes it)

Brief: instruments have priority, then Pastor and House, then Dehil and Elsie
individually if available, then the rest of the vocals as they fit. No crowd.

## The layout

| P16 | Source | Tier |
|---|---|---|
| **1** | Bus 8 DRUMS **L** | **instruments** |
| **2** | Bus 8 DRUMS **R** | |
| **3** | Bass | |
| **4** | E Gtr | |
| **5** | AC Gtr | |
| **6** | Keys 1 | |
| **7** | Keys 2 | |
| **8** | TRACK | |
| **9** | **Pastor HH** | **speech** |
| **10** | **House** | |
| **11** | **Dehil** (Vox 2) | **named singers** |
| **12** | **Elsie** (Wireless 3) | |
| **13** | **Bus 9 WL BUS P16** | **the rest** — Marie, Gabby, Peggy, Jude, Brenda, Martha |
| **14** | David (LEAD2) | fitted in the space left |
| **15** | Raissa | fitted in the space left |
| **16** | Bus 10 TALKBACKS | |

16 of 16, every tier satisfied, crowd out.

## How it all fit

One trick made the difference: **every vocal send into Bus 9 is panned dead
centre**, so its left and right legs are identical and **a single leg carries
the whole blend.** That freed the slot which let David and Raissa keep
individual channels rather than disappearing into the stem.

Verified before relying on it — all fourteen sends read pan +0.0.

## Who is where

**Individual channels (8):** Pastor, House, Dehil, Elsie, David, Raissa — plus
every instrument.

**Via the stem on channel 13 (6):** Marie, Gabby, Peggy, Jude, Brenda, Martha.

David and Raissa were chosen for the two spare slots because **they are the two
who had individual channels in the original Bank A** — not a guess about who
matters most. If you would rather swap either for someone else, it is one socket
each.

Note the stem on 13 contains *all* ten singers, so the six individual voices also
appear inside it. That is normal — you get the person plus the blend — but it
means you cannot remove Dehil from channel 13, only from channel 11.

## Instruments are better off than before

Every instrument that was individual before V24 is back, **and the DRUMS stem
returns in stereo.** Nothing in the instrument tier was given up to fit the
vocals.

## Tell the band before Sunday

**Every channel number has moved again** — V24 and V25 both re-laid the bank. A
P16-M stores its mix per channel number, so saved mixes point at the wrong
sources.

**Do not load V24.** Go straight to V25 so the band rebuilds their mixes once,
not twice. At rehearsal, not Sunday morning.

## Verified

All 40 channels byte-identical. Buses, mains, matrices, FX, AUX and the entire
input patch identical. Every output group except A identical, and within A only
outputs 33–48 changed — **the wedge feeds on A-1 to A-4 are untouched.**

## Unchanged facts

- **Bank B** is still mapped with all ten singers and connected to nothing. An
  S16 or SD16 on AES50-B would light it up and could carry the six stem-only
  singers individually.
- **Bus 9's vocal sends are mostly POST fader**, so FOH moves still change what
  the band hears on channel 13. PRE is the usual choice for monitors; it is a
  rehearsal change, not a Sunday one.
