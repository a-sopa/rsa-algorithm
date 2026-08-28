PUBLIC = tuple() #public - (e,n)
PRIVATE = tuple() #private - (d,n)

#*** MAIN ***

def main():
    text = input("Insert text to encrypt: ")
    PUBLIC, PRIVATE = key_generator(2377, 7573) #2377, 7573

    print(f"Public key: {PUBLIC}")
    print(f"Private key: {PRIVATE}")

    encrypted_list = encrypt(text, PUBLIC)

    print(encrypted_list)

    decrypted_list = decrypt(encrypted_list, PRIVATE)
    #print(decrypted_list)

    decrypted_str = list_to_str(decrypted_list)
    print(f"Original Text: {decrypted_str}")


# *** KEY GENERATION ***
def key_generator(p, q):
    """ Auxiliar function that helps generating the keys necessary to both encryption and decryption.
    """
    n = p * q 
    phi = (p - 1)*(q - 1) #Calculating phi(N)

    e = encryption_exponent(phi, n) #Calculating the encryption exponent (e)
    d = decryption_exponent(phi, e) #Calculating the decryption exponent (d)

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

def decrypt(enc_text, PRIVATE):
    d, n = PRIVATE
    original_message = []
    #M = C^d mod(N)
    for num in enc_text:
        decrypted_num = pow(num, d, n)
        decrypted_char = chr(decrypted_num)
        original_message.append(decrypted_char)

    return original_message

def list_to_str(list):
    final_str = ""
    for elem in list:
        final_str += elem
    return final_str

main()