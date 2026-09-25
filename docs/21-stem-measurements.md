# 21 — Stem Measurements

Measured from the nine WAV files supplied with the Logic broadcast template.
All are **24-bit / 48 kHz mono**, roughly 30 seconds each.

**What these are:** the template's own reference stems, named exactly as the
`.logicx` project references them. They are **not** recordings of your band or your
room. They tell us what material the template's processing was tuned against — which
is genuinely useful for gain staging, and not useful for judging GHC's sources.

| Stem | Peak | RMS | Crest | Sub | Low | Lo-mid | Mud | Mid | Up-mid | Presence | Edge | Air |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Bass DI | −8.8 | −15.5 | 6.8 | −16.9 | **−3.3** | −4.5 | −11.8 | −13.0 | −14.6 | −19.6 | −35.5 | −52.6 |
| Bass Mic | −6.6 | −15.5 | 8.9 | −26.6 | **−2.6** | −3.8 | −16.9 | −23.2 | −25.5 | −27.2 | −43.0 | −55.4 |
| AG 1 | −8.4 | −25.9 | **17.6** | −36.2 | −14.0 | −4.9 | −5.5 | −9.1 | −10.9 | −12.1 | −12.1 | **−17.1** |
| EG 1L | −10.2 | −21.7 | 11.5 | −43.3 | −27.4 | −14.1 | −7.3 | −5.6 | **−5.0** | −7.6 | −20.0 | −39.0 |
| EG 1R | −11.2 | −21.2 | 9.9 | −37.6 | −22.6 | −11.5 | **−4.5** | −5.5 | −6.7 | −12.0 | −20.0 | −42.6 |
| EG 2L | −11.2 | −20.4 | 9.3 | −40.0 | −27.0 | −12.7 | −5.9 | **−5.0** | −5.2 | −11.7 | −23.9 | −42.3 |
| EG 2R | −11.2 | −21.1 | 9.9 | −28.8 | −19.4 | −9.7 | **−5.4** | −6.2 | −6.8 | −8.8 | −19.4 | −39.4 |
| Crowd 1 R | −8.5 | −23.9 | 15.4 | −32.2 | −13.0 | −6.3 | −7.9 | **−4.6** | −8.0 | −15.1 | −19.0 | −27.8 |
| Crowd 2 L | −7.0 | −21.0 | 14.0 | **−12.4** | **−5.0** | −6.6 | −10.7 | −6.8 | −10.8 | −16.9 | −20.8 | −30.2 |

*Peak and RMS in dBFS. Band figures are energy relative to each stem's own total, in
dB — they describe tonal shape, not level. Silence below −60 dBFS excluded from RMS.*

Band definitions: sub 20–60 · low 60–120 · lo-mid 120–250 · mud 250–500 ·
mid 500–1k · up-mid 1–2k · presence 2–4k · edge 4–8k · air 8–16k Hz.

---

## What this confirms

### 1. The gain-staging spec is right

Peaks land between **−6.6 and −11.2 dBFS**; RMS between **−15.5 and −25.9 dBFS**.
That is almost exactly the target stated throughout this repository: **peaks at
−10 dBFS, average around −18 dBFS.** The template was built against material staged
this way, so its thresholds and ratios assume it. Keep your preamps there and the
processing behaves as designed.

### 2. Crowd mics need an aggressive high-pass

**Crowd 2 has extraordinary low-frequency content** — sub at −12.4 dB and low at
−5.0 dB relative to its own total. That is the most low-end energy of any stem here,
including both bass tracks. In a congregation mic that is not music; it is HVAC
rumble, footfall, stage spill and handling.

Your console already has channels 29 and 30 high-passed at **254 Hz, 24 dB/oct**,
which is correct and slightly unusual — most churches leave crowd mics at 80 Hz and
then wonder why the stream sounds muddy. **Do not lower it.**

Note also how different the two crowd mics are: Crowd 1 is midrange-centred
(mid −4.6) while Crowd 2 is bass-heavy. If your two crowd mics differ like this,
they are not a matched stereo pair and should be treated individually before being
linked.

### 3. The acoustic guitar is the dynamics problem

AG 1 has a **crest factor of 17.6 dB** — by far the widest here — and the brightest
top end of anything measured (air −17.1, edge −12.1, both ~10 dB above the next
brightest source). That is a channel that will jump out of a broadcast mix and sting
on earbuds.

This supports what is already in the build: compression on the acoustic, and the
de-esser on the vocal group catching the same region.

### 4. The template expects stereo guitars, you have mono

Four separate electric guitar stems — EG 1L/1R and EG 2L/2R — and the pairs are
genuinely different, not a copied mono signal. EG 1L peaks in the up-mid (−5.0)
while EG 1R peaks in the mud band (−4.5). Real stereo miking or a stereo modeler.

**Your console has one electric guitar channel** (ch 9, from A-10). The template's
guitar handling therefore does not transfer directly. Nothing to fix — just do not
expect the template's stereo guitar width online, because the source is not there.

### 5. Bass DI and Bass Mic do opposite jobs

The DI carries the definition — mud −11.8, mid −13.0, presence −19.6. The mic
carries the weight — low −2.6, but mid −23.2, presence −27.2, a full 10 dB darker.

Worth knowing if you ever add a bass amp mic. Your current single bass channel
(ch 8, from A-9) has to do both jobs, which is why the **800 Hz definition band
matters so much** on that channel — it is the only thing a phone speaker will
reproduce.

---

## What this does not tell us

These stems are the template's reference material from another room and another
band. They say nothing about:

- How your room sounds
- How your band plays
- Whether your gain structure is actually set correctly today
- What your crowd mics are picking up

To learn any of that, record one Sunday's 40 channels in Logic and measure those.
That is a genuinely worthwhile exercise and the multitrack recording is already
running every week.
