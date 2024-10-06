class BankAccount:
    def __init__(self,bank_balance=0):
        self.bank_balance=bank_balance

    def deposit(self,amount):
        self.bank_balance=self.bank_balance+amount

    def withdraw(self, amount):
        if 0 < amount <= self.bank_balance:
            self.bank_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"Current Balance: ${self.bank_balance:.2f}")
