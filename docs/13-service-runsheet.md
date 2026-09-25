# 13 — Service Run Sheet

The operating procedure for a Sunday. Printable version:
[`../checklists/pre-service.md`](../checklists/pre-service.md)

## Timeline

### T−90 min — Power up

Power on in this order. **Always this order.**

1. Console
2. Stage boxes
3. Wait for AES50 sync (check the console shows all boxes connected)
4. **Amplifiers and powered speakers LAST**

Power down in the exact reverse: amps first, console last. Powering an amplifier on
before the console has settled sends a loud thump through the PA and, over time,
damages drivers.

Then:
- [ ] Load show file `GHC-MASTER-SHOW`, recall **Scene 1 — DEFAULT / RESET**
- [ ] Confirm all AES50 links green and all 48 channels present
- [ ] Confirm Logic Pro sees the WING; open the session from the template
- [ ] Confirm the WING-LIVE SD card is inserted and formatted
- [ ] Confirm the Osee is on, audio input connected, meters moving

### T−75 min — Line check

- [ ] Every channel, one at a time: tap the mic or play the DI, confirm signal
- [ ] Verify phantom power where required
- [ ] Check every wireless: **fresh batteries in every pack and every handheld**,
      RF signal strong, no dropouts when walking the stage
- [ ] Verify the pastor's lav (ch 34) works, then mute it
- [ ] Confirm IEM packs are on the correct mixes, batteries fresh

### T−60 min — Band soundcheck

1. Start with the drummer alone. Kick, snare, toms, cymbals. Set gains.
2. Add bass. Get kick and bass working together before anything else joins.
3. Add keys, then guitars.
4. Add vocals last.
5. Build each IEM mix while the relevant musician plays — ask them, don't guess.
6. Run one full song at service volume. Check the SPL meter.

### T−30 min — Broadcast check

- [ ] Flip to Main 2, verify the broadcast mix on **headphones**
- [ ] LUFS meter reading near −16 integrated
- [ ] **Listen on a phone speaker**
- [ ] Solo Main 2 and confirm click and cues are absent
- [ ] Verify lip-sync on the live stream preview
- [ ] Confirm the stream is up and the confidence monitor is working

### T−20 min — Speech check

- [ ] Pastor on the headset, at speaking volume, **from the platform**
- [ ] Set gain, confirm no feedback anywhere on the platform — walk it
- [ ] Check the pulpit wedge level
- [ ] Verify automix is engaging correctly with two mics open
- [ ] Test the lav as a backup, then mute it

### T−15 min — Record and go

- [ ] **Start Logic Pro recording**
- [ ] **Start the WING-LIVE SD recording**
- [ ] Recall **Scene 2 — PRE-SERVICE**
- [ ] Walk-in music playing at 72–76 dBA
- [ ] All microphones muted
- [ ] Final walk of the room — listen from the back, the sides, under the balcony

### T−0 — Service

| Moment | Action |
|---|---|
| Welcome | Scene 3. Speech live, band muted. |
| Worship set | Scene 4. Ride DCA 2 (worship leader) above all else. |
| Quiet moment | Scene 5. |
| Prayer / altar | **Scene 6 — ambience muted (MG6).** |
| Sermon | Scene 7. DCA 1 up, DCA 12 down. Watch speech level constantly. |
| Video | Scene 8. Pre-check the audio before it rolls. |
| Offering / response | Scene 9. |
| Closing | Scene 10. |
| Dismissal | Scene 11. |

### Post-service

- [ ] Stop Logic recording, **save**
- [ ] Stop and eject the SD card
- [ ] Back up the recording to the NAS — **before you leave the building**
- [ ] Recall Scene 1
- [ ] Power down: **amps → stage boxes → console**
- [ ] All wireless off, batteries out, on charge
- [ ] Complete the service log below

---

## During-service discipline

**The three things to watch, constantly:**
1. The **speech level** — can everyone hear?
2. The **SPL meter** — are you within target?
3. The **Main 2 meter** — is the stream still alive and at level?

**The three things not to do:**
1. Do not edit scenes live.
2. Do not adjust monitor levels unless a musician asks.
3. Do not chase small mix problems during the sermon. Nobody notices the guitar EQ
   during the message. Everyone notices you missing the pastor's cue.

---

## Service log

Copy this into a new row every week. This log is how the system gets better.

| Date | Operator | Issues | Changes made | Follow-up needed |
|---|---|---|---|---|
| | | | | |

**Log every feedback event, every dropout, every dead battery, every "I couldn't
hear."** Patterns only become visible when they are written down. A microphone that
drops out once is bad luck; one that drops out on three logged occasions is a
microphone to replace.
