#ifndef STRUCTS_H
#define STRUCTS_H 

typedef struct{
    unsigned long long exponent;
    unsigned long long module;
} KeyPair;

typedef struct{
    KeyPair public;
    KeyPair private;
} RSAKeys;

#endif