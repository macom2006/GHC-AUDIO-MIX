# Appendix A1 — If the desk is actually an X32 / M32

> **SUPERSEDED — no longer applies to GHC.** The console file confirms a
> **Behringer WING full-size**, serial `S240100078BV2`, firmware 3.1-0. This
> appendix is retained only as reference for a satellite campus or a second room
> running an X32/M32.

The original brief said "Baringer Wing 32." There is no product with that name —
Behringer's WING family is **WING**, **WING Compact** and **WING Rack**, all sharing
the same 48-channel engine. The alternative reading was an **X32** (or its Midas
sibling, the **M32**), which is a different and older architecture.

Everything in docs 01–15 still applies in principle. This appendix lists what
changes in practice.

## Architectural differences that matter

| | WING | X32 / M32 |
|---|---|---|
| Input channels | 48 + 8 aux | 32 + 8 aux returns |
| **Main buses** | **4 stereo** | **1 stereo (LR) + 1 mono (M/C)** |
| Mix buses | 16 stereo | 16 mono/stereo-linkable |
| Matrices | 8 stereo | 6 mono |
| DCAs | 16 | 8 |
| Mute groups | Multiple | 6 |
| Channel EQ | 6-band | 4-band (+ HPF) |
| Automix | Yes (2 groups) | **No** |
| USB interface | 48×48 | 32×32 (X-USB card) |
| Per-channel sends to multiple mains | **Yes** | No — only LR and M/C |

## The one change that reshapes the whole design

**The X32 has only one main bus.** You cannot build the broadcast mix on "Main 2"
because there is no Main 2.

### Solution: build the broadcast mix on a stereo mix bus

1. **Link Mix Bus 15/16 as a stereo pair.** Name it `BROADCAST`.
2. Set every channel's send to bus 15/16 to **pre-fader**. This is essential — it
   makes the broadcast mix independent of the house faders, which is the whole point.
3. Enable **"pan follows channel pan"** on that bus so the stereo image is preserved.
4. Insert the broadcast processing chain on bus 15/16 (EQ, compressor, limiter).
5. Route bus 15/16 to the physical outputs feeding the Osee.

**What you lose:** two mix buses that could otherwise be monitor sends, and the
convenience of Sends-on-Fader showing a true second mix. **What you keep:** a
genuinely independent broadcast mix, which is non-negotiable.

### Revised bus plan for X32

| Bus | Purpose |
|---|---|
| 1–6 | IEM mixes (stereo-linked pairs → 3 stereo mixes) or 6 mono monitor sends |
| 7–8 | Wedges |
| 9–12 | FX sends (Hall, Plate, Delay, Drum Room) |
| 13 | Sub feed (aux-fed subs) |
| 14 | Utility / broadcast speech reverb |
| **15/16** | **BROADCAST (stereo, pre-fader)** |

You will have fewer IEM mixes available. If the band needs more than three stereo
in-ear mixes, an X32 is at its limit and a personal monitor system (P16-M or
similar) is the right answer.

## Revised channel count

32 channels instead of 48 means cuts. Suggested priority:

| Keep | Drop or combine |
|---|---|
| Kick, Snare top, HiHat, 2 toms, OH L/R | Kick out, snare bottom, third tom, drum spare |
| Bass DI | Bass amp mic |
| EG1, EG2, AG1 | AG2 |
| Keys L/R | Pads on the same channels, or mono |
| WL, BGV 1–3 | Vocal spare, choir |
| Tracks L/R, Click | Cues (fold into click mix) |
| Pastor headset, lav, 2 handhelds, lectern | Guest/kids/spare — repatch as needed |
| **Ambience L/R** | **Never drop these** — they are what makes the stream work |

## Other differences to account for

| Feature | Workaround on X32 |
|---|---|
| **No automix** | Manage speech mics manually, or gate each speech channel tightly and use mute groups aggressively. An external automixer (Dugan, or a Shure IntelliMix unit) is worth buying if you run panels or multiple speakers regularly. |
| 4-band EQ instead of 6 | Prioritise: one low cut (in addition to the HPF), one mid cut, one presence boost, one air shelf. Drop the least important band from each doc 04 table. |
| Only 8 DCAs | Use: 1 Speech, 2 Worship Vox, 3 BGV, 4 Drums, 5 Bass, 6 Guitars, 7 Keys, 8 Band (All). Drop the FX, Ambience and Media DCAs — control those on their channels. |
| 6 mono matrices | Combine zones: Lobby + nursery on one matrix, green room + hearing assist on another. |
| 32-channel USB | Records 32 of the 48 channels. Prioritise the list above. Virtual soundcheck works identically. |
| Gates are simpler | The side-chain keying used on ch 2 and ch 4 in doc 04 is available on X32 — use it. |

## Everything that does **not** change

- The dual-mix philosophy (doc 01)
- Gain structure targets (−18 dBFS average, −10 dBFS peaks)
- Every channel EQ, gate and compressor value in doc 04 — the numbers are the same
- Aux-fed subwoofers (doc 06)
- SPL and LUFS targets (docs 06, 07)
- Broadcast offsets and the mastering chain (doc 07)
- Ambience mic technique and the privacy rule (doc 07)
- Monitor philosophy and feedback procedure (doc 08)
- Logic Pro workflow and virtual soundcheck (doc 10) — the X-USB card supports it
- Osee integration and lip-sync (doc 11)
- Scenes, safes and operating discipline (doc 12)
- Run sheet, troubleshooting, training (docs 13–15)

## Recommendation

If the desk is an X32 and the church is serious about the online product, **the WING
is the right upgrade** — and specifically because of the four main buses. The ability
to build a genuinely separate broadcast mix, with its own fader level and pan per
channel, without spending monitor buses on it, is worth the price of the console on
its own for a church that streams every week.

In the meantime the X32 configuration above will get you most of the way there.
