import random
from argon2.low_level import hash_secret_raw, Type # type: ignore
import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM # type: ignore
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC # type: ignore
from cryptography.hazmat.primitives import hashes # type: ignore

def generate_salt():
    salt = os.urandom(16)
    return salt


def Key_Derive(password, salt):
    key = hash_secret_raw(
        secret=password.encode(),
        salt=salt,
        time_cost=3,
        memory_cost=64 * 1024,
        parallelism=2,
        hash_len=32,
        type=Type.ID

    )
    return key


def encrypt(plaintext_bytes, key):

    aes = AESGCM(key)
    nonce = os.urandom(12)
    ciphertext = aes.encrypt(nonce, plaintext_bytes, None)
    return nonce, ciphertext


def decrypt(nonce, ciphertext, key):
    aes = AESGCM(key)
    plaintext_bytes = aes.decrypt(nonce,ciphertext,None)
    return plaintext_bytes.decode()
