#include "my_library.h"

// ***KEY GENERATION**

int gcd(unsigned long long a, unsigned long long b){
    while (b != 0){
        int temp = a;
        a = b;
        b = temp % b;
    }
    return a;
}

int encryption_exponent(unsigned long long phi, unsigned long long n){
    for (int e = 2; e < n; e++){
        if (gcd(phi, e) == 1)
            return e;
    }
    return -1;
}

int decryption_exponent(unsigned long long phi, unsigned long long e){
    for (int d = 2; d < phi; d++){
        if (((d * e) % phi) == 1)
            return d;
    }
    return -1;
}

RSAKeys generate_keys(long int p, long int q){
    long int n = p * q;
    long int phi = (p - 1)*(q - 1);

    int e = encryption_exponent(phi, n);
    int d = decryption_exponent(phi, e);
    KeyPair public_key, private_key;
    public_key.exponent = e;
    public_key.module = n;
    private_key.exponent = d;
    private_key.module = n;

    RSAKeys keys;
    keys.public = public_key;
    keys.private = private_key;
    
    return keys;
}
