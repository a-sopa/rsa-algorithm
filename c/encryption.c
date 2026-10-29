#include "my_library.h"

// ***Encryption***


unsigned long long power(unsigned long long base, unsigned long long exp, unsigned long long mod){
    unsigned long long result = 1;
    base = base % mod;

    //Avoid Overflows
    while (exp > 0){
        //Multiply the result by the base, if the exponent is odd
        if (exp % 2 == 1){
            result = (result * base) % mod;
        }

        exp = exp >> 1; //Divide exponent by 2
        base = (base*base) % mod;
    }
    
    return result;
}

int encrypt(char text[], KeyPair public, unsigned long long *cipher){
    int i = 0;
    for (i = 0; text[i] != '\0'; i++){
        cipher[i] = power((unsigned char)text[i], public.exponent, public.module);
    }

    return i;
}