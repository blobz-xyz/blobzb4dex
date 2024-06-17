# common
def load_data(path, fields=[['addr', 0], ['qty', 1]], skip_header=False):
    chunk = []
    for line in open(path, 'r'):
        data = {}
        rr = line.strip().split(',')
        # load/cast fields
        for (k, i) in fields:
            v = rr[i].strip()
            if k == 'addr':
                v = v.lower()
            elif k == 'qty':
                v = int(v)
            data[k] = v
        # addr start with 0x only
        if data['addr'].startswith('0x'):
            chunk.append(data)
    return chunk
