# get order of columns from key:
# e.g. key = "ZEBRA" -> sorted letters = A, B, E, R, Z -> order = [4,2,1,3,0]
def get_key_order(key):
    # make a list of pairs (char, original_index)
    pairs = []
    for i in range(len(key)):
        pairs.append((key[i], i))
    # sort pairs by char (stable sort keeps earlier index first for duplicate letters)
    pairs_sorted = sorted(pairs, key=lambda x: x[0])
    # create an order list where order_position -> original_column_index
    order = []
    for p in pairs_sorted:
        order.append(p[1])
    return order


# Encrypt plaintext using columnar transposition and keyword
def encrypt(plaintext, key):
    # remove spaces from plaintext. If you want to keep spaces comment this out.
    text = ""
    for ch in plaintext:
        if ch != " ":
            text += ch

    # number of columns = length of key
    cols = len(key)

    # pad text with 'X' so it fills complete rectangle
    remainder = len(text) % cols
    if remainder != 0:
        pad_len = cols - remainder
        for i in range(pad_len):
            text += 'X'

    # number of rows after padding
    rows = len(text) // cols

    # create a matrix (list of lists) with rows rows and cols cols, fill row-wise
    matrix = []
    index = 0
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(text[index])
            index += 1
        matrix.append(row)

    # get column order based on key (list of original indices in sorted-key order)
    order = get_key_order(key)

    # read columns in the order determined by the key to form ciphertext
    cipher = ""
    for col_index in order:
        for r in range(rows):
            cipher += matrix[r][col_index]

    return cipher


# Decrypt ciphertext using columnar transposition and keyword
def decrypt(ciphertext, key):
    cols = len(key)
    # number of rows (we padded during encryption so this divides exactly)
    rows = len(ciphertext) // cols

    # prepare empty matrix (rows x cols) filled with placeholders
    matrix = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(None)
        matrix.append(row)

    # get the order of columns (original index positions for sorted key letters)
    order = get_key_order(key)

    # split ciphertext into column chunks (each of length rows) in the same order as encryption reading
    index = 0
    for col_index in order:
        for r in range(rows):
            matrix[r][col_index] = ciphertext[index]
            index += 1

    # read the matrix row-wise to reconstruct plaintext (including padding Xs)
    plain_with_pad = ""
    for r in range(rows):
        for c in range(cols):
            plain_with_pad += matrix[r][c]

    # remove trailing padding 'X' characters that were added during encryption
    # note: this will remove only trailing X's. If original text legitimately ended with X's,
    # you would need a different padding scheme; this is simple for lab purposes.
    plaintext = plain_with_pad.rstrip('X')

    return plaintext


# ------------------ MAIN PROGRAM ------------------
if __name__ == "__main__":
    plaintext = input("Enter plaintext: ")
    key = input("Enter key (word): ")

    # simple validation
    if len(key) == 0:
        print("Key cannot be empty.")
    else:
        cipher = encrypt(plaintext, key)
        print("Ciphertext:", cipher)

        decrypted = decrypt(cipher, key)
        print("Decrypted text:", decrypted)
