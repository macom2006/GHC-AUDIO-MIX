# WING OSC Address Reference — GHC

Derived from the GRACELAND console's own snapshot (serial S240100078BV2, fw 3.1-0).
Default OSC port **2223**, UDP. **Index numbers are not zero-padded** (`/ch/1`, not `/ch/01`).

Full machine-readable map, all 860 parameters: [`wing-osc-map.json`](wing-osc-map.json)

| Section | Range |
|---|---|
| `/ch/<n>` | 1 – 40 |
| `/aux/<n>` | 1 – 8 |
| `/bus/<n>` | 1 – 16 |
| `/main/<n>` | 1 – 4 |
| `/mtx/<n>` | 1 – 8 |
| `/dca/<n>` | 1 – 16 |
| `/mgrp/<n>` | 1 – 8 |
| `/fx/<n>` | 1 – 16 |

## Channel

| Address | Type | Meaning |
|---|---|---|
| `/ch/<n>/fdr` | f | fader in dB |
| `/ch/<n>/mute` | i | 1 = muted |
| `/ch/<n>/name` | s | channel name |
| `/ch/<n>/pan` | i | pan |
| `/ch/<n>/flt/lc` | i | high-pass on |
| `/ch/<n>/flt/lcf` | f | high-pass Hz |
| `/ch/<n>/flt/lcs` | s | slope: 6/12/18/24 |
| `/ch/<n>/in/conn/grp` | s | source group: A/LCL/USB/AUX/OFF |
| `/ch/<n>/in/conn/in` | i | source port number |
| `/ch/<n>/in/set/trim` | f | digital trim dB |

## Channel sends

| Address | Type | Meaning |
|---|---|---|
| `/ch/<n>/send/<b>/lvl` | f | send to bus b, dB |
| `/ch/<n>/send/<b>/on` | i | send on/off |
| `/ch/<n>/send/<b>/mode` | s | PRE or POST |
| `/ch/<n>/main/<m>/lvl` | f | send to main m, dB |
| `/ch/<n>/main/<m>/on` | i | main assign on/off |

## Channel EQ

| Address | Type | Meaning |
|---|---|---|
| `/ch/<n>/eq/on` | i | EQ in/out |
| `/ch/<n>/eq/<b>g` | f | band b gain dB (1-6) |
| `/ch/<n>/eq/<b>f` | f | band b frequency Hz |
| `/ch/<n>/eq/<b>q` | f | band b Q |
| `/ch/<n>/eq/lg` | f | low shelf gain |
| `/ch/<n>/eq/hg` | f | high shelf gain |

## Channel dynamics

| Address | Type | Meaning |
|---|---|---|
| `/ch/<n>/gate/on` | i | gate in/out |
| `/ch/<n>/gate/thr` | f | gate threshold dB |
| `/ch/<n>/dyn/on` | i | comp in/out |
| `/ch/<n>/dyn/thr` | f | comp threshold dB |
| `/ch/<n>/dyn/ratio` | f | ratio |
| `/ch/<n>/dyn/att` | f | attack ms |

## Bus / Main / Matrix

| Address | Type | Meaning |
|---|---|---|
| `/bus/<n>/fdr` | f | bus fader dB |
| `/bus/<n>/mute` | i | bus mute |
| `/bus/<n>/name` | s | bus name |
| `/bus/<n>/send/MX<m>/lvl` | f | bus to matrix m |
| `/main/<n>/fdr` | f | main fader dB |
| `/main/<n>/send/MX<m>/lvl` | f | main to matrix m |
| `/mtx/<n>/fdr` | f | matrix fader dB |
| `/mtx/<n>/in/set/trim` | f | matrix input trim dB |
| `/mtx/<n>/dly/on` | i | matrix delay on |
| `/mtx/<n>/dly/dly` | f | matrix delay value |

## DCA / mute groups / FX

| Address | Type | Meaning |
|---|---|---|
| `/dca/<n>/fdr` | f | DCA fader dB |
| `/dca/<n>/mute` | i | DCA mute |
| `/dca/<n>/name` | s | DCA name |
| `/mgrp/<n>/mute` | i | mute group active |
| `/fx/<n>/mdl` | s | FX model name |
| `/fx/<n>/<band>` | f | GEQ band, e.g. /fx/7/2k |

## Global

| Address | Type | Meaning |
|---|---|---|
| `/cfg/amix/x` | i | automix group X on |
| `/io/altsw` | i | alt source (virtual soundcheck) |

