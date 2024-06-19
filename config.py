REWARD_BLOBZ = 1_000_000 * 1_000_000 # TODO adjust

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

FIELDS = [ c[0] for c in CONFIG ]
