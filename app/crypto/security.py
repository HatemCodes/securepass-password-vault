from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
import os

# Derives a secure AES key from a password and a salt using PBKDF2
def derive_key(password: str, salt: bytes) -> bytes:
    """Derive encryption key from password"""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),     # Hash function for key derivation
        length=32,                     # AES-256 requires 32-byte keys
        salt=salt,                     # Random salt for added security
        iterations=100000,            # Number of iterations (makes brute force harder)
        backend=default_backend()
    )
    return kdf.derive(password.encode())  # Derive the key from the password

# Encrypts the input data using AES in GCM mode
def encrypt_data(key: bytes, data: str) -> bytes:
    """Encrypt data using AES-GCM"""
    nonce = os.urandom(12)  # Generate a 96-bit random nonce
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(data.encode()) + encryptor.finalize()  # Perform encryption
    return nonce + encryptor.tag + ciphertext  # Concatenate nonce + tag + ciphertext

# Decrypts AES-GCM encrypted data
def decrypt_data(key: bytes, encrypted_data: bytes) -> str:
    """Decrypt AES-GCM encrypted data"""
    nonce = encrypted_data[:12]               # Extract the nonce (first 12 bytes)
    tag = encrypted_data[12:28]               # Extract the GCM tag (next 16 bytes)
    ciphertext = encrypted_data[28:]          # The rest is the ciphertext
    cipher = Cipher(algorithms.AES(key), modes.GCM(nonce, tag), backend=default_backend())
    decryptor = cipher.decryptor()
    return (decryptor.update(ciphertext) + decryptor.finalize()).decode()  # Perform decryption and decode to string
