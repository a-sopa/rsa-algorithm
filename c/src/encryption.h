#ifndef ENCRYPTION_H
#define ENCRYPTION_H

#include "my_library.h"

unsigned long long power(unsigned long long base, unsigned long long exp, unsigned long long mod);

int encrypt(char text[], KeyPair public_key, unsigned long long *cipher);

#endif