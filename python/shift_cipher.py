def encrypt(text, key):
    result = ""
    for char in text:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift + key) % 26 + shift)
        else:
            result += char
    return result

def decrypt(cipher, key):
    result = ""
    for char in cipher:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift - key) % 26 + shift)
        else:
            result += char
    return result

#----- MAIN ------
text = input("Enter plaintext: ")
key = int(input("Enter key(shift value): "))

cipher = encrypt(text, key)
print("Ciphertext : ", cipher)

plaintext = decrypt(cipher, key)
print("Decrypted Plaintext: ", plaintext)