import random 
import string

def generate_random_mapping():
    letters = string.ascii_uppercase
    shuffled = random.sample(letters, len(letters))
    mapping = dict(zip(letters, shuffled))
    reverse_mapping = {v: k for k, v in mapping.items()}
    return mapping, reverse_mapping

def encrypt(text, mapping):
    return "".join(mapping.get(ch, ch) for ch in text.upper())

def decrypt(cipher, reverse_mapping):
    return "".join(reverse_mapping.get(ch, ch)for ch in cipher.upper())


# ------------- MAIN  --------------------
plaintext = input("Enter plaintext: ")
mapping, reverse_mapping = generate_random_mapping()

ciphertext = encrypt(plaintext, mapping)
print("Ciphertext : ", ciphertext)

decrypted_plaintext = decrypt(ciphertext, reverse_mapping)
print("decrypted_plaintext: ", decrypted_plaintext)