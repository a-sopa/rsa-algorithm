PUBLIC = tuple() #public - (e,n)
PRIVATE = tuple() #private - (d,n)

def key_generator():
    p = 2377
    q = 7573

    n = p * q

    phi = (p - 1)*(q - 1)

    e = encryption_exponent(phi, n)
    d = decryption_exponent(phi, e)

    PUBLIC = (e,n)
    PRIVATE = (d,n)
    print(PUBLIC)
    print(PRIVATE) 

def encryption_exponent(phi, n):
    for e in range(2, n): # 1 < e < phi(N) and gcd(e, phi(N)) = 1
        if gcd(e, phi) == 1:
            return e

def decryption_exponent(phi, e):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d

def gcd(a, b):
    """Auxiliar function that calculates the gdc using the Euclides method
        a -> First Number
        b -> Second Number"""
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a

key_generator()