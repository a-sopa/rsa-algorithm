def gcd(a, b):
    """Auxiliar function that calculates the gdc using the Euclides method
        a -> First Number
        b -> Second Number"""
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a

def encryption_exponent(phi, n):
    for e in range(2, n): # 1 < e < phi(N) and gcd(e, phi(N)) = 1
        if gcd(e, phi) == 1:
            return e

def decryption_exponent(phi, e):
    for d in range(2, phi):
        if (e * d) % phi == 1:
            return d

def key_generator(p, q):
    """ Auxiliar function that helps generating the keys necessary to both encryption and decryption.
    """
    n = p * q 
    phi = (p - 1)*(q - 1) #Calculating phi(N)

    e = encryption_exponent(phi, n) #Calculating the encryption exponent (e)
    d = decryption_exponent(phi, e) #Calculating the decryption exponent (d)

    return (e,n), (d,n)
