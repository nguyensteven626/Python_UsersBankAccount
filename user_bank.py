class BankAccount:
    def __init__(self, int_rate = .01, balance = 0):         
        self.int_rate = int_rate
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if(amount > self.balance):
            print(f"Insufficient funds: Charging a $5 fee" {})
        self.balance -= 5
        return self 

    def display_account_info(self):
        self.balance = balance
        print(f"Balance: {self.balance}")
        return self
        
    def yield_interest(self):
        self.balance * self.int_rate
        if( self.balance > 0)
        print(self.balance)
        return self

class User:
        def __init__ (self, name):
                self.name = name
                self.bankaccount = BankAccount()
        
        def make_deposit(self, amount):
                self.bankaccount.balance += amount
                return self

        def make_withdraw(self, amount):
                self.bankaccount.balance -= amount
                return self 

        def account_info(self):
                self.bankaccount.balance = balance
                print(f"Balance: {self.balance}")
                return self


