# 08 — Monitors, IEMs & Feedback Control

## Principle

**Musicians mix for themselves; FOH mixes for the congregation.** Every monitor bus
is **pre-fader**, so nothing you do at FOH changes what a musician hears. Their mix
is theirs.

## Monitor assignments

| Bus | Mix | For | Format |
|---|---|---|---|
| 1 | IEM WL | Worship leader | Stereo IEM |
| 2 | IEM BGV | BGV 1–3 (shared) | Stereo IEM |
| 3 | IEM KEYS | Keys player | Stereo IEM |
| 4 | IEM BASS | Bass player | Stereo IEM |
| 5 | IEM EG | Electric guitarist | Stereo IEM |
| 6 | IEM DRUMS | Drummer | Stereo IEM |
| 7–8 | Spare | Guest musicians | Stereo IEM |
| 9 | WEDGE PULPIT | Pastor / speaker | Mono wedge |
| 10 | WEDGE STAGE | Stage fill | Mono wedge |

---

## IEM starting mixes

Build each mix from the musician's own instrument outward. Give them what they need
to play in time and in tune, not a miniature FOH mix.

### Bus 1 — Worship Leader
| Source | Level |
|---|---|
| Own vocal (ch 25) | **0 dB — loudest thing in the mix** |
| Click (ch 32) | −6 dB |
| Cues (ch 24) | −8 dB |
| BGVs | −12 dB |
| Acoustic gtr | −8 dB |
| Keys / pads | −10 dB |
| Kick + snare | −12 dB |
| Bass | −12 dB |
| Ambience (ch 41–42) | **−18 dB** — critical for IEM users, or they feel sealed off from the room |
| Talkback (Aux 5) | −6 dB |

### Bus 2 — BGVs
| Source | Level |
|---|---|
| Own vocals (ch 26–28) | 0 dB |
| Worship leader | −4 dB |
| Click | −8 dB |
| Keys / pads | −8 dB |
| Kick + snare | −12 dB |
| Bass | −10 dB |
| Ambience | −18 dB |

### Bus 3 — Keys
| Source | Level |
|---|---|
| Own keys (ch 19–22) | 0 dB |
| Click | −4 dB |
| Cues | −6 dB |
| Kick + snare | −8 dB |
| Bass | **−6 dB** — keys and bass must lock |
| Worship leader | −6 dB |
| Tracks | −8 dB |
| Ambience | −18 dB |

### Bus 4 — Bass
| Source | Level |
|---|---|
| Own bass (ch 13) | 0 dB |
| **Kick (ch 1–2)** | **−4 dB — the most important relationship on stage** |
| Click | −4 dB |
| Snare | −10 dB |
| Keys | −10 dB |
| Worship leader | −8 dB |
| Ambience | −18 dB |

### Bus 5 — Electric Guitar
| Source | Level |
|---|---|
| Own guitar (ch 15/16) | 0 dB |
| Click | −6 dB |
| Cues | −8 dB |
| Drums (kick, snare, OH) | −8 dB |
| Bass | −8 dB |
| Worship leader | −6 dB |
| Ambience | −18 dB |

### Bus 6 — Drums
| Source | Level |
|---|---|
| **Click (ch 32)** | **−2 dB — the drummer needs it clearest of anyone** |
| Cues | −6 dB |
| Own kit | −6 dB (they hear it acoustically too) |
| Bass | **−4 dB** |
| Worship leader | −8 dB |
| Keys / tracks | −10 dB |
| Ambience | −16 dB |

### Bus 9 — Pulpit Wedge (speech)
| Source | Level |
|---|---|
| Pastor headset (ch 33) | −10 dB |
| Lectern (ch 37) | −10 dB |
| Handhelds | −12 dB |
| Media (ch 45–46) | −8 dB |
| **Music** | **−18 dB or off** |
| **Everything else** | **OFF** |

Keep this wedge as sparse as possible. Every extra open source in a wedge pointed at
an open microphone is feedback waiting to happen.

---

## The ambience-in-IEMs rule

Musicians in sealed in-ears are acoustically cut off from the congregation. They
cannot hear the room singing, they cannot hear applause, and they cannot feel the
service. This makes them play worse and lead worse.

**Every IEM mix gets the ambience mics at around −18 dB.** It is the difference
between a band playing *at* a congregation and a band worshipping *with* one. It
costs nothing and it is the most appreciated thing you can do for your musicians.

---

## Feedback control

### Ringing out a system — do this once, properly, at commissioning

1. Everyone off the stage, all channels muted.
2. Unmute **one** microphone. Place it where it will actually be used.
3. Raise its wedge or PA send slowly until it just begins to ring.
4. Identify the ringing frequency — use the WING's RTA with the channel soloed.
5. Apply a **narrow cut** (Q 8–10) of 3–6 dB at that frequency.
6. Raise the level again. Find the next ring. Repeat.
7. **Stop after 4–5 notches per channel.** More than that and you are destroying
   the tone of the microphone to solve a placement problem.
8. Pull back 6 dB from the ring point. That is your working headroom.
9. Record the notch frequencies in the table below.

### Notch log

| Channel | Notch 1 | Notch 2 | Notch 3 | Notch 4 | Date set | By |
|---|---|---|---|---|---|---|
| Ch 33 Pastor Headset | | | | | | |
| Ch 34 Pastor Lav | | | | | | |
| Ch 35 Handheld 1 | | | | | | |
| Ch 36 Handheld 2 | | | | | | |
| Ch 37 Lectern | | | | | | |
| Ch 43/44 Choir | | | | | | |
| Bus 9 Pulpit Wedge | | | | | | |
| Bus 10 Stage Wedge | | | | | | |

### Feedback frequency guide

| Ringing sounds like | Frequency range | First move |
|---|---|---|
| Low rumble / howl | 100–250 Hz | Raise the channel HPF |
| Boxy "woof" | 250–500 Hz | Narrow cut; check the mic is not near a hard surface |
| Honk | 500 Hz–1 kHz | Narrow cut; check wedge angle |
| Ring / "eee" | 1–4 kHz | Narrow cut; this is the most common band |
| Whistle / "sss" | 4–8 kHz | Narrow cut; check mic placement relative to the horn |

### Feedback prevention, in order of effectiveness

1. **Microphone placement.** Get the mic closer to the source and further from the
   speakers. Nothing else comes close.
2. **Turn things off.** Every open mic adds 3 dB of feedback risk per doubling.
   Automix (doc 04) does this automatically for speech.
3. **HPF on every channel.** Free gain-before-feedback.
4. **Narrow notch filters.** Surgical, not broad.
5. **Lower the monitor.** Musicians would rather hear a little less than have the
   service interrupted.
6. **Move to in-ears.** The permanent fix. Wedges pointed at open microphones are a
   problem you manage; in-ears are a problem you eliminate.

### If it feeds back mid-service

1. **Pull the master down 10 dB immediately.** Do not hunt for the channel first —
   stop the noise, then diagnose. A ringing PA is painful and frightening.
2. Identify the offending channel (usually the mic nearest a speaker, or the one
   just unmuted).
3. Mute it or lower it.
4. Bring the master back up.
5. **Note it in the service log** and fix the root cause during the week.

Never let a feedback event pass without writing it down. Recurring feedback is
always a system problem, never bad luck.
