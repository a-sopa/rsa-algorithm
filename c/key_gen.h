#include "my_library.h"

int gcd(unsigned long long a, unsigned long long b);

int encryption_exponent(unsigned long long phi, unsigned long long n);

int decryption_exponent(unsigned long long phi, unsigned long long e);

RSAKeys generate_keys(long int p, long int q);
