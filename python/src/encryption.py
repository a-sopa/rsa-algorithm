def convert_text_to_ascii(text):
    M = []
    for l in text:
        if l == '\n':
            break
        M.append(ord(l))
    return M

def encrypt(text, PUBLIC):
    e, n = PUBLIC
    M = convert_text_to_ascii(text)
    C = []
    for num in M:
        encrypted_num = pow(num, e, n)
        C.append(encrypted_num)
    return C