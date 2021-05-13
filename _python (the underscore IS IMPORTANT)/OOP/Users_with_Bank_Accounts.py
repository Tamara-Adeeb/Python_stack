class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.balance = balance
        self.interest_rate = 0.01
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance < self.balance - amount:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
        return self
    def display_account_info(self):
        print("Balance:",self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        return self
        
class Users:
    def __init__(self,name,email,int_rate = 0.01,balance=0):
        self.name = name 
        self.email = email
        self.account = [BankAccount(int_rate, balance)]
    def make_account (self,int_rate=0.01, balance=0):
        self.account.append(BankAccount(int_rate, balance))
    def make_deposit(self, amount,index=0):
        self.account[index].deposit(amount)
        return self
    def make_withdrawal(self, amount,index=0):
        self.account[index].withdraw(amount)
        return self
    def display_user_balance(self,index=0):
        print("User:", self.name, ", Balance:", self.account[index].balance)
        return self
    def transfer_money(self, other_user, amount, index=0):
        self.account[index].withdraw(amount)
        other_user.make_deposit(amount)
        return self

Tamara = Users("Tamara Adeeb","email" )
Adeeb = Users("Adeeb Adeeb","email")
Ali = Users("ALi Adeeb", "email")
acount1 = BankAccount(0.1, 1000)
acount2 = BankAccount(0.1, 1100)

Tamara.make_deposit(1000).display_user_balance()
Tamara.make_deposit(400).display_user_balance()
Tamara.make_account(acount1)
Tamara.make_account(acount2)
Tamara.display_user_balance(1)
Tamara.make_deposit(500,1)
Tamara.display_user_balance(1)





