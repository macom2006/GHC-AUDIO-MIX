# GHC BROADCAST V1 — Implementation Sheet

**Print this. Take it to the console. Work top to bottom.**

File: `GHC BROADCAST V1.snap` · Full change list: `../docs/20-what-changed.md`

Allow **90 minutes**, mid-week, with nobody waiting on you.

---

## BEFORE YOU TOUCH ANYTHING

- [ ] `Setup → Show → Save As` → **`GHC-PRE-BROADCAST-V1`**
- [ ] Copy that saved show to **USB** and to the **church server**
- [ ] Copy `GHC BROADCAST V1.snap` onto a USB stick

> This file was built from your **18 March 2026** snapshot. If the console has been
> changed since then, loading it reverts those changes. The backup above is your
> way back. If you would rather not risk it, use the change list in
> `docs/20-what-changed.md` and make the edits by hand on your current state.

---

## STEP 1 — Load and check the house  (15 min)

- [ ] Insert USB, load `GHC BROADCAST V1.snap`
- [ ] Play familiar music through the PA
- [ ] **Listen to the room.** It should sound the way it did before, with one
      exception below
- [ ] **Re-set the subwoofer level.** Matrix 4 is now aux-fed — it gets only kick,
      floor tom, bass, keys and tracks instead of the whole mix, so it will be
      quieter and much tighter. Bring Matrix 4 up until the low end feels right.
- [ ] Walk the room. Front, back, sides.

**Do not continue until the house sounds right.** The house is the primary product.

> Want the old subs back? Turn `Main 1 → MTX4` **on** and `Bus 11 → MTX4` **off**.
> Two switches. Everything else in this file stays.

---

## STEP 2 — Check the broadcast mix on the console  (10 min)

- [ ] **Solo Bus 7 "BROADCAST"** in headphones. You should hear a complete mix:
      drums, band, singers, speech, crowd.
- [ ] Anything missing? Check that channel's send to Bus 7.
- [ ] **Solo Matrix 5 "STREAM".** Same mix, now mastered — tape, EQ, compression,
      limiter.
- [ ] **Listen specifically for click, cue or talkback.** There should be none.
      If you hear any, find it and unassign it before going further.

---

## STEP 3 — Wire it to the Osee  (20 min)

- [ ] **LCL out 4** → Osee audio input **Left**
- [ ] **LCL out 5** → Osee audio input **Right**
- [ ] Set the Osee input to **LINE** (not Mic)
- [ ] Turn **OFF** the Osee's own EQ, compressor and AGC
- [ ] Turn **OFF** "audio follow video"
- [ ] Mute or unassign every camera's embedded audio

### Set the level
- [ ] Play loud worship material
- [ ] Lower **Matrix 5's output trim** until the Osee meters read
      **−12 dB average, −6 dB peak**
- [ ] Start around **−12 dB** of trim. The WING is +4 dBu; most switchers expect
      −10 dBV. If it still distorts, fit a −20 dB inline pad.
- [ ] Write the final value here: **________ dB**
- [ ] Once set, never touch it again. Mix level lives on the faders.

---

## STEP 4 — Wire the emergency feed  (10 min)

- [ ] **LCL out 2** → second Osee input, **Left**
- [ ] **LCL out 3** → second Osee input, **Right**
- [ ] Label that input **EMERGENCY AUDIO** on the switcher and on the wall plate
- [ ] **Test it:** switch the Osee to it, confirm audio, switch back
- [ ] Teach every operator where that button is

This is the house mix. It is not as good as the broadcast mix. It keeps the service
on air when something breaks.

---

## STEP 5 — Lip-sync  (20 min)

- [ ] Stand in shot with a mic open. **Clap sharply**, 5–10 times, with gaps.
- [ ] Record the program output
- [ ] Open it in Logic. Measure the gap between the frame where your hands meet and
      the audio transient
- [ ] **Enable the delay on Matrix 5** and enter that value
- [ ] Measured: **________ ms**   Date: __________   By: __________

1 frame @ 30 fps = 33 ms · @ 25 fps = 40 ms · @ 60 fps = 17 ms

**Audio slightly late is fine. Audio early is never fine.**

---

## STEP 6 — Scene safes  ★ DO NOT SKIP  (20 min)

This could not be written into the file — the encoding is not safe to guess at. It
is the single most important thing on the desk.

`Setup → Global → Safes`. Set these **ON**:

- [ ] **Source / preamp — every group** (LCL, AUX, A, B, C, SC, USB, CRD, MOD, PLAY, AES, USR, OSC)
- [ ] **Output patch — every group**
- [ ] **Bus 1, Bus 8, Bus 9** (the monitor mixes)
- [ ] **Matrix 1, 2, 3, 4, 5**
- [ ] **Main 1 master fader**
- [ ] **Ch 21 Pastor Lapel — mute safe**

### Test it
- [ ] Change a preamp gain by 10 dB. Pull a monitor bus down. Move the house master.
- [ ] Recall a scene.
- [ ] **Those three must not move.** Everything else should.
- [ ] Undo your test changes.

An untested safe is not a safe.

---

## STEP 7 — Finish the operating layer  (20 min)

Also not writable into a snapshot.

- [ ] **Automix**: enable group **X**. Add **ch 21, 23, 33** only (speech). Pastor at
      weight 0. **Do not add singers.**
- [ ] Test: two mics open, two people talking — the quieter mic should duck audibly
- [ ] **Talkback**: it is assigned to a channel but routed nowhere. Enable
      destinations **Bus 1, Bus 8, Bus 9**. Confirm it does **not** reach Main 1 or
      Matrix 5.
- [ ] **Verify the DCAs** loaded correctly: DCA 10 should be **SPEECH** (ch 21, 23,
      33), DCA 11 should be **CROWD** (ch 29, 30). I wrote these using the tag
      format your console already uses, but that encoding is inferred — check it.
- [ ] **Verify Mute Group 6 = CROWD.** Press it. Channels 29 and 30 must mute.
      This is your altar-call button.

---

## STEP 8 — Listen properly  (15 min)

- [ ] Stream to a private/unlisted test broadcast
- [ ] Listen on **earbuds**
- [ ] Listen on a **phone speaker** — this is what most of your viewers use
- [ ] Check speech against worship. They should feel **equally loud**. If the sermon
      is quieter, raise ch 21's send to Bus 7.
- [ ] Watch for lip-sync
- [ ] Check the crowd mics are present during singing but not distracting

---

## STEP 9 — Save and record

- [ ] `Setup → Show → Save As` → **`GHC-BROADCAST-V1-COMMISSIONED`**
- [ ] Export to **USB** and the **server**
- [ ] Write the Osee trim and lip-sync values into `docs/20-what-changed.md`
- [ ] Note anything you changed from the file, so the next person knows

---

## Sunday operating summary

| | |
|---|---|
| **Broadcast master** | Bus 7 — one fader controls the whole online mix |
| **Speech** | DCA 10 |
| **Crowd mics** | DCA 11 · **Mute Group 6 for every altar call and private prayer** |
| **Crowd level** | −18 dB normally, **−10 to −12 during congregational singing**, muted for prayer |
| **Emergency** | Second Osee input. House mix. One button. |
| **House targets** | Worship 88–92 dBA · Speech 72–78 dBA |
| **Stream target** | −16 LUFS · −1.5 dBTP · **speech as loud as music** |

---

## If something is wrong

| Symptom | First move |
|---|---|
| Room sounds thin / no low end | Matrix 4 level — the subs are aux-fed now and need re-setting |
| Stream silent | Solo Bus 7, then Matrix 5. Check LCL 4/5 cabling. Then switch the Osee to EMERGENCY. |
| Stream distorted | Matrix 5 output trim too high, or Osee input set to Mic instead of Line |
| Sermon quiet online | Raise ch 21 send to Bus 7 |
| Anything worse than before | Load `GHC-PRE-BROADCAST-V1`. Nothing here is one-way. |
