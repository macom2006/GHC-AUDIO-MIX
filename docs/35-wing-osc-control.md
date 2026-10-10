# 35 — Live Console Control over OSC

Everything needed to make `feimpraim/x32-wing-mcp` actually work on your WING,
plus the order to do it in. **Nothing here touches the console until step 4, and
nothing writes to it until step 6.**

## Why the original needs correcting

The repo's WING support is, in its author's own words, *"a scaffold to build
against, not a finished implementation."* Its addresses are X32-shaped:

| | Scaffold sends | Your WING actually uses |
|---|---|---|
| Channel fader | `/ch/01/mix/fader` | **`/ch/1/fdr`** |
| Channel mute | `/ch/01/mix/on` | **`/ch/1/mute`** |
| Bus send | `/ch/01/mix/07/level` | **`/ch/1/send/7/lvl`** |
| Main send | `/ch/01/mix/main/1/level` | **`/ch/1/main/1/lvl`** |

Two differences break every one of them: **indices are not zero-padded**, and
**the leaf names are different**. Values are also plain dB (`-14.43`), not the
X32's 0–1 taper, so the scaffold's `dbToFloat()` conversion must not be applied.

## Where the corrected map came from

Your `.snap` file is a serialisation of the console's live parameter tree. Every
address below was read out of your own console's export, with a known value
attached to check against — **860 parameters across 8 sections**.

- [`../tools/WING-OSC-REFERENCE.md`](../tools/WING-OSC-REFERENCE.md) — the readable reference
- [`../tools/wing-osc-map.json`](../tools/wing-osc-map.json) — all 860, machine-readable
- [`../tools/wing-tools.ts`](../tools/wing-tools.ts) — drop-in replacement for the scaffold
- [`../tools/wing_probe.py`](../tools/wing_probe.py) — read-only verifier, no dependencies

**These are high-confidence, not confirmed.** Step 4 confirms them.

---

## Step 1 — Find the console on the network

On the WING: `Setup → Network`. Note the IP address. If it is not on your LAN,
set it to a **static** address on the same subnet as the Mac, outside the DHCP pool.

On the WING: `Setup → Remote` (or Global). Confirm **OSC is enabled**. Your show
file already shows `osc: {"ronly": false}`, so it is on and not read-only.

Record it here: **console IP `________________`**

## Step 2 — Prove the network path

From the Mac:

```bash
ping -c 3 <CONSOLE_IP>
```

No reply means a VLAN, subnet or firewall issue. Fix that before anything else.

## Step 3 — Export a fresh snapshot

On the desk, save the current state to USB. You need it for step 4, and it is
your rollback. Copy it to the Mac.

## Step 4 — Verify the addresses. **Read-only. This is the decisive test.**

```bash
python3 tools/wing_probe.py <CONSOLE_IP> --snap "GHC BROADCAST V9.snap"
```

It queries 19 addresses and compares each reply against what your snapshot says
the value should be. It **sends no writes** — there is no write code in it at all.

| Result | Meaning |
|---|---|
| **Most match** | The map is correct. Go to step 5. |
| **Some match, some differ** | Partly right. **Send me the output** and I will correct the map. |
| **Nothing replies** | Wrong IP, OSC off, wrong subnet, Mac firewall, or wrong port. |

A clean run looks like:

```
/ch/1/fdr      Ch1 fader (dB)   -14.43   -14.43   MATCH
/bus/7/name    Bus7 name     BROADCAST BROADCAST MATCH
/mtx/5/fdr     Matrix5 fader   -32.10   -32.10   MATCH
```

Do this with the console **out of service**. It is harmless, but verify that for
yourself rather than taking my word for it.

## Step 5 — Install the server, reads only

```bash
git clone https://github.com/feimpraim/x32-wing-mcp.git
cd x32-wing-mcp
cp /path/to/GHC-AUDIO-MIX/tools/wing-tools.ts src/wing-tools.ts   # the corrected map
npm install
npm run build
```

Then in Claude Desktop's config on the Mac
(`~/Library/Application Support/Claude/claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "wing": {
      "command": "node",
      "args": ["/full/path/to/x32-wing-mcp/dist/index.js"],
      "env": {
        "CONSOLE_TYPE": "wing",
        "CONSOLE_IP": "YOUR.CONSOLE.IP.HERE",
        "CONSOLE_PORT": "2223"
      }
    }
  }
}
```

**Note what is absent: `ALLOW_WRITES`.** Without it the corrected tools refuse
every write and the server can only read. Run it this way for at least a week.

What you get read-only:

| Tool | Does |
|---|---|
| `wing_query` | Read any parameter by address |
| `wing_read_channel` | A channel's full state including every send |
| `wing_open_mic_report` | **Counts open mics on a monitor bus and calculates the gain-before-feedback cost** |

That third one is built for your actual problem. Point it at Bus 1 during a
rehearsal and it tells you live how many mics are open and what they are costing.

## Step 6 — Enable writes, when you are ready

Add `"ALLOW_WRITES": "true"` to the `env` block.

Available writes: channel fader, channel mute, bus send level, and **GEQ band** —
that last one makes a conversational ring-out possible: *"pull FX7's 2k5 band down
3 dB"*, done, listen, repeat.

**Snapshot recall is deliberately not implemented.** The scaffold wired it to an
unverified `/-action/gosnap`, and recalling a snapshot is the most destructive
thing you can do to that console. If it is ever added it needs its own opt-in
beyond `ALLOW_WRITES`.

### Rules for writes

- Never with `ALLOW_WRITES` set during a service. Take it out of the config.
- **Export a snapshot before any session** that has writes enabled.
- Writes bypass this repository's change log. Anything you keep, export and
  commit afterwards.
- Changing a monitor send changes what a musician hears, live, with no warning.

---

## Honest assessment

**Worth doing for reads.** It removes the export-upload-download cycle, means every
analysis is of the live desk, and kills the stale-baseline failure that produced
the Copilot file. `wing_open_mic_report` alone justifies it.

**Be slower about writes.** The snapshot workflow is clumsy but every change gets
reviewed before it reaches the desk, and there are now nine versions with a written
record of what changed and why. Live writes remove both safeguards from a console
that runs your Sunday services.

My recommendation: **read-only indefinitely, writes only in a mid-week session with
a fresh snapshot saved first.**

## Worth contributing back

The corrected address map is the missing piece in that project — its README
explicitly asks for *"anyone who can verify the WING OSC namespace against real
hardware."* Once step 4 confirms it, `tools/wing-tools.ts` and
`tools/wing-osc-map.json` are a genuine contribution, and Graceland Harvest would
be credited as the church that verified it.
