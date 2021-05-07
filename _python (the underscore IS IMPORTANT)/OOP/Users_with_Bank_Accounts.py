class BankAccount:
    def __init__(self, int_rate, balance):
        self.balance = 0
        self.interest_rate = int_rate
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if self.balance < self.balance - amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
    def display_account_info(self):
        print("Balance:",self.balance)
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate

class Users:
    def __init__(self,name,email):
        self.name = name 
        self.email = email
        self.account = BankAccount(int_rate, balance)
    def make_deposit(self, amount):
        self.account.deposit(amount)
    def make_withdrawal(self, amount):
        self.account.withdraw(amount)
    def display_user_balance(self):
        print("User:", self.name, ", Balance:", self.account.balance)
    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.make_deposit(amount)
