import random
import math

def is_prime(n, k=5):
    """Miller-Rabin primality test"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # Write n as d*2^r + 1
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    # Witness loop
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    """Generate a random prime number with specified bit length"""
    while True:
        p = random.getrandbits(bits)
        if p % 2 == 0:
            p += 1
        if is_prime(p):
            return p

def gcd(a, b):
    """Greatest common divisor using Euclidean algorithm"""
    while b != 0:
        a, b = b, a % b
    return a

def extended_gcd(a, b):
    """Extended Euclidean algorithm to find gcd and coefficients"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def mod_inverse(a, m):
    """Modular multiplicative inverse using extended Euclidean algorithm"""
    gcd, x, _ = extended_gcd(a, m)
    if gcd != 1:
        raise ValueError("Modular inverse does not exist")
    return x % m

def generate_keys(bit_length=1024):
    """Generate RSA public and private keys"""
    # Generate two distinct primes
    p = generate_prime(bit_length // 2)
    q = generate_prime(bit_length // 2)
    while p == q:
        q = generate_prime(bit_length // 2)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and gcd(e, phi) = 1
    e = 65537  # Common choice for e
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2

    # Compute d, the modular inverse of e modulo phi
    d = mod_inverse(e, phi)

    # Public key: (e, n), Private key: (d, n)
    public_key = (e, n)
    private_key = (d, n)

    return public_key, private_key

def encrypt(message, public_key):
    """Encrypt a message using the public key"""
    e, n = public_key
    # Convert message to integer if it's a string
    if isinstance(message, str):
        message = int.from_bytes(message.encode('utf-8'), byteorder='big')
    elif isinstance(message, int):
        pass
    else:
        raise ValueError("Message must be a string or integer")

    if message >= n:
        raise ValueError("Message too large for the key size")

    # Encrypt: c = m^e mod n
    ciphertext = pow(message, e, n)
    return ciphertext

def decrypt(ciphertext, private_key):
    """Decrypt a ciphertext using the private key"""
    d, n = private_key

    # Decrypt: m = c^d mod n
    plaintext_int = pow(ciphertext, d, n)

    # Try to convert back to string
    try:
        plaintext = plaintext_int.to_bytes((plaintext_int.bit_length() + 7) // 8, byteorder='big').decode('utf-8')
        return plaintext
    except UnicodeDecodeError:
        # If it's not a string, return as integer
        return plaintext_int

# Example usage
if __name__ == "__main__":
    # Generate keys
    public_key, private_key = generate_keys()

    # Original message
    message = "Hello, RSA!"

    # Encrypt
    encrypted = encrypt(message, public_key)
    print(f"Encrypted: {encrypted}")

    # Decrypt
    decrypted = decrypt(encrypted, private_key)
    print(f"Decrypted: {decrypted}")

    # Verify
    assert decrypted == message
    print("RSA encryption/decryption successful!")
