# common
def load_data(path, fields=[['addr', 0], ['qty', 1]], skip_header=False):
    chunk = []
    lines = [ line for line in open(path, 'r') ]
    if skip_header:
        lines = lines[1:]
    for line in lines:
        data = {}
        rr = line.strip().split(',')
        # load/cast fields
        for (k, i) in fields:
            v = rr[i].strip()
            if k == 'addr':
                v = v.lower().replace('"', '')
            elif k == 'qty':
                v = int(v)
            data[k] = v
        # addr start with 0x only
        if data['addr'].startswith('0x'):
            chunk.append(data)
    return chunk

def add_data(chunk, addr, code, qty):
    data = chunk.get(addr) or { 'addr': addr }
    data[code] = qty
    chunk[addr] = data
