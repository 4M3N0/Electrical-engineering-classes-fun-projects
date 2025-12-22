import json
from __objects__ import BankAccount

def load_accounts(filename="user_bankinfo.json"):
    try:
        with open(filename, "r") as f:
            accounts = json.load(f)
        return accounts
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_accounts(accounts, filename="user_bankinfo.json"):
    with open(filename, "w") as f:
        json.dump(accounts, f, indent=4)
        
        
def reload_user(user):
    accounts = load_accounts()
    for acc in accounts:
        if acc["username"] == user["username"]:
            return acc
    return user
    
        
def dashboard(account):
    while True:
        print("\n==============================")
        print(f"Welcome, {account['username']}")
        print(f"BankID (Transaction number): {account['bankid']}")
        print(f"Balance: ${account['balance']:.2f}")
        print("==============================")

        choice = input(
            "\n1) Transfer Money"
            "\n2) Transfer money"
            "\n3) Logout"
            "\n4) (R) to refresh page"
        ).upper()

        if choice == "1":
            transfer_balance(account)
            account = reload_user(account)
            
        elif choice == "R":
            account = reload_user(account)
            print(f"Balance: ${account['balance']}")

            
            
            
def transfer_balance(current_user):
    accounts = load_accounts()

    sender = None
    for acc in accounts:
        if acc["username"] == current_user["username"]:
            sender = acc
            break

    if sender is None:
        print("Sender not found.")
        return

    receiver_id = input("Receiver BankID: ")
    amount = float(input("Amount: $"))

    receiver = next(
        (acc for acc in accounts if acc.get("bankid") == receiver_id),
        None
    )

    if receiver is None:
        print("Receiver not found.")
        return

    if sender["balance"] < amount:
        print("Insufficient balance.")
        return

    sender["balance"] -= amount
    receiver["balance"] += amount

    save_accounts(accounts)
    
    return sender["balance"]
    
    print(f"Transferred ${amount}")
    
    
    