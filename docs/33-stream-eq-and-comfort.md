# 33 — Stream EQ, Clipping and Comfortable Listening

Built on the V5 you are actually running. **`GHC BROADCAST V9.snap`.**

---

## Why the stream still clips, and why it tires people out

Two faults, and they compound.

### Fault 1 — the top end was boosted four times over

The broadcast signal passes through two EQ stages, and **both were lifting the
treble**:

| Stage | Boost |
|---|---|
| Bus 7 EQ — 3.5 kHz | **+2.0 dB** |
| Bus 7 EQ — 8 kHz shelf | **+1.5 dB** |
| Matrix 5 Pulsar — 12 kHz | **+3.4 dB** |
| Matrix 5 Pulsar — 2 kHz | **+1.1 dB** |
| **Stacked total** | **+8.0 dB of top-end lift** |

Eight decibels of treble is not a bright mix, it is a painful one. On earbuds it is
exhausting within minutes, and it is the single biggest reason the stream is not
comfortable to listen to.

Half of that is mine — the Bus 7 boosts came from my V1, written before I had seen
that the Matrix 5 Pulsar was already lifting the same region. **Two stages, neither
aware of the other.**

### Fault 2 — the limiter was being used as a loudness maximiser

| Setting | Was | Should be |
|---|---|---|
| FX16 input gain | **+3.0 dB** | 0 dB |
| FX16 squeeze | **10** | 3 |

Driving a limiter **into** 3 dB of extra gain with aggressive squeeze is how you
make a radio advert loud. It is not what a church stream wants. Combined with +8 dB
of treble arriving at its input, that limiter was working constantly — and a limiter
that never rests is exactly what listening fatigue sounds like.

### And the gain staging was backwards

| Stage | Was |
|---|---|
| 1. Matrix 5 input trim | **+5.3 dB** ← signal **boosted** on the way in |
| 2. TAPE saturation | sees a hot signal |
| 3. Pulsar EQ | adds up to +3.4 dB more |
| 4. ECL33 compressor/limiter | slams |
| 5. FX16 limiter | +3 dB drive, squeeze 10 |
| 6. **Fader** | **−37.4 dB** ← only **now** is it turned down |

Every processor in that chain ran roughly 37 dB hotter than it needed to, and the
fader at the end simply made the resulting distortion quiet. **Same mistake as the
GoStream mic input, one stage earlier:** attenuating after the damage instead of
before it.

---

## What V9 changes

### The stream

| Change | From | To |
|---|---|---|
| Bus 7 EQ, 3.5 kHz | +2.0 dB | **+1.0 dB** |
| Bus 7 EQ, 8 kHz shelf | +1.5 dB | **0.0 dB** |
| Pulsar, 12 kHz | +3.4 dB | **+1.0 dB** |
| Pulsar, 2 kHz | +1.1 dB | **+0.5 dB** |
| **Pulsar, 30 Hz** | **+3.7 dB** | **0.0 dB** |
| FX16 limiter input gain | +3.0 dB | **0.0 dB** |
| FX16 limiter squeeze | 10 | **3** |
| Matrix 5 input trim | +5.3 dB | **0.0 dB** |
| Matrix 5 fader | −37.4 dB | **−32.1 dB** |

**Stacked top-end lift: +8.0 dB → +2.5 dB.**

On the 30 Hz boost: no phone, laptop or earbud reproduces 30 Hz. All it did was
trigger the limiter on energy nobody could hear — pumping the whole mix down for
nothing. Removing it is free headroom.

**The net output is unchanged at −32.1 dB.** Trim and fader were rebalanced to the
same total, so **you do not need to touch the GoStream.** The chain now runs at a
sane internal level and the attenuation happens where it belongs.

### Carried forward from V7

Your V5 predates these:

- **House mic EQ** — three octave-wide cuts narrowed to Q 5 / 7 / 7, same depth and
  frequency. No feedback margin given away; about two octaves of voice returned.
- **House mic compressor** attack 30 ms → 8 ms
- **Bus 16 "Slap" re-muted** — six open mics feed it at unity and it returns into the
  wedge. A latent feedback loop I left open in V1.

### Deliberately not included

**V6's move of PC playback to the analog AUX IN 5/6.** You are on V5, which keeps the
PC on USB-7, and I am assuming that is because the analog cable is not wired yet.
Forcing it would silence your playback. When you do wire it, that change is a
two-second edit on the desk: AUX 8 source → AUX IN 5.

---

## Verified untouched

- All routing and patching
- **Every high-pass filter** on every channel
- **Every channel fader**
- The house mix, Main 1, and PA Matrices 1–4
- The P16 Bank B patch and the BAND STEM

Your room will sound exactly as it does now. Only the stream changes.

---

## What to expect

**Less bright. Less loud. Much easier to listen to.**

It may sound slightly quieter at first, because the limiter is no longer squeezing
everything up against the ceiling. That is correct — the loudness you had was
manufactured by compression, and it is what made it tiring. If after a week it is
genuinely too quiet, raise **Bus 7's fader**, not the limiter drive.

### Check it

1. Play a worship song through the stream. Listen on **earbuds** for a full song, not
   thirty seconds. Fatigue is a slow effect.
2. Then a sermon clip. Speech should be clear and unforced.
3. Watch the FX16 limiter. **It should be mostly idle**, catching an occasional peak.
   If it is working constantly, Bus 7 is still too hot.
4. Confirm the GoStream meters read the same as before — they should, the net output
   did not change.

---

## The general lesson

Both the stream clipping and the GoStream clipping were the same mistake in different
places: **gain added early, taken away late.**

Anything that distorts, saturates, compresses or limits does its damage at the point
it is hit, and no amount of turning down afterwards undoes it. Attenuate going in,
not coming out.

Worth remembering next time something sounds crunchy and turning it down does not
help: the problem is always upstream of whatever you just turned down.
