# 53 — P16 Bank A, final order

**File:** `console/GHC BROADCAST V26.snap` — supersedes V24 and V25.

Brief: keep the order we had before — Drums (Kick, and a mix of snare, rack 1,
rack 2 and OH), Bass, Keys 1, Keys 2, Acoustic, E Gtr — then the vocals.

## The layout

| P16 | Source |
|---|---|
| **1** | **Kick** |
| **2** | **KIT MIX** — snare + rack 1 + rack 2 + OH |
| **3** | Bass |
| **4** | Keys 1 |
| **5** | Keys 2 |
| **6** | Acoustic |
| **7** | E Gtr |
| **8** | Pastor HH |
| **9** | House |
| **10** | Dehil (Vox 2) |
| **11** | Elsie (Wireless 3) |
| **12** | David (LEAD2) |
| **13** | Raissa |
| **14** | Vocal stem — Marie, Gabby, Peggy, Jude, Brenda, Martha |
| **15** | TRACK |
| **16** | Talkbacks |

16 of 16. Instruments in the order asked for, then vocals. No crowd.

## Bus 8 rebuilt and renamed

It was called DRUMS and held nine sources. It now holds exactly four, and is
renamed **KIT MIX** because it no longer contains the kick — a name that lies is
how V15 happened.

| Removed | Why |
|---|---|
| **Kick** | has its own channel now |
| **ch3**, labelled HH | it is the **snare bottom** mic (stage box says SNARE BTTM) |
| **Floor** | not in the brief; the overheads carry it |
| **Vox 4, at −16 dB** | **a vocal was sitting in the drum bus** |

| Changed | |
|---|---|
| **OHs: −19.16 → −8.0 dB** | at 19 dB under the snare the overheads were inaudible, so "and OH" was not true of the mix |

Contents now: Snare −0.36, Rack 1 −2.66, Rack 2 −2.05, OHs −8.00 — all **PRE
fader**, so the kit blend does not move when FOH touches a fader.

**Bus 8 feeds the P16 and nothing else** — verified before changing it, so none
of this reaches the house, the wedges or the stream.

## Three things to adjust by ear

1. **OHs at −8.0** is my starting point, not a measurement. More if the kit
   sounds small, less if it sounds washy.
2. **The snare bottom mic (ch3) is out.** If the snare sounds thin in the ears,
   add it back — one send, and its polarity is already correctly inverted.
3. **Floor tom is out.** The overheads cover it. One send if the drummer wants
   it discrete.

## KIT MIX is mono

One channel, as "a mix of…" implies, which is what let TRACK and talkback both
stay. If you would rather have it in stereo, it costs one slot — TRACK is the
one I would give up.

## Tell the band: rebuild mixes once

**Do not load V24 or V25.** All three versions re-laid the channel numbering, and
a P16-M stores its mix per channel number. Going straight to V26 means everyone
rebuilds their mix **once**. At rehearsal.

## Verified

Every channel fader, MAIN send, wedge send, stream send, EQ and compressor
identical. Mains, matrices, FX and AUX identical. A outputs 1–32 identical, so
the wedge feeds are untouched. Only the five channels whose Bus 8 send changed
differ at all.
