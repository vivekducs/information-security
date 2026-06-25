def generate_key(text, key):
    key = key.upper()
    key_extended = ""
    key_index = 0
    for ch in text:
        if ch.isalpha():
            key_extended += key[key_index % len(key)]
            key_index += 1
        else:
            key_extended += ch  # keep non-alpha chars as is like space
    return key_extended

def encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = generate_key(plaintext, key)
    ciphertext = ""

    for p, k in zip(plaintext, key):
        if p.isalpha():
            # shift by sum of plaintext and key chars mod 26
            c = (ord(p) - 65 + ord(k) - 65) % 26
            ciphertext += chr(c + 65)
        else:
            ciphertext += p

    return ciphertext

def decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = generate_key(ciphertext, key)
    plaintext = ""

    for c, k in zip(ciphertext, key):
        if c.isalpha():
            # shift back by subtracting key char from ciphertext char
            p = (ord(c) - 65 - (ord(k) - 65)) % 26
            plaintext += chr(p + 65)
        else:
            plaintext += c

    return plaintext




text = input("Enter plaintext: ")
key = input("Enter key: ")

ciphertext = encrypt(text, key)
print("Encrypted text:", ciphertext)
plaintext = decrypt(ciphertext, key)
print("Decrypted text:", plaintext)