# -------- RAIL FENCE ENCRYPTION --------
def encrypt(text, key):
    # Create empty rails (each rail is a list)
    rail = []
    for i in range(key):
        rail.append([])

    row = 0
    direction = 1   # 1 = going down, -1 = going up

    # Place characters in zig-zag pattern
    for ch in text:
        rail[row].append(ch)

        # Change direction at top or bottom
        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row = row + direction

    # Read rows to form ciphertext
    cipher = ""
    for r in range(key):
        for ch in rail[r]:
            cipher += ch

    return cipher



# -------- RAIL FENCE DECRYPTION --------
def decrypt(cipher, key):
    # Step 1 → Make empty matrix with newlines
    rail = []
    for i in range(key):
        rail.append(['\n'] * len(cipher))

    # Step 2 → Mark zig-zag path with '*'
    row = 0
    direction = 1

    for i in range(len(cipher)):
        rail[row][i] = '*'

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row = row + direction

    # Step 3 → Fill the cipher letters row by row
    index = 0
    for r in range(key):
        for c in range(len(cipher)):
            if rail[r][c] == '*' and index < len(cipher):
                rail[r][c] = cipher[index]
                index += 1

    # Step 4 → Read zig-zag to reconstruct plaintext
    plaintext = ""
    row = 0
    direction = 1

    for i in range(len(cipher)):
        plaintext += rail[row][i]

        if row == 0:
            direction = 1
        elif row == key - 1:
            direction = -1

        row = row + direction

    return plaintext



# ---------- MAIN ----------
text = input("Enter plaintext: ")
key = int(input("Enter number of rails: "))

cipher = encrypt(text, key)
print("Ciphertext:", cipher)

decrypted = decrypt(cipher, key)
print("Decrypted text:", decrypted)
