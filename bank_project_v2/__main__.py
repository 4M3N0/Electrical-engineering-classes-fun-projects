import json
import random
import os
from __objects__ import BankAccount
from __encrypt import encrypt, generate_seed
from __decrypt import decrypt
from __verification import send_verification_code, confirmation_code
from dashboard import dashboard



def main():
    while True:
       print(f"Welcome to AminoBank!")
       initialize = input("Please choose an action:\n 1) Open new account,\n 2) Log in.\n 3) Help.\n")
       if initialize == "1":           
           create_account()           
       elif initialize == "2":
            login()  
       elif initialize == "3":
           change_password()                 
       else:     
           print("Invalid option. Select 1-3")
           
           
       #print(acct.username, acct.balance, acct.password)
def create_account():
    creation_result = create_password()
    username = create_username()
    encrypted_password = creation_result[0]
    seed = creation_result[1]
    result = confirmation()
    email = result[0]
    bankid = generate_bankaddress()
    confirm_code = input("Confirmation code: ")
    code = result[1]
    if confirm_code == code:
        account = BankAccount(username, 150, encrypted_password, seed, email, bankid)
        save_accounts(account)
    else:
        print("Wrong confirmation code.")
           
                   
    print("New account created!")
    print(f"Username: {account.name}\nBalance: ${account.balance}\nPassowrd(encrypted): {account.password}\nKey: {seed}\nBankID: {account.bankid}")
    

def confirmation():
    email = input("Enter your e-mail address: ")
    try:
        code = confirmation_code()
        send_verification_code(email, code)
        return email, code
    except ValueError:
        print("Something went wrong")
    else:
        print("Something went wrong, make sure its a valid email.")
               
        

def create_username():
    while True:
        username = input("Enter new username: ").strip()
        break
    return username


def create_password():
    while True:
        password = input("Enter password: ")
        confirm_password = input("Confirm password: ")
        if password == confirm_password:
            
            password_creation = encrypt(password)
            
            encrypted_password = password_creation[0]
            seed = password_creation[1]
            break
        else:
            print("Passwords don't match. Try again.")
    return encrypted_password, seed
    print(encrypted_password)

def save_accounts(account, filename="user_bankinfo.json"):
    try:
        with open(filename, "r") as f:
            accounts = json.load(f)
    except FileNotFoundError:
            accounts = []
    
    if any(acc["username"] == account.name for acc in accounts):
        raise ValueError("Username already exists!")
            
            
    #accounts = []
    accounts.append(account.to_dict())
    
    with open(filename, "w") as f:
        json.dump(accounts, f, indent=4)
    
def load_accounts(filename="user_bankinfo.json"):
    try:
        with open(filename, "r") as f:
            accounts = json.load(f)
        return accounts
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def check_login(check_username, check_password):
    accounts = load_accounts()
    for account in accounts:
        if account["username"] == check_username and account["password"] == decrypt(check_password, account["key"]):
            print(decrypt(check_password, account["key"]))
            return account
    return None


def login():
    check_username = input("Username: ")
    check_password = input("Password: ")
    account = check_login(check_username, check_password)
    if account:
        print("Logging in...")
        dashboard(account)  
    else:
        print("User does not exist, or wrong password!")

        
def change_password():
    check_username = input("")

def generate_bankaddress():
    
    bank_number = []
    
    b1 = str(random.randint(1000, 9999))
    b2 = str(random.randint(1000, 9999))
    b3 = str(random.randint(1000, 9999))
    b4 = str(random.randint(1000, 9999))
    
    bank_number += [b1, b2, b3, b4]
    
    bankid = "-".join(bank_number)
    
    return bankid


main()