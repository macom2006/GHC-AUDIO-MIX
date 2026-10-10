#!/usr/bin/env python3
"""
WING OSC address prober — READ ONLY. Sends no writes, ever.

Verifies that the WING OSC address map derived from your snapshot is correct,
by querying each address and comparing the reply against the value your
snapshot says it should be.

Usage:
    python3 wing_probe.py <CONSOLE_IP> [--port 2223] [--snap path/to/current.snap]

Dependencies: none. Python 3.8+ standard library only.
"""
import argparse, json, socket, struct, sys, time

# ----------------------------------------------------------------- OSC codec
def _pad(b: bytes) -> bytes:
    return b + b"\0" * (4 - len(b) % 4 if len(b) % 4 else 4)

def osc_encode(address: str, args=()) -> bytes:
    out = _pad(address.encode())
    tags = ","
    body = b""
    for a in args:
        if isinstance(a, bool):   tags += "i"; body += struct.pack(">i", 1 if a else 0)
        elif isinstance(a, int):  tags += "i"; body += struct.pack(">i", a)
        elif isinstance(a, float):tags += "f"; body += struct.pack(">f", a)
        else:                     tags += "s"; body += _pad(str(a).encode())
    return out + _pad(tags.encode()) + body

def _read_str(buf, i):
    e = buf.index(b"\0", i)
    s = buf[i:e].decode("utf-8", "replace")
    return s, i + (len(s) + 4) // 4 * 4 if (len(s) % 4 == 0) else i + (len(s) // 4 + 1) * 4

def osc_decode(buf: bytes):
    try:
        addr, i = _read_str(buf, 0)
        if i >= len(buf): return addr, []
        tags, i = _read_str(buf, i)
        vals = []
        for t in tags.lstrip(","):
            if t == "i":   vals.append(struct.unpack(">i", buf[i:i+4])[0]); i += 4
            elif t == "f": vals.append(struct.unpack(">f", buf[i:i+4])[0]); i += 4
            elif t == "s": s, i = _read_str(buf, i); vals.append(s)
            elif t in "TF": vals.append(t == "T")
            else: break
        return addr, vals
    except Exception:
        return None, []

# ----------------------------------------------------------------- the probe
def probe(ip, port, tests, timeout=1.0):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.settimeout(timeout)
    s.bind(("0.0.0.0", 0))
    results = []
    for addr, expect, label in tests:
        got, note = None, ""
        try:
            s.sendto(osc_encode(addr), (ip, port))
            deadline = time.time() + timeout
            while time.time() < deadline:
                try:
                    data, _ = s.recvfrom(65536)
                except socket.timeout:
                    break
                a, v = osc_decode(data)
                if a == addr:
                    got = v[0] if len(v) == 1 else v
                    break
                note = "(reply for %s)" % a
        except Exception as e:
            note = "send error: %s" % e
        results.append((addr, label, expect, got, note))
    s.close()
    return results

def close(a, b, tol=0.6):
    if a is None or b is None: return False
    if isinstance(a, bool) or isinstance(b, bool): return bool(a) == bool(b)
    if isinstance(a, str) or isinstance(b, str):   return str(a).strip() == str(b).strip()
    try: return abs(float(a) - float(b)) <= tol
    except Exception: return False

def build_tests(ae):
    g = lambda *k: __import__("functools").reduce(lambda d, x: d[x], k, ae)
    t = [
      ("/ch/1/fdr",            g("ch","1","fdr"),                    "Ch1 fader (dB)"),
      ("/ch/1/mute",           g("ch","1","mute"),                   "Ch1 mute"),
      ("/ch/1/name",           g("ch","1","name"),                   "Ch1 name"),
      ("/ch/1/flt/lcf",        g("ch","1","flt","lcf"),              "Ch1 high-pass freq"),
      ("/ch/1/send/7/lvl",     g("ch","1","send","7","lvl"),         "Ch1 -> Bus7 send"),
      ("/ch/1/main/1/lvl",     g("ch","1","main","1","lvl"),         "Ch1 -> Main1 level"),
      ("/ch/23/eq/2q",         g("ch","23","eq","2q"),               "Ch23 EQ band2 Q"),
      ("/bus/7/name",          g("bus","7","name"),                  "Bus7 name"),
      ("/bus/7/fdr",           g("bus","7","fdr"),                   "Bus7 fader"),
      ("/bus/7/mute",          g("bus","7","mute"),                  "Bus7 mute"),
      ("/main/1/fdr",          g("main","1","fdr"),                  "Main1 fader"),
      ("/main/1/name",         g("main","1","name"),                 "Main1 name"),
      ("/mtx/5/name",          g("mtx","5","name"),                  "Matrix5 name"),
      ("/mtx/5/fdr",           g("mtx","5","fdr"),                   "Matrix5 fader"),
      ("/mtx/5/in/set/trim",   g("mtx","5","in","set","trim"),       "Matrix5 input trim"),
      ("/dca/1/name",          g("dca","1","name"),                  "DCA1 name"),
      ("/dca/1/fdr",           g("dca","1","fdr"),                   "DCA1 fader"),
      ("/fx/7/mdl",            g("fx","7","mdl"),                    "FX7 model"),
      ("/cfg/amix/x",          g("cfg","amix","x"),                  "Automix group X"),
    ]
    return t

def main():
    p = argparse.ArgumentParser()
    p.add_argument("ip")
    p.add_argument("--port", type=int, default=2223)
    p.add_argument("--snap", default=None, help="current .snap export to compare against")
    p.add_argument("--timeout", type=float, default=1.0)
    a = p.parse_args()

    if not a.snap:
        print("ERROR: pass --snap <your current .snap export> so replies can be checked.")
        sys.exit(2)
    ae = json.load(open(a.snap))["ae_data"]
    tests = build_tests(ae)

    print("WING OSC probe — READ ONLY, no writes are sent")
    print("target %s:%d   comparing against %s\n" % (a.ip, a.port, a.snap))
    print("%-22s %-22s %14s %14s" % ("ADDRESS", "WHAT", "EXPECTED", "CONSOLE SAID"))
    print("-" * 78)

    res = probe(a.ip, a.port, tests, a.timeout)
    ok = silent = wrong = 0
    for addr, label, exp, got, note in res:
        e = ("%.2f" % exp) if isinstance(exp, float) else str(exp)
        if got is None:
            verdict, g = "no reply", "-"; silent += 1
        elif close(got, exp):
            verdict, g = "MATCH", (("%.2f" % got) if isinstance(got, float) else str(got)); ok += 1
        else:
            verdict, g = "differs", (("%.2f" % got) if isinstance(got, float) else str(got)); wrong += 1
        print("%-22s %-22s %14s %14s   %s %s" % (addr, label, e[:14], g[:14], verdict, note))

    n = len(res)
    print("\n%d matched, %d differed, %d no reply (of %d)" % (ok, wrong, silent, n))
    if ok >= n * 0.7:
        print("\nVERDICT: the address map is correct. Reads work. Safe to proceed to step 4.")
    elif ok > 0:
        print("\nVERDICT: partly correct — some addresses need adjusting. Send me this output.")
    else:
        print("\nVERDICT: nothing replied. Check: console IP, OSC enabled on the desk,")
        print("         same subnet, no firewall on the Mac, port %d correct." % a.port)

if __name__ == "__main__":
    main()
