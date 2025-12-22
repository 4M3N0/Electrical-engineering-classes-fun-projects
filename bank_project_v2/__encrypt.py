#encryption process#


import random
import string





def generate_seed():
    new_seed = random.randint(100000, 99999999999999999999999999999999)
    return new_seed

def encrypt(password):
    
    seed = generate_seed()
    random.seed(seed)
    
    alphabet = list(string.ascii_letters)
    integers = list("0123456789")

    shuffled_alphabet = alphabet.copy()
    random.shuffle(shuffled_alphabet)

    shuffled_digits = integers.copy()
    random.shuffle(shuffled_digits)

    alphabet_encrypt = list(range(len(alphabet)))
    random.shuffle(alphabet_encrypt)

    letter_mapping = {letter: str(alphabet_encrypt[i]) for i, letter in enumerate(alphabet)}

    digit_mapping = dict(zip(integers, shuffled_alphabet[:10]))

    #encrypted = ""
    
    tokens = []
    for char in password:
        if char.isalpha():
            tokens.append(letter_mapping[char])
        elif char.isdigit():
            tokens.append(digit_mapping[char])
        else:
            tokens.append(char)
        
    return "-".join(tokens), seed




#encrypted_passwords[seed] = encrypt(password)
#print(encrypted_passwords)

