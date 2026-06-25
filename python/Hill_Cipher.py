def char_to_num(c):
    """Convert character A–Z to number 0–25"""
    return ord(c) - ord('A')

def num_to_char(n):
    """Convert number 0–25 to character A–Z"""
    return chr(n + ord('A'))

def generate_key_matrix(keyword: str, n: int):
    """Generate n x n key matrix from the keyword"""
    keyword = keyword.upper().replace(" ", "")
    if len(keyword) < n * n:
        raise ValueError("Keyword too short for matrix size")
    keyword = keyword[:n*n]
    key_numbers = [char_to_num(c) for c in keyword]
    key_matrix = [key_numbers[i:i+n] for i in range(0, n*n, n)]
    return key_matrix

def prepare_message_blocks(message: str, n: int, pad: bool=True):
    """Split message into numeric blocks of size n, pad with X if needed"""
    message = message.upper()
    message = "".join([c for c in message if c.isalpha()])  # Keep only A–Z
    if pad:
        while len(message) % n != 0:
            message += "X"
    if len(message) % n != 0:
        raise ValueError("Message length not multiple of block size and padding disabled.")
    blocks = []
    for i in range(0, len(message), n):
        blocks.append([char_to_num(c) for c in message[i:i+n]])
    return blocks

def matrix_det(mat):
    """Compute determinant of matrix (recursive expansion)"""
    n = len(mat)
    if n == 1:
        return mat[0][0]
    if n == 2:
        return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
    det = 0
    for col in range(n):
        minor = [[mat[r][c] for c in range(n) if c != col] for r in range(1, n)]
        cofactor = ((-1) ** col) * matrix_det(minor)
        det += mat[0][col] * cofactor
    return det

def modinv(a, m):
    """Find modular inverse of a under mod m"""
    a = a % m
    if a == 0:
        raise ValueError("No modular inverse for 0")

    def egcd(a, b):
        if b == 0:
            return (1, 0, a)
        x, y, g = egcd(b, a % b)
        return (y, x - (a // b) * y, g)

    x, y, g = egcd(a, m)
    if g != 1:
        raise ValueError(f"No modular inverse for {a} mod {m} (gcd={g})")
    return x % m

def matrix_adjugate(mat):
    """Compute adjugate of a matrix"""
    n = len(mat)
    if n == 1:
        return [[1]]
    cofactors = [[0]*n for _ in range(n)]
    for r in range(n):
        for c in range(n):
            minor = [[mat[i][j] for j in range(n) if j != c] for i in range(n) if i != r]
            cof = ((-1) ** (r + c)) * matrix_det(minor)
            cofactors[r][c] = cof
    adj = [[cofactors[j][i] for j in range(n)] for i in range(n)]  # Transpose
    return adj

def matrix_mod_inverse_int(mat, modulus):
    """Find modular inverse of matrix under given modulus"""
    n = len(mat)
    det = matrix_det(mat)
    det_mod = det % modulus
    det_inv = modinv(det_mod, modulus)
    adj = matrix_adjugate(mat)
    inv = [[(det_inv * adj[i][j]) % modulus for j in range(n)] for i in range(n)]
    return inv

def matrix_multiply(mat, vec, modulus):
    """Multiply matrix by vector under modulus"""
    n = len(mat)
    res = [0]*n
    for i in range(n):
        s = 0
        for j in range(n):
            s += mat[i][j] * vec[j]
        res[i] = s % modulus
    return res

def encrypt_hill(message, keyword, n):
    """Encrypt message using Hill cipher"""
    key = generate_key_matrix(keyword, n)
    blocks = prepare_message_blocks(message, n, pad=True)
    cipher = ""
    for blk in blocks:
        enc = matrix_multiply(key, blk, 26)
        cipher += "".join(num_to_char(x) for x in enc)
    return cipher

def decrypt_hill(ciphertext, keyword, n):
    """Decrypt ciphertext using Hill cipher"""
    key = generate_key_matrix(keyword, n)
    inv_key = matrix_mod_inverse_int(key, 26)
    blocks = prepare_message_blocks(ciphertext, n, pad=False)
    plain = ""
    for blk in blocks:
        dec = matrix_multiply(inv_key, blk, 26)
        plain += "".join(num_to_char(x) for x in dec)
    return plain

# ------------------- Main Program -------------------
message = input("Enter Plaintext: ")
keyword = input("Enter Key (length must be a perfect square, determinant of the matrix must be coprime with 26): ")

# Calculate matrix size (n x n)
n = int((len(keyword))**0.5)
if n * n != len(keyword):
    raise ValueError("Key length must be a perfect square (e.g., 4, 9, 16).")

# Generate key matrix
key_matrix = generate_key_matrix(keyword, n)

# Encryption & Decryption
encrypted = encrypt_hill(message, keyword, n)
decrypted = decrypt_hill(encrypted, keyword, n)

# Print results
print("\nKey Matrix:")
for row in key_matrix:
    print(row)

proc = "".join([c for c in message.upper() if c.isalpha()])
while len(proc) % n != 0:
    proc += "X"

print("\nProcessed Plaintext:", proc)
print("Encrypted Text:", encrypted)
print("Decrypted Text:", decrypted)
