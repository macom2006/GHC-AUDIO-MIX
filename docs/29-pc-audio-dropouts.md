# 29 — Computer Audio Dropping Out Intermittently

## The console is not doing it

I checked every processor that could gate, duck or mute AUX 8. All clean:

| Setting | State |
|---|---|
| AUX 8 dynamics (CMB combinator) | **OFF** |
| AUX 8 EQ | OFF |
| Side-chain | OFF |
| Inserts | none |
| Source auto-switch (`srcauto`) | **false** |
| Alt source (`altsrc`, `altsw`, `autoaltovr`) | **all false** |
| Clock | 48 kHz, internal |
| USB config | 48/48 |

The WING is passing through whatever arrives. **The gaps are happening before the
console** — on the Mac, or on the USB link.

There is exactly **one** console-side possibility I cannot rule out from the file,
and it is the first thing to check.

---

## Check this first — automix

**Automix group X is now switched on.** Membership is stored on the console and does
not travel in a snapshot, so I cannot see who is in it.

If **AUX 8 got added to group X**, the computer will be attenuated every single time
a speech microphone is louder than it — which presents exactly as intermittent
cutting, and would have started the moment automix was enabled.

**Go to the automix page. Group X should contain ch 21, ch 23 and ch 33 and nothing
else.** Remove anything else, especially AUX 8, the singers and any playback channel.

Automix belongs on speech microphones only. Never on music, never on playback.

---

## Identify the cause by when it cuts

This is the fastest route. Watch for the correlation:

| When it cuts | Cause | Go to |
|---|---|---|
| **When someone speaks** | Automix | above |
| **Randomly, a fraction of a second, any material** | Sample rate or clock | Fix 1, 2 |
| **When you start or stop a video, or switch apps** | Sample rate switching | Fix 1 |
| **When Logic is recording, especially later in the service** | CPU or disk contention | Fix 4 |
| **When someone touches the desk or the cable** | Physical | Fix 5 |
| **After the Mac has been idle** | Power management | Fix 3 |

---

## Fix 1 — lock the Mac to 48 kHz

The single most common cause.

Your WING is locked at **48 kHz**. Most computer material is not: YouTube and Spotify
are 44.1 kHz, video files are usually 48, system sounds vary. Every time an app asks
for a different rate, macOS renegotiates the interface — and you get a gap.

1. Open **Audio MIDI Setup** (Applications → Utilities)
2. Select the **WING**
3. Set **Format** to **48000 Hz**, 24-bit, for both input and output
4. Do the same in any playback application that offers a rate setting

Once everything is at 48 kHz, macOS resamples in software instead of
re-clocking the hardware, and the gaps stop.

## Fix 2 — get rid of the aggregate device

Earlier in this project, Logic was configured with the **WING as input device and a
Volt 276 as output device**. macOS bridges that with an implicit aggregate, and an
aggregate spanning two interfaces with independent clocks **will** drop out
intermittently as they drift.

1. Open **Audio MIDI Setup** and look for any **Aggregate Device** or **Multi-Output
   Device** in the left-hand list
2. If one exists and anything is pointed at it, stop using it
3. In Logic: `Settings → Audio → Devices`, set **both Input and Output to the WING**
4. Set the Mac's **system output** (menu bar, or System Settings → Sound) to the
   **WING** as well

One device, one clock, everywhere. See `docs/17-logic-broadcast-rig.md`.

## Fix 3 — stop the Mac managing power

- **System Settings → Displays → Advanced** — turn off "Put hard disks to sleep"
  behaviour and prevent sleep when the display is off
- **Energy Saver** — prevent automatic sleeping when plugged in
- Disable **App Nap** for your playback app: right-click it in Applications →
  Get Info → tick **Prevent App Nap**
- Keep the Mac plugged in. On battery, macOS throttles aggressively.

## Fix 4 — reduce the load on the Mac

If Logic is recording 40 tracks to disk while the same machine plays back video, you
can hit disk or CPU limits — and that produces exactly this, usually worsening as the
service goes on and the recording file grows.

- Record Logic to a **different physical drive** from the one serving playback
- **I/O Buffer to 512** while recording (you are not monitoring through Logic, so
  the extra latency costs nothing)
- **Process Buffer Range: Large**
- Close everything else. No browser, no email, no updates.
- Check free disk space. **Below about 10% free, macOS gets unreliable.**
- Consider a **separate machine for playback** — this is the proper answer if the
  same Mac is recording 40 channels and running media.

## Fix 5 — the physical link

- **Plug the WING directly into the Mac.** No hub, no dock, no extension.
- Use a **data-rated USB cable**, under 3 m. Charging cables and long passive runs
  cause exactly this.
- Try a **different port** — on Apple silicon Macs, ports are not always on the same
  internal controller
- Re-seat the connector at both ends

---

## When it is fixed

- [ ] Automix group X contains only ch 21, 23, 33
- [ ] Mac locked to 48 kHz in Audio MIDI Setup
- [ ] No aggregate or multi-output device in use
- [ ] Logic's input **and** output both set to the WING
- [ ] Mac's system output set to the WING
- [ ] Sleep and App Nap disabled
- [ ] WING connected directly to the Mac with a data cable
- [ ] Play forty minutes of continuous material with Logic recording. **No gaps.**

Test it for the length of a service, not for two minutes. Intermittent faults hide
from short tests — that is what makes them intermittent.

---

## A note on where this belongs

The WING is a rock-solid 48-channel interface and it is behaving correctly. Nearly
every "audio drops out over USB" fault in a church rig comes down to sample rate,
an aggregate device, power management, or a hub — in roughly that order.

If you work through the list above and it still cuts, the next step is to **take the
Mac out of the live path entirely** for playback: a cheap dedicated playback device
into a spare console input has no drivers, no operating system and nothing to
renegotiate. For walk-in music and video audio, that reliability is usually worth
more than the convenience.
