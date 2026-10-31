#!/usr/bin/env python3
"""Standing coupling audit for a Behringer WING snapshot.

Written after four self-inflicted defects in this repo, all the same shape:
something else referenced the thing that was changed.

  V1   deleted FX11 without checking what used it
  V10  reused an EQ technique without checking what the cuts were doing
  V14  moved BC VOX and left Vox Verb behind
  V15  pulled a channel from a bus on the strength of its name

Run it before shipping any snapshot. It answers, mechanically:
  - what feeds each bus, and where each bus goes (ALL 24 send keys, not just 1-16)
  - which buses output to nothing, and which reach more than one place
  - wet/dry pairs whose levels have drifted apart
  - channels sharing one physical input
  - channel names that contradict the stage-box name
  - which buses can reach a loudspeaker in the room, and which cannot

Usage:
    python3 tools/coupling_check.py "console/GHC BROADCAST V16.snap"
    python3 tools/coupling_check.py OLD.snap NEW.snap     # also: impact of the diff
"""
import json, sys, itertools

def load(p):
    return json.load(open(p))['ae_data']

def bus_name(d, b):
    return d['bus'][str(b)].get('name') or '(unnamed)'

def send_dests(o):
    """Every destination a bus/main actually feeds. Covers 1-16 AND MX1-MX8 --
    the key range that V13's first assertion missed."""
    return [(k, o['send'][k]['lvl']) for k in o['send'] if o['send'][k]['on']]

def leg_to_bus(leg):
    return (leg + 1) // 2

def report(d):
    out, inp = d['io']['out'], d['io']['in']
    issues = []

    # ---- where every bus goes, and what can reach the room -----------------
    patched = {}
    for grp in out:
        for i, e in out[grp].items():
            if not isinstance(e, dict) or e.get('grp') != 'BUS':
                continue
            patched.setdefault(leg_to_bus(e['in']), []).append('%s-%s' % (grp, i))

    print('=== BUS DESTINATIONS (all 24 send keys + output patch + mains) ===')
    for b in range(1, 17):
        bs = d['bus'][str(b)]
        sends = send_dests(bs)
        mains = [m for m in '1234' if bs['main'][m]['on']]
        phys = patched.get(b, [])
        print('  Bus %-2d %-12s fdr %+7.1f mute %-5s sends %-26s mains %-6s out %s'
              % (b, bus_name(d, b)[:12], bs['fdr'], bs['mute'],
                 sends or '-', mains or '-', phys or '-'))
        if not sends and not mains and not phys:
            issues.append('Bus %d (%s) reaches NOTHING - %d sources feed a dead end'
                          % (b, bus_name(d, b),
                             sum(1 for c in range(1, 41)
                                 if d['ch'][str(c)]['send'][str(b)]['on']
                                 and d['ch'][str(c)]['send'][str(b)]['lvl'] > -100)))
        # A stereo bus occupies two consecutive legs in one output group. That is
        # ONE destination, not two -- count distinct groups, not sockets, or every
        # stereo bus looks like a coupling problem and the report becomes noise.
        groups = {p.split('-')[0] for p in phys}
        places = len(sends) + len(mains) + len(groups)
        if places > 1 and not bs['mute']:
            issues.append('Bus %d (%s) reaches %d SEPARATE destinations: sends %s, mains %s, output groups %s'
                          ' - changing its fader moves all of them'
                          % (b, bus_name(d, b), places, [k for k, _ in sends] or '-',
                             mains or '-', sorted(groups) or '-'))

    # ---- wet/dry coupling --------------------------------------------------
    print('\n=== WET / DRY COUPLING (levels that should move together) ===')
    PAIRS = [(13, 15, 'vocals', 'Vox Verb'), (16, 14, 'band', 'Inst Verb')]
    for dry, wet, dname, wname in PAIRS:
        for dest in ('7',):
            ds, ws = d['bus'][str(dry)]['send'][dest], d['bus'][str(wet)]['send'][dest]
            if not (ds['on'] and ws['on']):
                continue
            gap = ds['lvl'] - ws['lvl']
            print('  %-10s %+6.1f dB   %-10s %+6.1f dB   dry-minus-wet %+6.1f dB'
                  % (dname, ds['lvl'], wname, ws['lvl'], gap))
            if abs(gap) > 2.0:
                issues.append('%s is %+.1f dB against %s into Bus %s - if the dry level was '
                              'moved, the reverb did not follow'
                              % (dname, gap, wname, dest))

    # ---- one physical input, two channels ----------------------------------
    print('\n=== PHYSICAL INPUTS CLAIMED BY MORE THAN ONE CHANNEL ===')
    claims = {}
    for c in range(1, 41):
        cn = d['ch'][str(c)]['in']['conn']
        if cn['grp'] == 'OFF':
            continue
        claims.setdefault((cn['grp'], cn['in']), []).append(c)
    clash = False
    for (grp, i), cs in sorted(claims.items()):
        if len(cs) > 1:
            clash = True
            names = ', '.join('ch%d %s' % (c, d['ch'][str(c)]['name'] or '(unnamed)') for c in cs)
            print('  %s-%-3s <- %s' % (grp, i, names))
            live = [c for c in cs if not d['ch'][str(c)]['mute'] and d['ch'][str(c)]['fdr'] > -100]
            if len(live) > 1:
                issues.append('%s-%s is shared by live channels %s - one of them is mis-patched'
                              % (grp, i, live))
    if not clash:
        print('  none')

    # ---- labels that contradict the stage box ------------------------------
    print('\n=== CHANNEL NAME vs STAGE-BOX NAME ===')
    odd = False
    for c in range(1, 41):
        ch = d['ch'][str(c)]
        cn = ch['in']['conn']
        src = inp.get(cn['grp'], {}).get(str(cn['in']), {})
        a, b = (ch['name'] or '').strip(), (src.get('name') or '').strip()
        if not a or not b:
            continue
        if a.lower().split()[0] != b.lower().split()[0]:
            odd = True
            print('  ch%-3s channel says %-18r   input says %r' % (c, a, b))
    if not odd:
        print('  all consistent')
    print('  (a wrong label is what caused V15 - verify against the physical source)')

    # ---- which buses can reach a loudspeaker in the room -------------------
    print('\n=== CAN THIS BUS MAKE SOUND IN THE ROOM? (feedback reachability) ===')
    ROOM = {'LCL-2', 'LCL-3', 'LCL-6', 'LCL-7', 'LCL-8'}  # PA + wedge local outs
    for b in range(1, 17):
        bs = d['bus'][str(b)]
        phys = patched.get(b, [])
        mains = [m for m in '1234' if bs['main'][m]['on']]
        room = bool(mains) or any(p.startswith('A-') and int(p.split('-')[1]) <= 8 for p in phys) \
               or any(p in ROOM for p in phys)
        onward = [k for k, _ in send_dests(bs)]
        print('  Bus %-2d %-12s %-22s %s' % (b, bus_name(d, b)[:12],
              'ROOM' if room else 'not in the room',
              ('-> also feeds %s' % onward) if onward else ''))

    print('\n' + '=' * 72)
    if issues:
        print('%d THING(S) TO LOOK AT BEFORE SHIPPING:\n' % len(issues))
        for n, s in enumerate(issues, 1):
            print('  %d. %s' % (n, s))
    else:
        print('No coupling issues found.')
    return issues

def impact(old, new):
    """Every object that references anything the diff touched."""
    def flat(o, p=''):
        if isinstance(o, dict):
            for k, v in o.items():
                yield from flat(v, p + '/' + k)
        else:
            yield p, o
    a, b = dict(flat(old)), dict(flat(new))
    changed = sorted(k for k in a if k in b and a[k] != b[k])
    print('\n' + '=' * 72)
    print('=== IMPACT OF THE DIFF (%d values changed) ===' % len(changed))
    buses = sorted({int(k.split('/')[2]) for k in changed if k.startswith('/bus/')})
    for bnum in buses:
        print('\n  Bus %d (%s) was changed. Everything that references it:' % (bnum, new['bus'][str(bnum)].get('name') or '?'))
        feeders = [c for c in range(1, 41)
                   if new['ch'][str(c)]['send'][str(bnum)]['on']
                   and new['ch'][str(c)]['send'][str(bnum)]['lvl'] > -100]
        print('    fed by %d channels: %s' % (len(feeders), feeders))
        print('    feeds: %s' % ([k for k, _ in send_dests(new['bus'][str(bnum)])] or 'nothing'))
        for ob in range(1, 17):
            if ob != bnum and new['bus'][str(ob)]['send'].get(str(bnum), {}).get('on'):
                print('    *** Bus %d (%s) also sends INTO it' % (ob, new['bus'][str(ob)].get('name')))
    if not buses:
        print('  no bus-level changes')

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    issues = report(load(sys.argv[1]))
    if len(sys.argv) > 2:
        impact(load(sys.argv[1]), load(sys.argv[2]))
    sys.exit(1 if issues else 0)
