# 38 — Riding stream vocal level without touching FOH

## The control

**Bus 13 "BC VOX" → Bus 7 "BROADCAST" send.** As shipped in V11: **−2.0 dB**.

On the desk: select **Bus 7 (BROADCAST)**, press **SENDS** for sends-on-fader,
then ride the **BC VOX** fader. Or Bus layer → BC VOX → SENDS tab → BROADCAST.

## Why it does not touch FOH

| Path | Carries | Controlled by |
|---|---|---|
| Channel fader → Main 1 | FOH vocals | Channel faders |
| Channel send (post-fader, 0 dB) → Bus 13 → Bus 7 | Stream vocals | **Bus 13 → Bus 7 send** |

Bus 13 has all four main sends OFF and is not patched to any physical output.
It feeds Bus 7 and nothing else. Verified against `GHC BROADCAST V11.snap`.

## What is in BC VOX

ch 13, 14, 15, 16 (Vox 1–4), 20 (LEAD2), 22 (Raissa), 24 (Wireless 3),
25 (Jude), 26 (Brenda), 27 (Wireless 4) — all post-fader at 0 dB, except
LEAD2 at +2.

## What is NOT in it

**Pastor (ch21) and House (ch23) go direct to Bus 7 at +3 dB.** Speech is not
affected by this fader — which is what you want. If speech also needs to come
down, that is the channel's own Bus 7 send, not BC VOX.

## The reverb caveat

Vocal reverb reaches the stream on its own path:

| Bus | → Bus 7 |
|---|---|
| 15 Vox Verb | −1.0 |
| 12 Delay | (via its own send) |
| 16 Slap | muted since V9 |

Pull BC VOX 3 dB and the stream gets relatively wetter. Pull **Bus 15 → Bus 7**
by the same amount if you want the reverb to track the dry level.

## Starting point

−2.0 → **−5.0 dB**. Listen to one song before going further.
