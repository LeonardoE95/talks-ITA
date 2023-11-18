#!/usr/bin/env python3

# pip install pycryptodome

from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

IV  = b"ABCABCABCABCABCA"
KEY = b"!A%D*G-KaPdSgVkY"

def encryption_example(plaintext_bytes):
    global IV, KEY
    
    b64_plaintext = b64encode(plaintext_bytes)
    
    aes = AES.new(KEY, AES.MODE_CBC, IV)
    ciphertext_bytes = aes.encrypt(pad(b64_plaintext, AES.block_size))
        
    b64_ciphertext = b64encode(ciphertext_bytes)
    
    return b64_ciphertext

# -----------------------

def decryption_example(b64_ciphertext):
    global IV, KEY

    ciphertext_bytes = b64decode(b64_ciphertext)

    aes = AES.new(KEY, AES.MODE_CBC, IV)
    b64_plaintext = unpad(aes.decrypt(ciphertext_bytes), AES.block_size)

    plaintext_bytes = b64decode(b64_plaintext)
    
    return plaintext_bytes

# -----------------------

def main():
    plaintext = "Hello World!"
    plaintext_bytes = plaintext.encode("utf-8")
    ciphertext_bytes = encryption_example(plaintext_bytes)    
    assert decryption_example(ciphertext_bytes) == plaintext_bytes

# -----------------------
    
if __name__ == "__main__":
    main()
