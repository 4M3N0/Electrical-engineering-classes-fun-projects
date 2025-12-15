import random
import string

#password = "admin"
def decrypt(check_password, seed):

    random.seed(seed)
    print(seed)

    alphabet = list(string.ascii_letters)
    integers = list("0123456789")

    shuffled_alphabet = alphabet.copy()
    random.shuffle(shuffled_alphabet)

    shuffled_digits = integers.copy()
    random.shuffle(shuffled_digits)

    alphabet_encrypt = list(range(len(alphabet)))
    random.shuffle(alphabet_encrypt)
    
    letter_mapping = {letter: str(alphabet_encrypt[i]) for i, letter in enumerate(alphabet)}
    #reverse_letter_mapping = {v: k for k, v in letter_mapping.items()}

    digit_mapping = dict(zip(integers, shuffled_alphabet[:10]))
    #reverse_digit_mapping = {v: k for k, v in digit_mapping.items()}

    tokens = []
    for char in check_password:
        if char.isalpha():
            tokens.append(letter_mapping[char])
        elif char.isdigit():
            tokens.append(digit_mapping[char])
        else:
            tokens.append(char)
        encrypted = "-".join(tokens)
    return encrypted

    
#encrypted_passwords[seed] = encrypt(password)
#print(encrypted_passwords)

