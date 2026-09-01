#include "my_library.h"

// ***Encryption***




int encrypt(char text[], KeyPair public, unsigned long long *cipher){

    int ascii[ARRAY_MAX];
    int len = convert_text_to_ascii(text);

    for (int i = 0; i < len; i++){
        cipher[i] = power(ascii[i], public.exponent, public.module);
    }

    return len;
}