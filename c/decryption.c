#include "my_library.h"

void decrypt(const unsigned long long *cipher, int len, KeyPair private_key, char *decrypted_text){
    for (int i = 0; i < len; i++){
        //Get the original text
        unsigned long long decrypted_num = power(cipher[i], private_key.exponent, private_key.module);

        //Convert it from ascii to char
        decrypted_text[i] = (char)decrypted_num;
    }
    decrypted_text[len] = '\0';
}