
def decrypt(enc_text, PRIVATE):
    d, n = PRIVATE
    original_message = []
    #M = C^d mod(N)
    for num in enc_text:
        decrypted_num = pow(num, d, n)
        decrypted_char = chr(decrypted_num)
        original_message.append(decrypted_char)

    return "".join(original_message)
