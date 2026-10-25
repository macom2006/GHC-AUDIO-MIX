# 40 — BC BAND: one fader for the band on the stream

**File:** `console/GHC BROADCAST V13.snap` (built on V12)

## What you get

**Bus 16, renamed "BC BAND".** One fader that sets the whole band's level in the
stream, with no effect on FOH, the wedges or the in-ears.

You now have three stream controls:

| Control | Covers |
|---|---|
| **Bus 16 BC BAND → Bus 7** | Kick, Snare, HH, toms, OHs, Bass, E Gtr, AC Gtr, Keys 1&2, Sax, LOOP |
| **Bus 13 BC VOX → Bus 7** | All singers (doc 38) |
| ch21 / ch23 direct sends | Pastor, House — speech, deliberately separate |

On the desk: select **Bus 7 (BROADCAST)**, press **SENDS**, and both BC BAND and
BC VOX appear as faders side by side.

## Why Bus 16

All 16 buses were allocated. Bus 16 was "Slap", a slap-delay return that has
been muted at −144 since V9. Retiring it was the only way to free a bus.

**The slap delay is gone permanently.** It has been inaudible for weeks.

## What was changed

- 14 band channels now send to BC BAND at **exactly their old Bus 7 level**;
  their direct Bus 7 sends are off
- BC BAND → Bus 7 at unity, bus fader at 0
- Bus 16 renamed, unmuted, fader 0
- Slap EQ flattened (it was a −15 dB telephone filter)
- Slap's brickwall limiter switched **off**
- All 15 old slap sends into Bus 16 turned off
- FX3 pre-insert off

**Net level into the GoStream is unchanged — verified channel by channel.**
Nothing to re-trim on the switcher.

## The feedback trap this nearly created

Bus 16 also sent to **Bus 1 STAGE MON at −26 dB** — the old slap return into
the wedges. Harmless while the bus was muted at −144.

Unmuting it and bringing the fader to 0 would have injected **the entire band
into the stage monitors**, on a system that already has a feedback problem at
13 open mics.

That send is now OFF. It was caught by an assertion, not by listening — the
first build of V13 had it, and the check failed before the file shipped.

A second gap: bus sends are stored under keys `1`–`16` **and `MX1`–`MX8`** for
the matrices. The first loop only checked `1`–`16`. Any future routing audit
must cover all 24 keys.

## Verified before release

- Net broadcast gain identical on all 14 channels
- BC BAND sends to Bus 7 and nothing else — all 24 destinations checked
- Bus 7 sends only to Matrix 5 — no return path, no loop
- Neither bus reaches any main, so neither can reach the PA
- Output patch untouched — BC BAND reaches no speaker, wedge or in-ear
- Buses 1–15 untouched: P16 in-ears, all five monitor mixes, subs all safe
- Every channel fader, main send, EQ, dynamics and preamp untouched

## Deliberately not done

**No compressor on BC BAND.** Band glue is the thing that would make the stream
sound "produced", but setting a ratio on a bus nobody has heard is how V11
happened. The compressor is off and waiting.

Get SD cards into WING-LIVE, record Matrix 5 for two services, and the glue
gets set against measurement.
