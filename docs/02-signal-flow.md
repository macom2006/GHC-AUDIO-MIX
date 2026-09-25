# 02 — Signal Flow

## End-to-end block diagram

```
STAGE                          FOH                                  DESTINATIONS
─────                          ───                                  ────────────

 Mics & DIs                ┌──────────────────────────────┐
 ──────────►  S32 ═══AES50-A══►│  WING — 48 input channels    │
 (32 ch)      stage box        │                              │
                               │  Preamp → Filter → Gate →    │
 FOH mics  ──────────────────► │  EQ → Comp → Sends           │
 (local 1-8)                   │                              │
                               └───┬──────────┬───────────┬───┘
                                   │          │           │
                    ┌──────────────┘          │           └──────────────┐
                    │                         │                          │
             ┌──────▼──────┐          ┌───────▼───────┐        ┌─────────▼────────┐
             │  MAIN 1     │          │   MAIN 2      │        │  BUS 1–10        │
             │  HOUSE LR   │          │  BROADCAST LR │        │  IEM + WEDGES    │
             └──────┬──────┘          └───────┬───────┘        └─────────┬────────┘
                    │                         │                          │
        ┌───────────┼───────────┐             │                    S32 outputs
        │           │           │             │                    → IEM racks
        ▼           ▼           ▼             ▼                    → wedge amps
     MTX 1       MTX 2       MTX 3/4/5     MTX 6
    PA L/R       SUBS        FILLS,        BROADCAST
   +room EQ    (aux-fed     LOBBY,         +delay
   +delay       from        NURSERY        +limiter
   +limiter     Bus 15)                        │
        │           │           │              │
        ▼           ▼           ▼              ▼
    MAIN PA      SUBS        ZONES         OSEE SWITCHER ──► STREAM
                                                │
                                                └──► (alt) OBS via USB

                               ┌──────────────────────────────┐
                               │  USB-B 48×48 → LOGIC PRO     │  ◄── multitrack record
                               │  WING-LIVE SD → 64 ch backup │      + virtual soundcheck
                               └──────────────────────────────┘
```

## Channel processing order (WING input strip)

```
Source select ──► Preamp gain ──► Trim ──► Polarity ──► Filters (HPF/TLF/LPF)
   │
   └──► Insert A ──► Gate/Expander ──► EQ (6-band) ──► Compressor ──► Insert B
            │
            └──► Sends:  Main 1 (house, own level + pan)
                         Main 2 (broadcast, own level + pan)
                         Main 3 (spare/zone)
                         Main 4 (record/spare)
                         Bus 1–16 (pre or post fader, per send)
                         Direct out → USB / SD recorder
```

**Key point for operators:** the fader you touch is the *channel* fader, which
feeds Main 1 and Main 2 through **separate, independently adjustable sends**. Pull
the vocal down for the room and it does not automatically come down on the stream.
That is the feature, not a bug — and it is the thing new operators get wrong.

## Clocking

| Setting | Value | Why |
|---|---|---|
| Sample rate | **48 kHz** | Video standard. Never 44.1 kHz — it will drift against the Osee. |
| Clock master | **WING internal** | The console is the master for everything. |
| S32 stage box | Slave via AES50-A | Clock follows AES50 automatically. |
| Logic Pro | Slave to WING over USB | In Logic: set the WING as the audio device; do not enable external sync sources. |
| Osee switcher | Slave (embedded audio) or async (analog in) | Analog input is immune to clock drift — one more reason to prefer it. |

**Clocking failure symptom:** periodic clicks or ticks every few seconds, on all
channels at once. Check that nothing else is trying to be clock master.

## Latency budget

| Stage | Typical latency | Notes |
|---|---|---|
| WING A/D → D/A (local) | ~0.8 ms | Console through-latency |
| AES50 stage box round trip | ~1.0 ms | Adds to the above |
| Console total, mic to output | **~1.8 ms** | Imperceptible; IEMs are safe |
| Plugin inserts / premium FX | 0–2 ms | Keep off IEM paths if possible |
| PA processing (external DSP, if any) | 1–3 ms | Measure it; add to the delay ring calculation |
| Osee video processing | 1–3 frames (~33–100 ms) | **This is what breaks lip-sync — see doc 11** |

**Rule:** total mic-to-ear latency for in-ear monitoring must stay under **5 ms**.
Anything more and vocalists will hear a comb-filtered doubling against the sound
conducted through their own skull, and they will pull an earpiece out.

## Redundancy and failure paths

| Failure | Consequence | Mitigation in this design |
|---|---|---|
| AES50-A cable fails | All 32 stage inputs lost | Keep a spare Cat5e run taped to the snake path; AES50-B is wired and free |
| Console PSU fails | Total loss | WING has dual PSU on full-size model — both must be plugged into **different circuits** |
| Logic Pro crashes | Recording lost | WING-LIVE SD card records in parallel, independently |
| Stream computer fails | Stream lost, house unaffected | House PA is fed from Matrix 1, entirely independent of the broadcast chain |
| Operator error mid-service | Wrong mix live | Scene recall with scoped safes — see doc 12 |

**Never** run the house PA through the streaming computer. The house is the primary
product; it must survive every failure in the broadcast chain.
