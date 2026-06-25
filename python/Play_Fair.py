def generate_key_matrix(keyword):
    keyword = keyword.upper().replace("J", "I") 
    matrix = []
    used = set()

    for char in keyword:
        if char.isalpha() and char not in used:
            used.add(char)
            matrix.append(char)

    # Add remaining alphabet
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ": 
        if char not in used:
            used.add(char)
            matrix.append(char)

    # Convert to 5x5 matrix
    key_matrix = [matrix[i:i+5] for i in range(0, 25, 5)]
    return key_matrix

def prepare_message_pairs(message):
    message = message.upper().replace("J", "I")
    message = "".join([c for c in message if c.isalpha()])  # Keep letters only

    pairs = []
    i = 0
    while i < len(message):
        a = message[i]
        if i + 1 < len(message):
            b = message[i + 1]
            if a == b:  # Same letter → insert X
                pairs.append(a + "X")
                i += 1
            else:
                pairs.append(a + b)
                i += 2
        else:
            pairs.append(a + "X")  # Last single letter → add X
            i += 1
    return pairs

def find_position(matrix, char):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def encrypt_playfair(message, keyword):
    matrix = generate_key_matrix(keyword)
    pairs = prepare_message_pairs(message)
    encrypted = ""

    for a, b in pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  # Same row
            encrypted += matrix[row1][(col1 + 1) % 5]
            encrypted += matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  # Same column
            encrypted += matrix[(row1 + 1) % 5][col1]
            encrypted += matrix[(row2 + 1) % 5][col2]
        else:  # Rectangle rule
            encrypted += matrix[row1][col2]
            encrypted += matrix[row2][col1]

    return encrypted

def decrypt_playfair(ciphertext, keyword):
    matrix = generate_key_matrix(keyword)
    pairs = [ciphertext[i:i+2] for i in range(0, len(ciphertext), 2)]
    decrypted = ""

    for a, b in pairs:
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)

        if row1 == row2:  # Same row → shift left
            decrypted += matrix[row1][(col1 - 1) % 5]
            decrypted += matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  # Same column → shift up
            decrypted += matrix[(row1 - 1) % 5][col1]
            decrypted += matrix[(row2 - 1) % 5][col2]
        else:  # Rectangle rule
            decrypted += matrix[row1][col2]
            decrypted += matrix[row2][col1]

    return decrypted


message = input("Enter plaintext: ")
keyword = input("Enter Key: ")

encrypted = encrypt_playfair(message, keyword)
decrypted = decrypt_playfair(encrypted, keyword)

print("\nKey Matrix:")
for row in generate_key_matrix(keyword):
    print(row)

print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)