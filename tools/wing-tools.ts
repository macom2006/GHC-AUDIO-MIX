import { z } from "zod";
import { ConsoleOSC } from "./osc-client.js";

/**
 * Behringer WING MCP tools — CORRECTED ADDRESS MAP.
 *
 * Replaces the scaffold in feimpraim/x32-wing-mcp, whose WING addresses were
 * X32-shaped guesses (`/ch/01/mix/fader`). These addresses are derived from a
 * real WING's own snapshot export (serial S240100078BV2, firmware 3.1-0), where
 * the .snap JSON is a serialisation of the console's live parameter tree.
 *
 * Two differences from the X32 that break every scaffold address:
 *   1. Indices are NOT zero-padded.  /ch/1/...   not  /ch/01/...
 *   2. Leaf names differ.            fdr, mute, send/<b>/lvl, main/<m>/lvl
 *                                    not  mix/fader, mix/on, mix/<b>/level
 *
 * Values are dB directly (e.g. -14.43), not the X32's 0..1 float taper, so
 * dbToFloat()/floatToDb() must NOT be applied.
 *
 * STATUS: addresses are high-confidence but not yet confirmed against hardware.
 * Run tools/wing_probe.py first — it is read-only and checks every address
 * against your own snapshot's values.
 */

const A = {
  chFader:   (c: number) => `/ch/${c}/fdr`,
  chMute:    (c: number) => `/ch/${c}/mute`,
  chName:    (c: number) => `/ch/${c}/name`,
  chHpfOn:   (c: number) => `/ch/${c}/flt/lc`,
  chHpfFreq: (c: number) => `/ch/${c}/flt/lcf`,
  chBusSend: (c: number, b: number) => `/ch/${c}/send/${b}/lvl`,
  chBusOn:   (c: number, b: number) => `/ch/${c}/send/${b}/on`,
  chMainLvl: (c: number, m: number) => `/ch/${c}/main/${m}/lvl`,
  chMainOn:  (c: number, m: number) => `/ch/${c}/main/${m}/on`,
  chEqGain:  (c: number, b: number) => `/ch/${c}/eq/${b}g`,
  chEqFreq:  (c: number, b: number) => `/ch/${c}/eq/${b}f`,
  chEqQ:     (c: number, b: number) => `/ch/${c}/eq/${b}q`,
  busFader:  (b: number) => `/bus/${b}/fdr`,
  busMute:   (b: number) => `/bus/${b}/mute`,
  busName:   (b: number) => `/bus/${b}/name`,
  mainFader: (m: number) => `/main/${m}/fdr`,
  mtxFader:  (x: number) => `/mtx/${x}/fdr`,
  mtxTrim:   (x: number) => `/mtx/${x}/in/set/trim`,
  dcaFader:  (d: number) => `/dca/${d}/fdr`,
  dcaMute:   (d: number) => `/dca/${d}/mute`,
  mgrpMute:  (g: number) => `/mgrp/${g}/mute`,
  geqBand:   (f: number, band: string) => `/fx/${f}/${band}`,
};

/** Channel/bus/DCA counts on a full-size WING. */
const LIMITS = { ch: 40, aux: 8, bus: 16, main: 4, mtx: 8, dca: 16, mgrp: 8, fx: 16 };

/**
 * Writes are gated behind ALLOW_WRITES=true so the default install can read
 * the console but cannot change it. Recommended for a desk that runs services.
 */
const WRITES_ENABLED = process.env.ALLOW_WRITES === "true";

function guard(what: string) {
  if (!WRITES_ENABLED) {
    throw new Error(
      `Refused: ${what}. Writes are disabled. Set ALLOW_WRITES=true in the MCP ` +
      `server config to enable, and never while a service is running.`
    );
  }
}

const ok = (text: string) => ({ content: [{ type: "text" as const, text }] });

export function registerWingTools(server: any, osc: ConsoleOSC) {

  // ---------------------------------------------------------------- READS
  server.tool(
    "wing_query",
    "Read any WING parameter by its OSC address, e.g. /ch/1/fdr or /mtx/5/in/set/trim. Read-only.",
    { address: z.string().describe("OSC address, e.g. /bus/7/fdr") },
    async ({ address }: { address: string }) => {
      const v = await osc.query(address);
      return ok(`${address} = ${JSON.stringify(v)}`);
    }
  );

  server.tool(
    "wing_read_channel",
    "Read a channel's key settings: name, fader, mute, high-pass, and its sends to every bus and main.",
    { channel: z.number().int().min(1).max(LIMITS.ch) },
    async ({ channel }: { channel: number }) => {
      const out: Record<string, any> = {};
      for (const [k, addr] of [
        ["name", A.chName(channel)], ["faderDb", A.chFader(channel)],
        ["mute", A.chMute(channel)], ["hpfOn", A.chHpfOn(channel)],
        ["hpfHz", A.chHpfFreq(channel)],
      ] as const) {
        out[k] = (await osc.querySafe(addr))?.[0];
      }
      out.busSends = {};
      for (let b = 1; b <= LIMITS.bus; b++) {
        const on = (await osc.querySafe(A.chBusOn(channel, b)))?.[0];
        if (on) out.busSends[b] = (await osc.querySafe(A.chBusSend(channel, b)))?.[0];
      }
      out.mainSends = {};
      for (let m = 1; m <= LIMITS.main; m++) {
        const on = (await osc.querySafe(A.chMainOn(channel, m)))?.[0];
        if (on) out.mainSends[m] = (await osc.querySafe(A.chMainLvl(channel, m)))?.[0];
      }
      return ok(JSON.stringify(out, null, 2));
    }
  );

  server.tool(
    "wing_open_mic_report",
    "Count microphones feeding a monitor bus and report the gain-before-feedback cost. Read-only. " +
    "Purpose-built for diagnosing wedge feedback.",
    { bus: z.number().int().min(1).max(LIMITS.bus).default(1) },
    async ({ bus }: { bus: number }) => {
      const open: Array<{ ch: number; name: string; send: number }> = [];
      for (let c = 1; c <= LIMITS.ch; c++) {
        const on = (await osc.querySafe(A.chBusOn(c, bus)))?.[0];
        if (!on) continue;
        const lvl = (await osc.querySafe(A.chBusSend(c, bus)))?.[0];
        if (typeof lvl === "number" && lvl > -90) {
          open.push({ ch: c, name: String((await osc.querySafe(A.chName(c)))?.[0] ?? ""), send: lvl });
        }
      }
      const loss = open.length > 1 ? 3 * Math.log2(open.length) : 0;
      const lines = open.map(o => `  ch${o.ch} ${o.name} ${o.send.toFixed(1)} dB`).join("\n");
      return ok(
        `Bus ${bus}: ${open.length} sources open\n${lines}\n\n` +
        `Gain before feedback lost vs a single source: ${loss.toFixed(1)} dB\n` +
        `Reducing to 4 sources would recover ${(loss - 6).toFixed(1)} dB.`
      );
    }
  );

  // ---------------------------------------------------------------- WRITES
  server.tool(
    "wing_set_channel_fader",
    "Set a channel fader in dB. Requires ALLOW_WRITES=true.",
    { channel: z.number().int().min(1).max(LIMITS.ch), db: z.number().min(-144).max(10) },
    async ({ channel, db }: { channel: number; db: number }) => {
      guard(`set ch${channel} fader to ${db} dB`);
      osc.send(A.chFader(channel), [{ type: "f", value: db }]);
      return ok(`ch${channel} fader -> ${db.toFixed(1)} dB`);
    }
  );

  server.tool(
    "wing_set_channel_mute",
    "Mute or unmute a channel. Requires ALLOW_WRITES=true.",
    { channel: z.number().int().min(1).max(LIMITS.ch), mute: z.boolean() },
    async ({ channel, mute }: { channel: number; mute: boolean }) => {
      guard(`${mute ? "mute" : "unmute"} ch${channel}`);
      osc.send(A.chMute(channel), [{ type: "i", value: mute ? 1 : 0 }]);
      return ok(`ch${channel} ${mute ? "muted" : "unmuted"}`);
    }
  );

  server.tool(
    "wing_set_bus_send",
    "Set a channel's send level to a bus, in dB. Requires ALLOW_WRITES=true.",
    { channel: z.number().int().min(1).max(LIMITS.ch),
      bus: z.number().int().min(1).max(LIMITS.bus),
      db: z.number().min(-144).max(10) },
    async ({ channel, bus, db }: { channel: number; bus: number; db: number }) => {
      guard(`set ch${channel} -> bus${bus} to ${db} dB`);
      osc.send(A.chBusSend(channel, bus), [{ type: "f", value: db }]);
      return ok(`ch${channel} -> bus${bus} = ${db.toFixed(1)} dB`);
    }
  );

  server.tool(
    "wing_set_geq_band",
    "Set one band of a graphic EQ in an FX slot — the ring-out tool. " +
    "Band names are the GEQ's own labels: 20, 25, 31, 40, 50, 63, 80, 100, 125, 160, 200, 250, " +
    "315, 400, 500, 630, 800, 1k, 1k25, 1k6, 2k, 2k5, 3k15, 4k, 5k, 6k3, 8k, 10k, 12k5, 16k, 20k. " +
    "Requires ALLOW_WRITES=true.",
    { fxSlot: z.number().int().min(1).max(LIMITS.fx),
      band: z.string(), db: z.number().min(-15).max(15) },
    async ({ fxSlot, band, db }: { fxSlot: number; band: string; db: number }) => {
      guard(`set FX${fxSlot} GEQ band ${band} to ${db} dB`);
      osc.send(A.geqBand(fxSlot, band), [{ type: "f", value: db }]);
      return ok(`FX${fxSlot} GEQ ${band} -> ${db.toFixed(1)} dB`);
    }
  );

  // Deliberately NOT implemented: snapshot/scene recall.
  // Recalling a snapshot is the most destructive operation on the console and
  // the scaffold wired it to an unverified address. If it is ever added it must
  // require a separate opt-in beyond ALLOW_WRITES.
}
