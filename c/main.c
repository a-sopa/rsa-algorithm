#include "my_library.h"

int main(){
    RSAKeys keys = generate_keys(PRIME1, PRIME2);
    KeyPair public_key = keys.public;
    KeyPair private_key = keys.private;

    char message[ARRAY_MAX];

    printf("Public key: (%lld,%lld)\n", public_key.exponent, public_key.module);
    printf("Private key: (%lld,%lld)\n", private_key.exponent, private_key.module);

    printf("Insert text: ");
    scanf("%s", message);

    

    return 0;
}