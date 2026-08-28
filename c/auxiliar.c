

int generate_keys(p, q){
    long int n = p * q;
    long int phi = (p - 1)*(q - 1);

    int e = encryption_exponent(phi, n);
    int d = decryption_exponent(phi, e);
    long int public_key = (e, n);
    long int private_key = (d, n);

    return public_key, private_key;
}

int encryption_exponent(phi, n){
    for (int e = 2; e < n; e++){
        if (gcd(phi, e) == 1)
            return e;
    }
}

int decryption_exponent(phi, e){
    for (int d = 2; d < phi; d++){
        if (((d * e) % phi) == 1)
            return d;
    }
}

int gcd(int a, int b){
    while (b != 0){
        int temp = a;
        a = b;
        b = temp % b;
    }
    return a;
}