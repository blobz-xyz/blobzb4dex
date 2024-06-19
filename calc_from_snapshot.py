from pprint import pprint as pp
from web3.utils.address import to_checksum_address
from collections import Counter
from config import *
from common import *

chunk = {}

# 1) snapshot_org, golden_blobz, silver_blobz
for (code, path) in CONFIG[:3]:
    rr = load_data(path)
    for r in rr:
        add_data(chunk, r['addr'], code, r['qty'])

# 2) galxe leaderboard
(code, path) = CONFIG[3]
rr = load_data(path, [['addr', 0], ['qty', 2]], True)
for r in rr:
    # calc qty between 1 to 5
    raw_qty = r['qty']
    calc_qty = 1
    if raw_qty > 1165:  calc_qty = 5
    elif raw_qty > 875: calc_qty = 4
    elif raw_qty > 585: calc_qty = 3
    elif raw_qty > 295: calc_qty = 2
    # update chunk data
    add_data(chunk, r['addr'], code, calc_qty)

# 3) blobz x fwx
(code, path) = CONFIG[4]
addrs = [ o['addr'] for o in load_data(path, [['addr', 0]], True) ]
addrs = dict(Counter(addrs))
for (addr, qty) in addrs.items():
    add_data(chunk, addr, code, min(qty, 5)) # max 5

# 3.1) others
for (code, path) in CONFIG[-11:]:
    qty = int(path.split('_')[-1][0]) # get qty from filename
    addrs = [ o['addr'] for o in load_data(path, [['addr', 0]], True) ]
    for addr in addrs:
        add_data(chunk, addr, code, qty)

# 4) sum points
total_points = 0
for (addr, info) in chunk.items():
    info['points'] = sum(info.values())
    total_points += info['points']

# 5) before reshape
for (addr, info) in chunk.items():
    # add checksum address
    info['addr'] = to_checksum_address(addr)
    # calc BLOBZ
    info['blobz'] = REWARD_BLOBZ * (info['points'] / total_points)

# 6) reshape chunk to list of dict
chunk = chunk.values()

# 7) sort by points, address
chunk = sorted(chunk, key=lambda x: (-x['points'], x['addr']))

# 8) add no
cur_no = None
cur_points = None
for (idx, info) in enumerate(chunk):
    if info['points'] != cur_points:
        cur_no = idx + 1
        cur_points = info['points']
    info['no'] = cur_no

# 9) print output (header)
fields = ','.join(FIELDS)
print("#,Address,BLOBZ,Points,{}".format(fields))

# 10) print output (body)
for c in chunk:
    blobz = int(c['blobz'] / 1_000_000) # million
    fields = ','.join([ str(c.get(f) or 0) for f in FIELDS ])
    print('{},{},{},{},{}'.format(
        c['no'],        # no
        c['addr'],      # addr
        blobz,          # BLOBZ (million unit)
        c['points'],    # points
        fields,         # collection points
    ))
