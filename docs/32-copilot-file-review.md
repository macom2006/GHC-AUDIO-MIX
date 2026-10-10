# 32 — Review of the Copilot File

**File:** `GHC BROADCAST V3.1 FOH STREAM OPTIMIZED.snap`
**Created:** 2026-09-25 22:20 · **Reviewed:** 2026-10-10

## Verdict: do not load it. Stay on V7.

Your instinct that something was shaky is correct. There are two show-stoppers,
and both come from the same root cause.

---

## Root cause: it was built on a two-week-old baseline

Comparing it against every version in this project, the file is derived from
**`GHC BROADCAST V1.snap`** — the first file I sent, on 25 September.

Since then there have been six revisions and your own operators' edits. Copilot
never saw any of them, so loading this file does not "add Copilot's improvements to
your console" — **it replaces your console with a two-week-old state that happens to
have some tone changes on it.**

That is not a criticism of Copilot's work. It is a process problem, and it will
recur every time two tools edit the same file from different starting points.

---

## Show-stopper 1 — it would blast the GoStream

| | Matrix 5 fader | Input trim | **Net** |
|---|---|---|---|
| Your live console | −37.4 | +5.3 | **−32.1 dB** |
| My V7 | −37.4 | +5.3 | **−32.1 dB** |
| **Copilot file** | −0.6 | +2.0 | **+1.4 dB** |

**That is 33.5 dB hotter into the GoStream's microphone input.**

This is the exact fault that caused the clipping and the noise you spent two weeks
chasing, and that you finally solved by setting that attenuation. Loading this file
puts a near-full-scale console output into a mic input, live.

Copilot did not decide to undo it. Its baseline predates the fix, so it simply never
knew the setting existed. The danger is identical either way.

**This is the clearest argument yet for scene-safing Matrix 5** — see
`16-remediation-plan.md` Stage 1.

## Show-stopper 2 — every open mic's high-pass was lowered

You asked Copilot to help with **feedback**. This moves in the opposite direction.

| Ch | Name | V7 | Copilot | Change |
|---|---|---|---|---|
| 13–16 | Vox 1–4 | 200 Hz | 120 Hz | **−80** |
| 20 | LEAD2 (David) | 185 Hz | 110 Hz | **−75** |
| 21 | **Pastor Lapel** | 165 Hz | 110 Hz | **−55** |
| 22 | Raissa | 185 Hz | 120 Hz | −65 |
| 23 | House | 165 Hz | 147 Hz | −18 |
| 24 | Wireless 3 | 189 Hz | 120 Hz | −69 |
| 25 | Jude | 181 Hz | 110 Hz | −71 |
| 26 | Brenda | 185 Hz | 110 Hz | −75 |
| 27 | Wireless 4 | 183 Hz | 120 Hz | −63 |
| 33 | Kids Lapel | 165 Hz | 110 Hz | −55 |

**All thirteen.** The high-pass filter is free gain before feedback — it removes
energy no voice needs and every open microphone picks up. Opening the 110–200 Hz
band across thirteen simultaneously open mics adds proximity boom and stage rumble
into a wedge mix that already has no headroom.

It will not usually change the frequency that rings, which lives at 1–4 kHz. It will
make the wedges muddier and cost you usable level — the opposite of the brief.

---

## What loading it would also undo

| | |
|---|---|
| LOST | Bus 1 monitor GEQ (FX7) — the thing you ring out on |
| LOST | ch 33's original ring-out GEQ |
| LOST | Bus 6 BAND STEM |
| LOST | The entire P16 Bank B patch on AES50-B |
| LOST | PC audio on analog AUX IN 5 — the dropout fix |
| LOST | PC feeding the subs |
| LOST | DCA 8 "PC" membership |
| LOST | ch 34 duplicate PC path shut off |
| LOST | Automix group X armed |
| LOST | Bus 16 "Slap" muted — the latent delay loop reopens |
| LOST | House mic EQ narrowed to Q 5/7/7 |

---

## Credit where it is due

Copilot's work is not bad work. Read on its own terms it is a careful tone pass, and
**it made no routing changes at all** — no repatching, no bus changes, no level moves
except one. That restraint is worth noting.

Two of its calls match conclusions I reached independently:

| Copilot's change | My position |
|---|---|
| Main 1 low shelf **+3 → +1 dB** | I made exactly this change in V2, for the same reason |
| **De-scoop the kick** — the −14.7 dB and −15.0 dB cuts | My own audit flagged these as extreme and "worth an A/B" (doc 00, L2) |

When two independent reviews land on the same two items, those items are probably
right.

Its other instincts — gentler vocal EQ, a softer-knee bus compressor, slightly less
aggressive broadcast EQ — are all defensible. They are just tone, and tone should be
A/B'd in the room, not merged sight-unseen.

---

## `GHC BROADCAST V8-TONE.snap` — Copilot's good ideas, safely

Rather than discard the work, I have built **V7 plus the defensible tonal moves**,
and nothing else:

| Change | Detail |
|---|---|
| Kick 295 Hz | −14.7 → **−9.0 dB** (Copilot proposed −5.0; this is the midpoint) |
| Kick 900 Hz | −15.0 → **−8.0 dB** (Copilot proposed −3.5) |
| Kick 7.3 kHz | +7.8 → **+5.5 dB** |
| Main 1 bus comp | threshold −18 → −16, ratio 3 → 2.5, knee 2 → 4, release 150 → 180 ms |
| Main 1 comp attack | **kept at 20 ms** — Copilot proposed 30, which is too slow for speech |

**Verified identical to V7:** all thirteen high-pass filters, the Matrix 5 output at
−32.1 dB, all routing and patching, every fader, every bus, the PC audio path, and
the automix configuration.

### Use it as an A/B, not a replacement

Load V7, listen to a song. Load V8-TONE, listen to the same song. Keep whichever you
prefer. The kick is the obvious difference — V8 has noticeably more body and less of
the scooped modern sound.

**V7 remains the safe default.** If in doubt, stay on it.

---

## The process problem — worth fixing

Two tools editing one console file from different baselines will keep producing
this, and next time it might not get caught before a Sunday.

**Adopt this rule: whoever works on the mix starts from a fresh export of the live
console, taken that day.**

1. Save the current state on the desk → USB
2. Hand **that** file to whoever is working on it — me, Copilot, anyone
3. Get their file back, **load it mid-week**, never on a Sunday
4. Export the result as the new current state
5. One file is "live" at any moment. Name it with the date.

And before loading **any** file from anyone, check these three:

- [ ] **Matrix 5 net output around −32 dB** (fader + trim)
- [ ] **Open-mic high-pass filters at 165–200 Hz**, not lower
- [ ] **Bus 1 has FX7 (GEQ) on its post-insert**

Those three catch almost everything that matters. They would have caught this.
