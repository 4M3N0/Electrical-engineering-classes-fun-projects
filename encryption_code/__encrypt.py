#encryption process#


import random
import string

seeds = []
encrypted_passwords = {}

seed = random.randint(100000, 99999999999999999999999999999999)
random.seed(seed)
seeds.append(seed)
#print("Seed:", seed)

alphabet = list(string.ascii_letters)
integers = list("0123456789")

shuffled_alphabet = alphabet.copy()
random.shuffle(shuffled_alphabet)

shuffled_digits = integers.copy()
random.shuffle(shuffled_digits)

alphabet_encrypt = list(range(len(alphabet)))
random.shuffle(alphabet_encrypt)

letter_mapping = {letter: str(alphabet_encrypt[i]) for i, letter in enumerate(alphabet)}
reverse_letter_mapping = {v: k for k, v in letter_mapping.items()}

digit_mapping = dict(zip(integers, shuffled_alphabet[:10]))
reverse_digit_mapping = {v: k for k, v in digit_mapping.items()}

password = "admin123"

def encrypt(password):
    #encrypted = ""
    
    tokens = []
    for char in password:
        if char.isalpha():
            tokens.append(letter_mapping[char])
        elif char.isdigit():
            tokens.append(digit_mapping[char])
        else:
            tokens.append(char)
        
    return "-".join(tokens)

encrypted_passwords[seed] = encrypt(password)
#print(encrypted_passwords)





























#unique_numbers = list(range(len(alphabet)))
#random.shuffle(unique_numbers)
#alphabet_random = list(range(len(alphabet)))
#random.shuffle(alphabet_random)



#mapping = {}
#for i, letter in enumerate(alphabet):
    #mapping[letter] = str(unique_numbers[i])
#for n, number in enumerate(integers):
    #mapping[number] = str(alphabet_random[n])
    
#print(mapping)

#def encrypt_password(password, mapping):
   # encrypted = ""
    #for char in password:
    #    if char in mapping:
   #         encrypted += mapping[char]
#        else:
 #           encrypted += char
#    return encrypted
    
#password = "Hello123"
#encrypted_pw = encrypt_password(password, mapping)
#print("E: ", encrypted_pw)


