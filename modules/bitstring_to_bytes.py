def bitstring_to_bytes(s):
    padding = (8 - len(s) % 8) % 8
    s = s + "0" * padding
    
    n = int(s, 2)
    
    return n.to_bytes(len(s) // 8, byteorder='big')