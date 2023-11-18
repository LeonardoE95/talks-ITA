#!/usr/bin/env python3

class OTP:
    def __init__(self, random_key):
        self.random_key = random_key

    def encrypt(self, plaintext_bytes):
        if len(plaintext_bytes) != len(self.random_key):
            print("[ERROR] - OTP length assumption is broken")
            exit()
        
        ciphertext_bytes = [0] * len(plaintext_bytes)
        for i in range(0, len(plaintext_bytes)):
            ciphertext_bytes[i] = self.random_key[i] ^ plaintext_bytes[i]
            
        return ciphertext_bytes

    def decrypt(self, ciphertext):
        return self.encrypt(ciphertext)

# ---------------------------
    
def main():
    key = list(b"keyyo")
    otp = OTP(key)
    plaintext_bytes = list(b"HELLO")
    ciphertext_bytes = otp.encrypt(plaintext_bytes)
    print(f"[key={key}] {plaintext_bytes} -> {ciphertext_bytes}")

if __name__ == "__main__":
    main()
