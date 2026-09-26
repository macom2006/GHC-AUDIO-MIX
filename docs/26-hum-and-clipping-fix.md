# 26 — Ground Hum and Clipping: the Actual Fix

The hum and the remaining clipping are **the same problem**, and it cannot be solved
with settings. It needs about £60–150 of hardware.

---

## First, a correction

I told you to drop the WING's Matrix 5 output trim to about **−30 dB**. That was an
emergency stopgap to stop the distortion, and as a permanent setting **it is making
your noise worse.**

Here is why. Running the console output 30 dB down means the signal leaves the WING
at roughly 1/30th of its proper voltage. The GoStream's preamp then has to amplify it
back up — and it amplifies the cable's noise, the ground hum and the input stage's
own noise floor by exactly the same amount. You have deliberately worsened your
signal-to-noise ratio by 30 dB.

**Attenuate with a transformer, not with a fader.** That is the whole fix.

---

## Why the current connection cannot work

| | Level |
|---|---|
| WING XLR output, nominal | **+4 dBu** |
| WING XLR output, peaks | up to **+18 to +21 dBu** |
| GoStream mic input, expects | **−40 to −60 dBu** |
| GoStream line input (if offered), expects | around **−10 dBV** |

Even in **Line** mode you are about **12–14 dB too hot on average** and **20+ dB too
hot on peaks**. In mic mode you are 45–65 dB too hot.

**You need roughly 20–30 dB of passive attenuation.** There is no setting on either
box that provides it without a penalty:

- Turning the WING down → wrecks signal-to-noise, amplifies the hum *(what you have now)*
- Turning the GoStream preamp down → the input stage is already clipping before the gain control
- Turning PGM down → the clipping happened upstream; you just get quieter distortion

---

## The fix: two passive DI boxes, used in reverse

A passive DI does three things at once, and all three are what you need:

1. **Transformer isolation** — physically breaks the ground path between the console
   and the switcher. This is what kills the hum.
2. **Passive attenuation of 20–30 dB** — takes +4 dBu line level down to the mic level
   the GoStream wants, with **no added noise**, because a transformer has no noise
   floor of its own.
3. **A ground lift switch** — a second line of defence if the hum persists.

And a transformer is unbothered by phantom power, so even if the GoStream's mic input
is left on Condenser, nothing is harmed.

### Wiring

```
WING XLR OUT 4  ──►  DI box 1 input  ──XLR──►  GoStream Mic 1
WING XLR OUT 5  ──►  DI box 2 input  ──XLR──►  GoStream Mic 2
                     (ground lift engaged)
```

Most passive DIs have a ¼" input, so you need two **XLR-female to ¼" TS** cables or
adapters. Many DIs also have an XLR "thru" input — check yours; if so, no adapter is
needed.

### What to buy

| Option | Notes |
|---|---|
| **Radial ProAV2** | Stereo, one box, built precisely for this job — device output into a mixer. Ground lift, attenuation, excellent transformers. **This is what I would buy.** |
| Radial ProD2 | Stereo passive DI, same principle |
| 2× Whirlwind IMP 2 | Inexpensive, well made, widely available |
| 2× Behringer DI20 or Ultra-DI DI400P | Budget option. Works. Not as quiet as the Radials, but far quieter than what you have now. |

If your DI has an input pad switch, start at **−20 dB** and adjust from there.

### Then reset the levels properly

Once the DIs are in:

1. **WING Matrix 5 output trim back to 0 dB.** The console should run at its proper
   operating level — that is where its signal-to-noise is best.
2. **GoStream: Mic Type `Line` if offered**, otherwise Dynamic (XLR). Not Condenser.
3. **GoStream preamp: 0 dB** on both channels.
4. **GoStream faders: −10 dB**, identical on both.
5. Raise the WING's Matrix 5 trim only if the GoStream meters read low — target
   **−12 dB average, −6 dB peaks**, clip indicators dark on the loudest worship.

You should now have a clean, quiet, properly-levelled feed with a real stereo image.

---

## Before you buy: find out where the hum actually is

Twenty minutes of testing. Do this so you know the DI will fix it rather than hoping.

### Test 1 — is the hum in the audio cable, or already in the console?

Put headphones on the **WING** and solo **Matrix 5**.

- **Hum present on the console?** The problem is upstream — on the console or the
  stage. A DI will not fix it. Skip to "If the hum is on the console" below.
- **Console clean, hum only in the stream?** It is a ground loop between the WING and
  the GoStream. The DI is the fix.

### Test 2 — which device is completing the loop?

With the system running and the hum audible, disconnect these **one at a time** and
listen after each:

| Disconnect | If the hum stops |
|---|---|
| The audio cables to the GoStream | The loop is the audio path → **DI boxes** |
| The Mac's USB from the WING | The Mac is the loop → **USB isolator**, or run the Mac on battery to confirm |
| Each HDMI camera cable in turn | That camera's path is the loop → HDMI isolator, or re-route its power |
| The GoStream's network cable | The network is the loop → fibre or an ethernet isolator |

### Test 3 — power

Put the **WING and the GoStream on the same power strip, on the same circuit.**
Ground loops form when two connected devices sit on different mains earths. This is
free, takes two minutes, and sometimes solves it outright.

**Never lift a mains earth to solve hum.** It is dangerous and illegal in most
jurisdictions. Lift the *signal* ground on a DI, never the safety earth on a plug.

### If the hum is on the console itself

Then it is coming from the stage, not the video chain. Likely causes:

- A DI or instrument on stage with a ground problem — mute channels one at a time to
  find it
- Lighting dimmers or LED drivers near audio cable runs
- An unbalanced cable somewhere in the stage patch
- A guitar amp — classic; a hum that changes when the player touches their strings

---

## Why this will not be fixed by settings

I want to be plain about this, because it has cost you several rounds already.

You are connecting a professional balanced line output to a compact switcher's
microphone input. That interface is a **20–30 dB level mismatch and a shared ground
path**. Neither box has a control that fixes either one. Every adjustment available
to you trades one problem for the other:

- Turn it down at the console → quieter, but the hum and noise come up with it
- Turn it up at the console → cleaner signal-to-noise, but it clips
- There is no setting in between where both are acceptable

A transformer solves both simultaneously and permanently, which is exactly why every
professional install has one at this junction.

**This is the last piece of hardware your broadcast chain needs.** It is also, per
pound spent, the biggest audible improvement left in the entire system.

---

## Checklist once the DIs arrive

- [ ] WING XLR out 4 → DI 1 → GoStream Mic 1
- [ ] WING XLR out 5 → DI 2 → GoStream Mic 2
- [ ] Ground lift **engaged** on both DIs
- [ ] WING Matrix 5 output trim back to **0 dB**
- [ ] GoStream Mic Type: **Line** (or Dynamic if there is no Line option)
- [ ] GoStream preamps: **0 dB** both
- [ ] GoStream faders: **−10 dB** both, identical
- [ ] Panning: Mic 1 **−100**, Mic 2 **+100**
- [ ] PGM fader back to **0 dB**, limiter **ON** at **−3 dB**
- [ ] Loudest worship material: **no red clip indicators anywhere**
- [ ] Listen on headphones from the actual stream — hum gone, stereo image correct
- [ ] Record the final Matrix 5 trim value: `______ dB`
