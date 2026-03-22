# app/crypto/tools/rsa.py

import random
from math import gcd

# Helper function to compute modular inverse using Extended Euclidean Algorithm
def modinv(a, m):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1  # Base case
        g, y, x = egcd(b % a, a)  # Recursive call
        return g, x - (b // a) * y, y
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')  # Inverse only exists if a and m are coprime
    return x % m  # Ensure result is positive

# Simple primality check (sufficient for demo purposes, not secure)
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):  # Check divisibility up to sqrt(n)
        if n % i == 0:
            return False
    return True

# Generate RSA public and private keys using primes p and q
def generate_keys(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")  # Enforce RSA requirement
    n = p * q  # RSA modulus
    phi = (p - 1) * (q - 1)  # Euler's totient function

    # Choose public exponent e
    e = 65537  # Common default choice for e
    if gcd(e, phi) != 1:
        # If e and phi are not coprime, find a valid e
        e = 3
        while gcd(e, phi) != 1:
            e += 2  # Try next odd number

    # Compute private exponent d (modular inverse of e)
    d = modinv(e, phi)

    return ((e, n), (d, n))  # Return (public_key, private_key)

# Encrypt message using RSA public key
def encrypt(message, public_key):
    e, n = public_key
    # Convert each character to its encrypted form using modular exponentiation
    return [pow(ord(char), e, n) for char in message]

# Decrypt ciphertext using RSA private key
def decrypt(ciphertext, private_key):
    d, n = private_key
    # Decrypt each number and convert back to character
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])
