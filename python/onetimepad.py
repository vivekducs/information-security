def encrypt(text, key):
    result = ""
    for i in range(len(text)):
        p = ord(text[i]) - ord('A')      # convert to 0–25
        k = ord(key[i]) - ord('A')
        c = (p + k) % 26                 # OTP encryption
        result += chr(c + ord('A'))      # convert back A–Z
    return result


def decrypt(cipher, key):
    result = ""
    for i in range(len(cipher)):
        c = ord(cipher[i]) - ord('A')
        k = ord(key[i]) - ord('A')
        p = (c - k) % 26                 # OTP decryption
        result += chr(p + ord('A'))
    return result


# ----- MAIN ------
text = input("Enter plaintext (A-Z only): ").upper()
key  = input("Enter key (same length): ").upper()

if len(text) != len(key):
    print("Length does not match... try again")
else:
    cipher = encrypt(text, key)
    print("Ciphertext:", cipher)

    decrypted_plaintext = decrypt(cipher, key)
    print("Decrypted Plaintext:", decrypted_plaintext)
