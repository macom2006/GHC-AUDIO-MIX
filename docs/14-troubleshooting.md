# 14 — Troubleshooting

Written for someone diagnosing a problem with a congregation watching. Work top to
bottom. Do not skip steps because one "couldn't be it."

## No sound at all, anywhere

1. **Is the console on Alt Source?** (Virtual soundcheck left engaged from mid-week.)
   This is the number one cause of total silence. Flip it back to Main Source.
2. Are the amplifiers powered on?
3. Is Main 1 / Matrix 1 muted or at −∞?
4. Is a mute group engaged?
5. Is the AES50 link to the stage box up? Check for green.
6. Check the physical output cables at the console.

## No sound from one channel

1. Is the channel muted? Is its DCA muted? Is it in an engaged mute group?
2. Is the fader up? Is the DCA fader up?
3. Is it assigned to Main 1?
4. Is the gate closed? (Watch the gate meter — bypass it as a test.)
5. Is the preamp gain up?
6. Is phantom power on, if the mic needs it?
7. Swap the cable. Then swap the mic. Then swap the stage box input.

## Feedback

**First: pull the master down 10 dB.** Stop the noise, then diagnose.

1. Which mic was just unmuted or just moved? Start there.
2. Is a mic in front of a speaker? Move the mic or the person.
3. Is a wedge too loud? Pull it.
4. Identify the frequency on the RTA, apply a narrow notch (doc 08).
5. Log it. Fix the root cause mid-week.

## Stream has no audio

**At GHC the broadcast mix comes out of Logic Pro, not the console** — see
`17-logic-broadcast-rig.md`. Work down this list:

1. **Is Logic still running?** Check the transport and the Stream output meter.
2. Is the Stream output object muted or at −∞?
3. Is the audio interface still connected? Logic drops a device silently when USB
   is disturbed — `Settings → Audio → Devices` will show it.
4. Are the cables from the interface to the Osee connected at both ends?
5. Is the Osee input set to **line** and unmuted?
6. Is "audio follow video" on, and did someone cut to a camera with no audio?
7. Is the encoder running? Is the stream actually live?

**If it cannot be recovered in under a minute: switch the Osee to the EMERGENCY
AUDIO input.** That is the WING's Matrix 5 feed, independent of the Mac. Get the
service back on air first, diagnose afterwards.

## Clicks, pops or gradual lip-sync drift on the stream only

This is almost always the **two-clock problem** — Logic running the WING as input
device and a second interface as output device. The house is unaffected because it
never touches the Mac.

1. `Settings → Audio → Devices` — confirm **Input Device and Output Device are both
   the WING**.
2. If a second interface must be used, it belongs in an Aggregate Device with the
   WING as clock master and **drift correction enabled** on the other device.
3. See `17-logic-broadcast-rig.md`.

## Stream audio is distorted

1. Is the Main 2 limiter pinned? Pull the Main 2 master down.
2. Is the level into the Osee too hot? (Doc 11 — this is the most likely cause.)
   Reduce the Matrix 6 output trim.
3. Is the Osee input set to **mic** instead of **line**? Fix it.
4. Is the switcher's own AGC or compressor on? Turn it off.
5. Is a single channel clipping at the preamp? Check the input meters.

## Stream audio is quiet or thin

1. Check the LUFS meter — is it near −16?
2. Is the broadcast mix actually built, or is it a copy of the house mix? (Doc 07.)
3. Are the ambience mics up?
4. Is the 300 Hz cut on Main 2 too aggressive?
5. Are the drums and bass at their broadcast offsets?

## Audio and video out of sync

1. Re-run the clap test (doc 11).
2. Was anything changed in the video chain this week — firmware, resolution, a new
   camera?
3. Adjust the Matrix 6 delay (Option A) or the OBS offset (Option B).
4. Remember: **audio slightly late is fine; audio early is never fine.**

## Clicking, popping or ticking on all channels

Sample-rate or clock mismatch.

1. Confirm the console is at 48 kHz.
2. Confirm Logic Pro is at 48 kHz.
3. Confirm the WING is the clock master and nothing else is trying to be.
4. Check the AES50 cables — a marginal Cat5e run causes intermittent ticks.
5. Replace the AES50 cable. Use shielded Cat5e or better, and keep runs under 100 m.

## Hum or buzz

| Sound | Likely cause | Fix |
|---|---|---|
| Low hum (50/60 Hz) | Ground loop | Lift the ground on one end of the offending connection with a ground-lift DI; never lift a mains earth |
| Buzz (harmonic, harsh) | Lighting dimmers, LED drivers | Reroute cables away from lighting; use balanced connections throughout |
| Buzz on one channel only | Unbalanced cable or a failing DI | Swap the cable, then the DI |
| Hum that changes when someone touches a guitar | Guitar grounding | Check the amp and the player's pedalboard power |
| Hiss | Too many open mics, or a preamp gain too high | Automix (doc 04), and re-check the gain structure |

## Wireless dropouts

1. Fresh batteries. Always the first check, always.
2. Check RF level on the receiver.
3. Is another device on the same frequency? Re-scan and re-sync.
4. Are the antennas positioned with a clear line of sight to the platform?
5. Is a phone, LED wall or Wi-Fi access point near the receiver?
6. Log the pattern. A pack that drops out repeatedly needs replacing, not retuning.

## Logic Pro stopped recording

1. Don't panic — the SD card recording is independent and still running.
2. Check disk space. This is almost always the cause.
3. Check the USB connection.
4. Restart Logic **after** the service, not during.

## "I couldn't hear the pastor"

1. Check the SPL — was speech below 72 dBA?
2. Was DCA 1 down from the worship set and never brought back up?
3. Is the 2.5 kHz intelligibility boost in place on the speech channel (doc 04)?
4. Is the room too reverberant? (Acoustic problem, not a console problem.)
5. Is the complaint from a specific seat? Check the fills and delays for that zone.
6. Consider the hearing assist system — is it working, and does the congregation
   know it exists?

---

## Emergency procedures

### Total console failure
1. If there is a backup mixer or a powered speaker with a mic input, get the pastor's
   voice into the room by any means available.
2. The message matters more than the production. A handheld mic into a single
   powered speaker keeps the service going.
3. Keep a wired dynamic mic and a spare XLR permanently in the FOH rack for exactly
   this.

### Feedback that will not stop
Pull the master to −∞. Take the time you need. Silence for ten seconds is better
than a ringing PA for one.

### Something is being broadcast that should not be
**Mute Main 2 immediately**, then fix the cause. Contact the media team to trim the
recording before it is published. This applies to private prayer, pastoral
conversation, off-mic comments, and anything said at the altar.

**When in doubt, mute first and ask afterwards.** Nobody has ever been disciplined
for protecting someone's privacy.
