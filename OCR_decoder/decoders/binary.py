from bitarray import bitarray as bit

def encode_bin(m):
    return ''.join(format(ord(c),'08b') for c in m)

def decode_bin(b):
    bits = bit(b)
    return bits.tobytes().decode('ascii')
