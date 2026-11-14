# 51 — P16 rebuilt: every vocal on its own channel

**File:** `console/GHC BROADCAST V24.snap` (built on V23)

Brief: all the vocals divided across the available channels, **Pastor and House
each on their own**, and **no crowd**.

## The new Bank A

| P16 | Source | |
|---|---|---|
| **1** | Bus 6 BAND STEM **L** | all 14 instruments, PRE fader |
| **2** | Bus 6 BAND STEM **R** | |
| **3** | Vox 1 | MARIE |
| **4** | Vox 2 | DEHIL |
| **5** | Vox 3 | GABBY |
| **6** | Vox 4 | PEGGY |
| **7** | LEAD2 | DAVID |
| **8** | Raissa | RAISSA |
| **9** | Wireless 3 | ELSIE |
| **10** | Jude | JUDE |
| **11** | Brenda | BRENDA |
| **12** | Wireless 4 | MARTHA |
| **13** | **Pastor HH** | own channel |
| **14** | **House** | own channel |
| **15** | Bass | pitch and time reference |
| **16** | Bus 10 TALKBACKS | |

16 of 16. All ten singers individual, Pastor and House separate, crowd out.

## What changed and what it costs

**Gained:** six singers who were never in the P16 at all — Marie, Gabby, Peggy,
Elsie, Jude, Brenda — plus House, which was in neither bank.

**Lost as individual channels:** E Gtr, AC Gtr, Keys 1, Keys 2 and TRACK. They
are all still there inside **Bus 6 BAND STEM** on channels 1–2, just not
separately adjustable. The Bus 8 DRUMS stem is gone for the same reason — drums
are in the band stem.

**Bass kept its own channel** because the crowd slot freed up and bass is the
one instrument singers use for pitch and the band locks to for time. If TRACK
or the drums stem would serve better there, it is a one-socket change — say
which.

Bus 6's sends are all **PRE fader**, so the band blend in everyone's ears no
longer moves when the FOH engineer touches a fader. That is an improvement over
the old layout, where the individual instrument feeds came straight off the
stage box.

## Tell the band before Sunday

**Every channel number has moved.** A P16-M stores its mix per channel number,
so every saved mix on every unit is now pointing at the wrong source — channel 3
used to be Bass and is now Marie.

**Everyone has to rebuild their mix once.** Do it at rehearsal, not at 9 a.m. on
a Sunday. After that it stays put.

## Verified

All 40 channels byte-identical. Buses, mains, matrices, FX and AUX identical.
The whole input patch identical. Every output group except A identical, and
within A only outputs 33–48 changed — **the wedge feeds on A-1 to A-4 are
untouched**, so the stage monitors behave exactly as before.

## Bus 9 is free again

`WL BUS P16`, the vocal stem, is no longer patched anywhere — individual
channels supersede it. It is still built and loaded, so it costs nothing to
leave, and it is there if you ever want a single all-vocals channel back.

## Still true

Bank B remains mapped with all ten singers and connected to nothing. **An S16 or
SD16 on AES50-B** would give a second 16-channel bank — and with Bank A now
serving singers, that second bank is what would give the musicians their
individual instruments back.

## Coupling check: two new flags, both expected

`tools/coupling_check.py` goes from 8 items to 10 on V24. Both additions are
consequences of the change, not faults:

- **Bus 8 DRUMS now reaches nothing.** Intended — the drums stem came off the
  P16 because drums are inside Bus 6. It joins buses 2, 5, 9 and 12 as
  configured-but-unrouted.
- **Bus 6 BAND STEM now feeds output groups A and B.** It is patched to the new
  Bank A as well as the long-dead Bank B, so **one fader controls the band blend
  in both banks.** Harmless while nothing is fitted on AES50-B; worth remembering
  if an S16/SD16 ever goes in, because it is then a shared control rather than
  two independent ones.
