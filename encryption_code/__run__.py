import sys, os, json
from __encrypt import encrypt, seed
from __decrypt import decrypt

if os.path.exists("user_info.json") and os.path.getsize("user_info.json") > 0:
    with open("user_info.json", "r") as file:
        user_info = json.load(file)
else:      
        user_info = [
    {
        "username": "admin",
        "password": "0-42-22-17-11-m-T-P",
        "seed": "0"
    }
]
    

def main():
    
    while True:
        proceed = input("Enter (S) to continue..").upper()
        if proceed == 'S':
            create_change = input(" Option (1): Create new password.\n Option (2): Log in\n Option (3): Reset Password.")
            if create_change == '1':
                
                username = create_username()
                encrypted_password = create_password()
                new_account = {"username": username, "seed": seed, "password": encrypted_password}
                
                user_info.append(new_account)
                
                with open("user_info.json", "w") as file:
                    json.dump(user_info, file, indent=4)
                print("New account created!")
                
            elif create_change == '2':
                log_in()
            
def create_username():
    while True:
        username = input("Enter new username: ").strip()
        #print(username)
        break
    return username
        

def create_password():
    while True:
        password = input("Enter password: ")
        confirm_password = input("Confirm password: ")
        if password == confirm_password:
            encrypted_password = encrypt(password)
            break
        else:
            print("Passwords don't match. Try again.")
    return encrypted_password
            
def log_in():
    while True:
        check_username = input("Enter username: ")
        account = next((a for a in user_info if a["username"] == check_username), None)
        if account:
            unique_seed = account["seed"]
            print(unique_seed)
            check_password = input("Enter your password: ")
            encryption = decrypt(check_password, account["seed"] )
            print(encryption)
            if encryption == account["password"]:
                remove_chars = "-"
                print("Success! decrypted: ", "".join(c for c in encryption if c not in remove_chars), "-->", check_password)
                print(f"Welcome back {check_username}")
            else:
                print("Wrong password!")
                
        return unique_seed
    

    
        if account is None:
            print("Invalid username.")
            continue
        check_password = input("Enter your password: ")
        encryption = decrypt(check_password, account["seed"] )
        if encryption == account["password"]:
            print("Success! encrypted: ", encryption)
            
     
main()
















