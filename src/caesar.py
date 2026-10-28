def cipher(string, key):
    ret = []
    for c in string:
        ret.append(chr((ord(c) + key) % 255))
    return "".join(ret)

def decipher(string, key):
    ret = []
    for c in string:
        ret.append(chr((ord(c) - key) % 255))
    return "".join(ret)


