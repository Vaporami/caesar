def cipher(string, key):
    ret = []
    for i in range(len(string)):
        str_chr_id = ord(string[i])
        key_chr_id = ord(key[i % len(key)])
        ret.append(chr((str_chr_id + key_chr_id) % 256))
    return "".join(ret)

def decipher(string, key):
    ret = []
    for i in range(len(string)):
        str_chr_id = ord(string[i])
        key_chr_id = ord(key[i % len(key)])
        ret.append(chr((str_chr_id - key_chr_id) % 256))
    return "".join(ret)
