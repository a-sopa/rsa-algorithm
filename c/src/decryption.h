#ifndef DECRYPTION_H
#define DECRYPTION_H

#include "my_library.h"

void decrypt(const unsigned long long *cipher, int len, KeyPair private_key, char *decrypted_text);

#endif