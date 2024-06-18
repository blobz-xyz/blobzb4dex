from pprint import pprint as pp
from collections import Counter
from common import *

CONFIG = [
    # 1 pts / 1 vote, 6 votes = 6 pts
    ('snapshot_org',        './src/snapshot_org.csv'),

    # n nft = n pts, no cap
    ('golden_blobz',        './src/Golden BLOBz.csv'),
    ('silver_blobz',        './src/Silver BLOBz.csv'),

    # pts between 1 - 5 base on leaderboard points
    ('galxe_leaderboard',   './src/rar/Galxe leaderboard.csv'),

    # max 5 pts per wallet
    ('blobz_x_fwx',         './src/rar/BLOBz x FWX minter_1pt.csv'),

    # pts from filename
    ('300_bitcoin',         './src/rar/300 Bitcoin Bingo Free Entry_1 pt.csv'),
    ('questn',              './src/rar/BLOBz-QuestN follower_5 pt.csv'),
    ('gull_network',        './src/rar/Gull Network_1 pt.csv'),
    ('3960_jk',             './src/rar/3,960 $JK Giveaway_1 pt.csv'),
    ('600_somdej',          './src/rar/6,000 $SOMDEJ Giveaway_1 pt.csv'),
    ('1000_lqdx',           './src/rar/1,000 $LQDX Giveaway_1 pt.csv'),
    ('100_op',              './src/rar/100 $OP Giveaway_1 pt.csv'),
    ('last_change_to_mint', './src/rar/Last_Chance_to_Mint_BLOBz!_1 pt.csv'),
    ('blobz_invasion',      './src/rar/BLOBz_Invasion__2 pt.csv'),
    ('get_golder_blobz',    './src/rar/Get_Golden_BLOBz_1 pt.csv'),
    ('fwx_trading',         './src/rar/BLOBz_FWX_Trading_Contest._1 pt.csv'),
]

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

# 4) others
for (code, path) in CONFIG[-11:]:
    qty = int(path.split('_')[-1][0]) # get qty from filename
    addrs = [ o['addr'] for o in load_data(path, [['addr', 0]], True) ]
    for addr in addrs:
        add_data(chunk, addr, code, qty)

# TODO debug remove later
for c in chunk.values(): print(c)

# TODO checksum address before report
# TODO play full quest ~ mid score of blobz-bt
# TODO google sheet for check points
