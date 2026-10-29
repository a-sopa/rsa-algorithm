#include "my_library.h"
#include <time.h>

int main(){
    RSAKeys keys = generate_keys(PRIME1, PRIME2);
    KeyPair public_key = keys.public;
    KeyPair private_key = keys.private;

    char message[] = "QUOTE: They didn't bring us here to change the past...";
    unsigned long long cipher[ARRAY_MAX];
    int len = strlen(message);

    struct timespec start, end;

    clock_gettime(CLOCK_MONOTONIC, &start);
    for (int i = 0; i < NUM_ITERATIONS; i++){
        encrypt(message, public_key, cipher);
    }
    clock_gettime(CLOCK_MONOTONIC, &end);
    
    double time_enc = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;

    char decrypted_message[ARRAY_MAX];

    clock_gettime(CLOCK_MONOTONIC, &start);
    for (int i = 0; i < NUM_ITERATIONS; i++){
        decrypt(cipher, len, private_key, decrypted_message);
    }
    clock_gettime(CLOCK_MONOTONIC, &end);

    double time_dec = (end.tv_sec - start.tv_sec) + (end.tv_nsec - start.tv_nsec) / 1e9;

    printf("--- (C) BENCHMARK RESULTS (%d iterations) ---\n", NUM_ITERATIONS);
    printf("Total Encryption Time: %.6f s (Avg: %.8f s/iteration)\n", time_enc, time_enc/NUM_ITERATIONS);
    printf("Total Decryption Time: %.6f s (Avg: %.8f s/iteration)\n", time_dec, time_dec/NUM_ITERATIONS);

    return 0;
}