# 09 — FX Rack

Effects serve the mix. They are not decoration, and on a church PA they are used
far more sparingly than most operators expect.

## FX assignments

| Slot | Effect | Fed by | Returns to | Use |
|---|---|---|---|---|
| **1** | **Vocal Hall reverb** | Bus 11 | Main 1, Main 2 | Worship leader, lead vocals |
| **2** | **Vocal Plate reverb** | Bus 12 | Main 1, Main 2 | BGVs, choir |
| **3** | **Vocal Delay** | Bus 13 | Main 1, Main 2 | Worship leader on big moments |
| **4** | **Drum Room** | Bus 14 | Main 1, Main 2 | Snare, toms |
| 5 | Short Room (broadcast) | Bus 16 | **Main 2 only** | Speech — tiny amount, stream only |
| 6 | Channel de-esser | Insert on ch 25 | — | Worship leader sibilance |
| 7 | Channel de-esser | Insert on ch 33 | — | Pastor headset sibilance |
| 8 | 31-band GEQ | Insert on Matrix 1 | — | House room correction |
| 9 | 31-band GEQ | Insert on Bus 9 | — | Pulpit wedge ringing out |
| 10 | 31-band GEQ | Insert on Bus 10 | — | Stage wedge ringing out |
| 11 | Multiband / bus comp | Insert on Main 2 | — | Broadcast glue (doc 07) |
| 12 | True-peak limiter | Insert on Matrix 6 | — | Broadcast safety (doc 07) |
| 13 | Limiter | Insert on Matrix 1 | — | PA protection |
| 14–16 | Spare | | | Guest artists, special events |

> Slot counts and which engines can host "premium" processors vary by WING model and
> firmware. Verify the available slots on your desk and adjust this table — the
> assignments matter more than the slot numbers.

---

## Effect settings

### FX1 — Vocal Hall (Bus 11)
| Parameter | Value |
|---|---|
| Type | Hall / Ambience |
| Pre-delay | **20 ms** — keeps the vocal's consonants clear of the reverb |
| Decay | **1.4 s** |
| HPF on return | 300 Hz — no low-end wash |
| LPF on return | 8 kHz — keeps the reverb behind the dry vocal |
| Diffusion | Medium-high |
| Returns to | Main 1 and Main 2 |

### FX2 — Vocal Plate (Bus 12)
| Parameter | Value |
|---|---|
| Type | Plate |
| Pre-delay | 10 ms |
| Decay | **1.0 s** |
| HPF on return | 350 Hz |
| LPF on return | 10 kHz |
| Use | BGVs and choir — shorter and brighter than the hall, so the group blends without smearing |

### FX3 — Vocal Delay (Bus 13)
| Parameter | Value |
|---|---|
| Type | Stereo delay |
| Time | **Tap to tempo — 1/4 note** |
| Feedback | 15–20% (2–3 repeats maximum) |
| HPF on return | 400 Hz |
| LPF on return | 6 kHz — dark repeats sit behind the vocal |
| Use | Ride this send. Push it at the end of a phrase, pull it back for the next line. A delay left permanently up turns into mud. |

### FX4 — Drum Room (Bus 14)
| Parameter | Value |
|---|---|
| Type | Room |
| Pre-delay | 5 ms |
| Decay | **0.6 s** |
| HPF on return | 200 Hz |
| LPF on return | 12 kHz |
| Fed by | Snare (−8 dB), toms (−10 dB) |
| Use | Subtle. It should disappear when you mute it and the kit should sound smaller. |

### FX5 — Short Room, broadcast only (Bus 16)
| Parameter | Value |
|---|---|
| Type | Small room |
| Pre-delay | 5 ms |
| Decay | **0.5 s** |
| HPF on return | 400 Hz |
| LPF on return | 5 kHz |
| Return assigned to | **Main 2 only** |
| Fed by | Speech channels at −24 dB |
| Purpose | Stops the sermon sounding like a voiceover booth online. Almost inaudible when set correctly. |

---

## Rules for FX

1. **No reverb on speech in the house.** None. It destroys intelligibility in a room
   that already has reverberation of its own.
2. **FX sends are post-fader.** Pull a channel down and its effect follows.
3. **Always high-pass and low-pass the returns.** An unfiltered reverb return is the
   most common source of unexplained mix mud.
4. **If muting the FX makes the mix clearer, it was too loud.** Check this every
   soundcheck: mute all FX, listen, unmute. The difference should be a pleasant
   sense of space, not a dramatic change.
5. **Delay is for moments, not for songs.** Ride it.
6. **The broadcast gets more reverb than the house.** Always. The room is doing the
   work in one and nothing in the other.

## FX return levels — starting points

| Return | House (Main 1) | Broadcast (Main 2) |
|---|---|---|
| FX1 Vocal Hall | −12 dB | **−9 dB** |
| FX2 Vocal Plate | −14 dB | −11 dB |
| FX3 Vocal Delay | −18 dB | −15 dB |
| FX4 Drum Room | −16 dB | −13 dB |
| FX5 Speech Room | **Not assigned** | −24 dB |

All FX returns are members of **DCA 9** so they can be pulled together instantly —
useful when a spoken moment arrives unexpectedly during a worship set.
