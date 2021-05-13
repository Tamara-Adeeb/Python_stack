class BankAccount:
    #we can use class attribute to declare a variable insted of global varibale that i might use in my class method or attribut
    bank_name = "VenVal" #this is a class attribute it's unified for all the instant
    number_of_bank_account = 0
    def __init__(self, int_rate,balance=0):
        self.balance = balance
        self.interest_rate = int_rate
        BankAccount.number_of_bank_account += 1 #to keep track of how many acounts i did open in my bank
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if self.balance < amount:
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

acount1 = BankAccount(0.1, 1000)
acount2 = BankAccount(0.1, 1100)
acount1.deposit(10000).withdraw(100).withdraw(500).withdraw(50).display_account_info()
acount2.deposit(1000).deposit(100).withdraw(100).withdraw(50).withdraw(10).withdraw(30).display_account_info()
print(acount1.bank_name)
print(BankAccount.number_of_bank_account)