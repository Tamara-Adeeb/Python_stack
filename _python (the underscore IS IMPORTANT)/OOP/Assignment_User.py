class Users:
    def __init__(self,name,email):
        self.name = name 
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print("User:", self.name, ", Balance:", self.account_balance)
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.make_deposit(amount)
    
Tamara = Users("Tamara Adeeb","email")
Adeeb = Users("Adeeb Adeeb","email")
Ali = Users("ALi Adeeb", "email")
Tamara.make_deposit(1000)
Tamara.make_deposit(200)
Tamara.make_deposit(50)
Tamara.make_withdrawal(30)
Adeeb.make_deposit(1000)
Adeeb.make_withdrawal(50)
Adeeb.make_withdrawal(50)
Adeeb.make_withdrawal(50)
Ali.make_deposit(1000)
Ali.make_withdrawal(50)
Ali.make_withdrawal(50)
Ali.make_withdrawal(50)
Tamara.transfer_money(Ali,100)


