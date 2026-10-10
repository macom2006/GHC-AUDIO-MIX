# 34 — Measurement of `S_Mason_Rd_3.m4a`

16.0 s · AAC 133 kbps · 48 kHz stereo · measured 2026-10-10

**I cannot listen to audio.** What follows is measurement, not an opinion on how it
sounds. The numbers are solid; the interpretation depends on things only you know —
see "What I need from you" at the end.

---

## Headline numbers

| Measurement | Result | Target | Verdict |
|---|---|---|---|
| **Integrated loudness** | **−12.5 LUFS** | −16 LUFS | **3.5 LU too loud** |
| **True peak** | **+0.1 dBTP** | −1.5 dBTP | **Over full scale — clipping** |
| Sample peak | 0.1 dBFS | — | 7 samples at full scale |
| Consecutive clipped runs | 0 | — | No sustained flat-topping |
| RMS | −18.0 dBFS | — | |
| **Crest factor** | **18.1 dB** | 10–16 typical | **Not over-compressed** |
| Loudness range | 11.9 LU | 6–9 LU | Wider than ideal for a stream |
| Short-term range | −37.9 to −11.4 LUFS | — | 26 LU swing |
| **L/R correlation** | **0.791** | <0.98 | **Genuine stereo** |
| Side vs mid energy | −9.2 dB | — | Real width |

---

## The three things that are definitely true

### 1. It is clipping, and it is too loud

**True peak +0.1 dBTP** with seven samples at full scale. Anything at or above
0 dBFS is clipping into the encoder, and a lossy codec makes it worse — AAC
overshoots on reconstruction, so peaks that just touch 0 in the file land above it
on playback.

At **−12.5 LUFS** it is also 3.5 LU hotter than the −16 target. Streaming platforms
normalise, so the extra loudness buys nothing and costs headroom.

### 2. The stereo problem is fixed

Correlation 0.791 with side energy 9.2 dB below mid. **This is genuine stereo.** The
collapsed-mono fault from the GoStream panel is gone — whoever set Mic 2 to +100 did
it correctly.

### 3. It is NOT over-compressed — and that corrects something I told you

**Crest factor 18.1 dB.** A heavily limited broadcast mix measures 8–12 dB. This
material is dynamic and breathing.

In `33-stream-eq-and-comfort.md` I said the limiter was "working constantly" and that
this was the cause of listening fatigue. **On the evidence of this recording, that
was overstated.** The material is not squashed. A few transients are hitting the
ceiling, but the body of the mix is not being crushed.

That changes the prescription: the fix is **headroom and ceiling**, not less
compression. V9's removal of the +3 dB limiter drive is still correct — it stops the
peaks slamming — but I should not have characterised the whole mix as over-limited.

---

## The spectral balance — and why I will not draw a conclusion from it

Octave-band energy:

| Band | Level |
|---|---|
| 125–250 Hz | **63.8 dB** ← dominant |
| 250–500 Hz | 54.9 dB |
| 500 Hz–1 kHz | 52.5 dB |
| 1–2 kHz | 44.7 dB |
| **2–4 kHz** | **34.9 dB** ← lowest in the whole spectrum |
| **4–8 kHz** | **54.0 dB** ← jumps back up 19 dB |
| 8–16 kHz | 44.5 dB |

A **29 dB gap between the low-mids and the 2–4 kHz band**, with the energy jumping
19 dB back up above it, is not a shape any console setting in your file explains.
Your PA graphics cut 2 kHz by 4.5 dB and the broadcast bus *boosts* 3.5 kHz.

So one of these is true, and I cannot tell which from the file alone:

1. **This clip simply has no 2–4 kHz content** — mostly bass and drums, no lead
   vocal or speech in these 16 seconds. Then the "hole" is the content, not the system.
2. **It is not a recording of the stream** — a phone in the room, or a camera, whose
   own microphone and processing produced this curve.
3. Something in the signal chain really is doing this, in which case speech
   intelligibility would be severely compromised and people would be complaining
   loudly about not hearing the sermon.

Given nobody has reported that, **(1) or (2) is far more likely than (3).**

### The 6.2 kHz event

There is a narrow peak at **6177 Hz** standing 41 dB above its neighbours. Its shape
at the strongest point:

```
 -0.6 s  -4.6 dB
 -0.3 s  -1.0 dB      builds over about half a second
  0.0 s   0.0 dB
 +0.3 s  -1.3 dB      holds within ~1 dB for ~0.5 s
 +0.5 s  -19.2 dB     then stops abruptly
```

**Build, plateau, abrupt stop** is not a cymbal — a cymbal is instant attack and
exponential decay. It is consistent with either a feedback tone being held at a
ceiling by the limiter, or a sustained sibilant or synth wash.

**I am not calling this feedback.** It is present at full strength only 28% of the
clip and I do not know what is playing. But **6 kHz is squarely in the whistle band**,
and if your ring-out finds something near 6.2 kHz, this measurement supports it.

Treat it as a lead for the ring-out, not a diagnosis.

---

## What I need from you

Three answers would turn this from measurement into diagnosis:

1. **What is this a recording of?** The live stream as a viewer receives it, a phone
   held up in the room, or a console export? The answer changes everything above.
2. **Before or after loading V9?** If before, the clipping confirms V9 was needed. If
   after, V9 did not solve it and I need to look again.
3. **What is happening in those 16 seconds?** Full band, worship with vocals,
   speech, walk-in music?

The most useful recording you could send me is **the stream itself, captured from
the viewer's end, with a sermon passage and a worship chorus in the same clip.**
That lets me check speech-to-music loudness matching, which is the complaint most
likely to be driving people away.
