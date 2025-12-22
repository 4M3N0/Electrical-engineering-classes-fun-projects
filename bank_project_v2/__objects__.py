class BankAccount:
    
    def __init__(self, name, balance=100, password=0, seed=0, email=0, bankid=0):
        self.name = name
        self.balance = balance
        self.password = password
        self.seed = seed
        self.email = email
        self.bankid = bankid
        
    def deposit(self, amount):
        self.balance += amount
        
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -=amount
            
    def to_dict(self):
        return {
            
            "username":self.name,
            "password":self.password,
            "balance":self.balance,
            "key":self.seed,
            "email":self.email,
            "bankid":self.bankid
            
            }
