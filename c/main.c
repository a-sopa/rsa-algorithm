#include "my_library.h"

int main(){
    RSAKeys keys = generate_keys(PRIME1, PRIME2);
    KeyPair public_key = keys.public;
    KeyPair private_key = keys.private;

    char message[ARRAY_MAX];
    unsigned long long cipher[ARRAY_MAX];

    printf("Public key: (%lld,%lld)\n", public_key.exponent, public_key.module);
    printf("Private key: (%lld,%lld)\n", private_key.exponent, private_key.module);

    printf("Insert text: ");
    
    if (fgets(message, sizeof(message), stdin) != NULL){
        message[strcspn(message, "\n")] = '\0'; //Remove the \n character
    }

    int len = encrypt(message, public_key, cipher);

    for (int i = 0; i < len; i++){
        printf("%lld ", cipher[i]);
    }
    printf("\n");

    return 0;
}