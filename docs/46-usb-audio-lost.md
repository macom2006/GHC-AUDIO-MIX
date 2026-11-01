# 46 — USB audio from the computer stopped

Third occurrence of PC-audio trouble (see doc 28, doc 29). Diagnosed against V18.

## Ruled out: the console

Every part of the console path is verified correct **and unchanged across all
eighteen snapshots I have shipped**:

| | State | Changed since V1? |
|---|---|---|
| `io.in.USB` (computer input bank) | USB-7 = "PC", stereo | **No — byte-identical in all 18** |
| `ae_globals` clock | 48 000 Hz, internal | **No — byte-identical in all 18** |
| `ae_globals.usbacfg` | 48/48 channels | **No — byte-identical in all 18** |
| AUX 8 source | USB-7 | No — unchanged since V9 |
| AUX 8 fader / mute | −8.8 dB, unmuted | No |
| AUX 8 → Main 1 | on, 0.0 dB | No |
| AUX 8 → Bus 7 (stream) | −6.0 dB | No |
| AUX 8 → Bus 11 SUB FEED | −6.0 dB | No |
| ch34, the old duplicate PC path | source OFF, muted, −144 | No — correctly parked |

Nothing else claims USB-7 or USB-8.

**Do not reload a snapshot to fix this.** No snapshot can have caused it, none
can repair it, and recalling one mid-service risks disturbing a working state
for nothing.

## The one pre-existing oddity, which is NOT the cause

`USB-7` and `USB-8` are both flagged stereo, so they nominally overlap on
USB-8. The same is true of USB-39/40 and USB-43/44.

**This has been the case since V1 and the PC has worked throughout.** It is a
tidy-up, not the fault. It did not change on the day the audio stopped, so it
cannot be why.

## Therefore: it is the computer or the USB link

Same conclusion doc 29 reached about the intermittent version of this fault.

### Isolate it in ten seconds

**Solo (PFL) AUX 8 and watch its input meter while the computer plays.**

- **Meter moving** → the link is fine and the problem is downstream — but the
  routing above is verified, so check AUX 8 isn't soloed-out or the DCA holding
  it isn't pulled.
- **Meter dead** → the computer is not delivering. Work the list below.

### In order of likelihood

1. **The computer's output device reverted.**
   macOS: System Settings → Sound → Output must be **WING**. It falls back to
   internal speakers after sleep, a reboot or an OS update.
   **Then check the app separately** — browsers, media players and
   ProPresenter each hold their own output device and do not follow the system
   setting.

2. **Sample-rate mismatch.** The console is **48 kHz internal**. On macOS open
   Audio MIDI Setup → WING → Format and confirm **48 000 Hz**. If the Mac or the
   app is at 44.1, audio may not pass at all. This is the most common cause
   after device selection.

3. **The cable or the port.** Re-seat the USB cable at the console end. Use a
   **direct port on the computer, not a hub** — the WING carries 48 channels
   each way and a cable that passes data fine can still fail to sustain that
   stream.

4. **On Windows only:** the WING needs its USB driver. A Windows update can
   replace or break it. Reinstall from Behringer's WING downloads.

### Recovery order that does not cost you a service

```
quit the playback app
unplug the USB cable
plug it back in
relaunch the app
re-select WING as its output device
```

Rebooting the console is almost never necessary and takes it out of service for
minutes. Try everything above first.

## Worth fixing permanently

This is the third time. Two things reduce the recurrence:

1. **Stop the computer being a single point of failure for playback.** AUX 7
   "2TR" exists and is unused (muted, −144) — a second playback path from a
   phone or a media player on a jack would cover a USB failure mid-service.
2. **Put the PC check in the pre-service checklist** —
   `checklists/pre-service.md` — as an explicit "play a track, confirm AUX 8
   meters" step, so it is caught at 9 a.m. rather than mid-service.
