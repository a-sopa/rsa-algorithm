#include "auxiliar.c"
#include "my_library.h"

int main(){
    RSAKeys keys = generate_keys(PRIME1, PRIME2);
    KeyPair public_key = keys.public;
    KeyPair private_key = keys.private;

    printf("Public key: (%d,%d)\n", public_key.exponent, public_key.module);
    printf("Private key: (%d,%d)", private_key.exponent, private_key.module);

    return 0;
}