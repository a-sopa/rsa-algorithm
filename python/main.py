PUBLIC = tuple() #public - (e,n)
PRIVATE = tuple() #private - (d,n)

#*** MAIN ***

def main():
    text = input("Insert text to encrypt: ")
    PUBLIC, PRIVATE = key_generator(2377, 7573)

    print(PUBLIC)
    print(PRIVATE)

    encrypted_list = encrypt(text, PUBLIC)
    print(encrypted_list)


#def power()

# *** KEY GENERATION ***
def key_generator(p, q):
    #p = 2377
    #q = 7573

    n = p * q
    phi = (p - 1)*(q - 1)

    e = encryption_exponent(phi, n)
    d = decryption_exponent(phi, e)

    return (e,n), (d,n)

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


# *** ENCRYTPTION ***

def encrypt(text, PUBLIC):
    e, n = PUBLIC
    M = convert_text_to_ascii(text)
    C = []
    for num in M:
        encrypted_num = pow(num, e, n)
        C.append(encrypted_num)
    return C

def convert_text_to_ascii(text):
    M = []
    for l in text:
        if l == '\n':
            break
        M.append(ord(l))
    return M


main()