PUBLIC = tuple() #public - (e,n)
PRIVATE = tuple() #private - (d,n)

import sys
import os

#Allowing python to find src package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 

from src.keygen import key_generator
from src.encryption import encrypt
from src.decryption import decrypt

def main():
    text = input("Insert text to encrypt: ")
    PUBLIC, PRIVATE = key_generator(2377, 7573) #2377, 7573

    print(f"Public key: {PUBLIC}")
    print(f"Private key: {PRIVATE}")

    encrypted_list = encrypt(text, PUBLIC)
    print(encrypted_list)

    decrypted_list = decrypt(encrypted_list, PRIVATE)
    print(f"Original Text: {decrypted_list}")

if __name__ == "__main__":
    main();