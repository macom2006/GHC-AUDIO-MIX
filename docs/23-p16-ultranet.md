# 23 — P16 Ultranet / Personal Monitoring

The P16 feed comes off the S32's Ultranet port, carrying **AES50-A outputs 33–48**.
Those sixteen patches are already set. Here is what is actually on them.

## Current P16 channel map

| P16 ch | AES50-A out | Source | Signal | Processed? |
|---|---|---|---|---|
| 1 | 33 | Bus 8 L | **DRUMS L** | Bus — processed |
| 2 | 34 | Bus 8 R | **DRUMS R** | Bus — processed |
| 3 | 35 | A-9 | Bass | **RAW INPUT** |
| 4 | 36 | A-10 | Electric Guitar | **RAW INPUT** |
| 5 | 37 | A-11 | Keys 1 — **left leg only** | **RAW INPUT** |
| 6 | 38 | A-13 | Keys 2 — **left leg only** | **RAW INPUT** |
| 7 | 39 | A-23 | Crowd 1 | **RAW INPUT** |
| 8 | 40 | A-24 | Crowd 2 | **RAW INPUT** |
| 9 | 41 | Bus 10 L | **TALKBACK** | Bus — processed |
| 10 | 42 | A-20 | Raissa | **RAW INPUT** |
| 11 | 43 | A-17 | Martha | **RAW INPUT** |
| 12 | 44 | A-22 | David | **RAW INPUT** |
| 13 | 45 | A-30 | Dehil | **RAW INPUT** |
| 14 | 46 | A-15 | Track / Loop | **RAW INPUT** |
| 15 | 47 | A-16 | Acoustic Guitar | **RAW INPUT** |
| 16 | 48 | A-25 | Pastor | **RAW INPUT** |

### What is right about this

- **Crowd mics are on the P16** (channels 7 and 8). Most churches never do this, and
  it is the single thing that stops in-ear users feeling sealed off from the
  congregation. Keep it.
- **Talkback is on channel 9.** Correct.
- Drums arrive as a processed stereo bus rather than eight raw mics eating eight
  slots. Correct use of a limited channel count.

---

## This is why your wedges feed back

**Seven of your twelve singers are not on the P16 at all.**

| Singer | Channel | On the P16? |
|---|---|---|
| David (lead) | ch 20 | yes |
| Raissa | ch 22 | yes |
| Martha | ch 27 | yes |
| Dehil | ch 14 | yes |
| Pastor | ch 21 | yes |
| **Marie** | ch 13 | **no** |
| **Gabby** | ch 15 | **no** |
| **Peggy** | ch 16 | **no** |
| **House** | ch 23 | **no** |
| **Elsie** | ch 24 | **no** |
| **Jude** | ch 25 | **no** |
| **Brenda** | ch 26 | **no** |
| **Kids Lapel** | ch 33 | **no** |

A singer who cannot hear themselves in their in-ears will ask for the wedge. Seven
of them have no alternative. That is precisely why Bus 1 STAGE MON is carrying
twelve open microphones, and why you are 10.8 dB down on gain before feedback before
anyone touches a fader.

**The feedback problem and the P16 problem are the same problem.** Fix the P16
allocation and the wedge dependency largely disappears on its own.

---

## The second fault: thirteen of sixteen channels are raw inputs

Sources like `A-9` and `A-20` in the output patch are the **physical input**, tapped
before the WING channel strip. Your musicians are hearing:

| Missing | Consequence in their ears |
|---|---|
| High-pass filter | Proximity boom, stage rumble, handling noise |
| Gate / expander | Every open mic's room noise, all the time |
| EQ | Un-corrected, boxy vocal tone |
| Compressor | Level jumps straight into a sealed earpiece |

The crowd mics are the worst case. On the console, channels 29 and 30 are
high-passed at **254 Hz, 24 dB/oct**. The P16 feed bypasses that entirely, so the
band is getting the full HVAC rumble and stage spill those filters exist to remove.

### The fix, and the thing to check first

Feeding P16 from raw inputs is sometimes deliberate — it keeps musicians' mixes
independent of FOH. That instinct is right, but the execution is too blunt. What you
want is **post-processing, pre-fader**: they get the EQ and compression, and FOH
fader moves still cannot touch their mix.

**Check this at the desk:** in the output patch source list, does your firmware offer
channel direct outs (a `CH` source group) with a tap-point selector? I cannot confirm
it from the file, because nothing in your current patch uses one.

- **If yes** — repatch AES50-A outs 35–40 and 42–48 from the raw inputs to the
  matching **channel direct outs, tapped pre-fader / post-processing.** Same sources,
  properly conditioned. This is the single biggest quality improvement available to
  your in-ear users.
- **If no** — leave them raw, but at minimum accept that the crowd mics will carry
  rumble, and consider spending one P16 slot on a processed crowd feed from a bus
  instead of two raw ones.

### Third fault: the keys are half-missing

Channels 5 and 6 carry **A-11 and A-13** — the *left leg only* of two stereo keyboard
rigs. Anything panned right in either rig simply does not exist in anybody's ears.

Two stereo rigs on two mono channels is the worst of both worlds. Either give one rig
a proper stereo pair, or sum both rigs to a stereo keys group and spend two channels
on that.

---

## Recommended reallocation — no purchase required

This is what I would do with the sixteen channels you have:

| P16 | Source | Change |
|---|---|---|
| 1 | Drums L (Bus 8 L) | keep |
| 2 | Drums R (Bus 8 R) | keep |
| 3 | Bass | repatch to direct out |
| 4 | Electric Guitar | repatch to direct out |
| 5 | Acoustic Guitar | move up from 15 |
| 6 | **Keys stereo L** | one stereo keys group, not two mono halves |
| 7 | **Keys stereo R** | |
| 8 | Track / Loop | |
| 9 | **David — lead vocal** | discrete |
| 10 | **Raissa** | discrete |
| 11 | **Vocal group L** | a stereo group bus carrying the other singers |
| 12 | **Vocal group R** | |
| 13 | **Pastor** | discrete, processed |
| 14 | **Crowd L** | processed, high-passed |
| 15 | **Crowd R** | processed, high-passed |
| 16 | **Talkback** | keep |

Every singer now hears themselves — the two leads discretely, the rest through the
vocal group. It is a compromise, but it is a far better one than seven singers
hearing nothing.

**Cost of the group buses:** you need one stereo keys group and one stereo vocal
group. Buses 2–6 are currently monitor mixes with very little on them (Bus 5 and
Bus 6 are muted; Bus 4 sits at −52 dB). Two of those can be repurposed.

---

## The proper fix: a second Ultranet feed

Sixteen channels cannot serve twelve singers plus a full band discretely. It is
arithmetic again, not configuration.

**AES50 port B is completely free** — I checked, nothing is patched to it. Add an
**S16 or SD16 on AES50-B** and its Ultranet port gives you **sixteen more P16
channels**, for thirty-two total. Then every singer gets their own, every instrument
gets its own, and nobody argues.

That is a modest purchase that removes your wedge dependency, your feedback problem
and your monitor complaints in one move. Of everything in this repository, it is the
equipment spend I would make first — ahead of anything else except room acoustics.

---

## Order of work

| # | Action | Cost | Effect |
|---|---|---|---|
| 1 | Get the seven missing singers onto the P16, however you have to do it | free | **Removes the cause of the wedge feedback** |
| 2 | Check for channel direct outs; if available, repatch all raw P16 sources | free | Proper EQ, compression and filtering in every earpiece |
| 3 | Fix the keys — stereo pair or stereo group | free | Musicians stop hearing half a keyboard rig |
| 4 | High-pass the crowd feed | free | Removes rumble from every in-ear mix |
| 5 | Add an S16/SD16 on AES50-B | modest | 32 P16 channels; the problem stops being a compromise |

Steps 1 to 4 cost nothing and can be done at one mid-week rehearsal.

---

## A note on how P16 mixes are taught

Once every singer is on the system, teach the band the same rule that governs the
console: **build your mix from yourself outward.** Own voice or instrument first and
loudest, then the rhythm reference they need to stay in time, then a little of
everything else, then the crowd mics at the bottom so the room stays present.

A musician whose P16 mix is a miniature FOH mix will always ask for more wedge. A
musician who can hear themselves clearly will stop asking.
