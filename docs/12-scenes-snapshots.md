# 12 — Scenes & Snapshots

A scene that surprises the operator is worse than no scene at all. Everything here
is about **predictable recall**.

## Show file

**Name:** `GHC-MASTER-SHOW`
Every service loads this show file. Never build a new one from scratch on a Sunday.

## Scene list

| # | Scene | When | What it sets |
|---|---|---|---|
| **1** | **DEFAULT / RESET** | Start of every session | The known-good state. All processing per doc 04, band and vox muted, speech ready, house master at −10. |
| 2 | PRE-SERVICE | 30 min before | Walk-in music from Aux 1–2, ambience up on Main 2, house at 72–76 dBA, all mics muted |
| 3 | WELCOME / ANNOUNCE | Service start | MG3 out (speech live), MG1+MG2 in (band and vox muted), media ready |
| **4** | **WORSHIP** | Worship set | MG1+MG2 out, band and vocals live, FX active, DCA1 speech pulled to −10, ambience at −12 on Main 2 |
| 5 | WORSHIP — QUIET | Reflective moments | As scene 4, drums and tracks down 6 dB, pads up 2 dB, reverb up 3 dB |
| 6 | PRAYER / ALTAR | Prayer, ministry | **MG6 in — ambience MUTED.** Speech live, band down to a pad only |
| **7** | **SERMON** | Preaching | MG1+MG2 in, DCA1 at 0 dB, automix active, ambience at −24 on Main 2, FX off except FX5 |
| 8 | VIDEO | Video playback | MG4 out (media live), everything else down, speech ready underneath |
| 9 | OFFERING / RESPONSE | Giving, response | Band live at a lower level, speech live, ambience at −15 |
| 10 | CLOSING | End of service | As scene 4 |
| 11 | POST-SERVICE | After dismissal | Walk-out music, ambience up, mics muted |
| 12 | SPECIAL EVENT | Concerts, weddings, funerals | Duplicate and modify — **never edit scenes 1–11 for a one-off** |

---

## Scope — what a scene is allowed to change

This is the most important page in this document. Get it wrong and a scene recall
will blow up a live service.

### Global safes (never recalled, ever)

| Safed | Why |
|---|---|
| **All preamp gains** | Gain is set for the person on the mic today. A scene must never change it. |
| **Phantom power states** | Switching phantom on a live mic makes a loud bang |
| **All output patching** | Physical routing does not change between scenes |
| **Matrix 1 room EQ** | Room correction is a property of the building |
| **Matrix 1 / 2 delays** | Physical alignment |
| **Matrix 6 broadcast delay** | Lip-sync alignment |
| **Main 1 master fader** | The operator owns the house level, always |
| **All monitor bus levels (Bus 1–10)** | **Musicians' mixes are theirs.** A scene recall must never change an in-ear mix mid-service. |
| Notch filters set during ring-out | Feedback protection |

### What scenes DO recall

- Channel fader levels (Main 1 and Main 2 sends)
- Mute states and mute group states
- DCA levels and assignments
- FX send levels and FX return levels
- Ambience channel levels
- Automix on/off

### Channel safes

| Channel | Safed from | Reason |
|---|---|---|
| Ch 33 Pastor Headset | Mute recall | Never accidentally muted by a scene change mid-sermon |
| Ch 34 Pastor Lav | Everything except mute | Backup must always be ready |
| Ch 24 Cues, Ch 32 Click | **Fully locked** | Must never be assigned to a main by any scene |
| Ch 41–42 Ambience | Main 1 assignment | Must never appear in the house PA |

---

## Operating rules

1. **Recall scenes between segments, not during them.** Recall while the pastor is
   walking to the platform, not while he is mid-sentence.
2. **Use a crossfade time of 1–2 seconds** where the console supports it. Instant
   jumps are audible and jarring.
3. **After recalling, look at the desk before you look at the room.** Confirm the
   mutes and DCAs are where you expect.
4. **Never edit a scene during a live service.** Make the adjustment on the faders,
   note it down, and store it after the service or at the mid-week rehearsal.
5. **Store after every service**, when something genuinely improved. Overwrite
   deliberately, never by reflex.

## Weekly scene maintenance

| When | Task |
|---|---|
| Mid-week rehearsal | Run virtual soundcheck (doc 10), refine scenes, store |
| After each service | Note any scene that fought you; fix it mid-week, not on Sunday |
| Monthly | Export the show file to USB and to the church file server |
| After firmware updates | **Verify every safe and every scope setting.** Firmware updates can reset them. Also re-verify that ch 24 and 32 are still unassigned from the mains. |

## Backups

| Backup | Frequency | Location |
|---|---|---|
| Show file to USB stick | Weekly | Kept in the FOH rack |
| Show file to church server | Weekly | `/AV/Console-Backups/YYYY-MM-DD/` |
| Show file to this repository | On any significant change | Commit the exported file and note what changed |

A console can fail. A show file that only exists inside it is a show file you will
lose. Three copies, one of them off-site.
