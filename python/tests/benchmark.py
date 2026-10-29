PUBLIC = tuple() #public - (e,n)
PRIVATE = tuple() #private - (d,n)
NUM_ITERATIONS = 10000

import sys
import os
import time

#Allowing python to find src package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))) 

from src.keygen import key_generator
from src.encryption import encrypt
from src.decryption import decrypt


def run_benchmark():
    text = "QUOTE: They didn't bring us here to change the past..."
    PUBLIC, PRIVATE = key_generator(2377, 7573) #2377, 7573

    cipher = encrypt(text, PUBLIC)

    #BENCHMARK TEST
    start = time.perf_counter()
    for _ in range(NUM_ITERATIONS):
        _ = encrypt(text, PUBLIC)
    end = time.perf_counter()
    time_enc = end - start


    start = time.perf_counter()
    for _ in range(NUM_ITERATIONS):
        _ = decrypt(cipher, PRIVATE)
    end = time.perf_counter()
    time_dec = end - start

    #BENCHMARK RESULTS
    print(f"--- PYTHON RSA BENCHMARK ({NUM_ITERATIONS} iterations) ---")
    print(f"Total encryption time: {time_enc:.6f} s (Avg: {time_enc/NUM_ITERATIONS:.8f} s/iteration)")
    print(f"Total decryption time: {time_dec:.6f} s (Avg: {time_dec/NUM_ITERATIONS:.8f} s/iteration)")


if __name__ == "__main__":
    run_benchmark();