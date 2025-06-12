# Class name
class BankAccount:
    def __init__(self, initial_balance = 0.0):
        self.account_balance =round (float((initial_balance)) ,2)
#Encapsulation and Behaviors
    def deposit(self, amount):
        "Add money to the account"
        if amount > 0:
            self.account_balance += amount
            return True
        return False # Invalid deposit amount
    
    def withdraw( self, amount):
        "Remove money from the account"
        if 0 < amount <= self.account_balance:
            self.account_balance <= amount
            return True
        return False # If theres no enough money to withdraw
    
    def display_balance(self):
        "show current balance"
        print(f"current balance: ${self.account_balance:.2f}")
        
        
    

