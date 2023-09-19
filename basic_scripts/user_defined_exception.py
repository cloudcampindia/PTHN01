class InsufficientBalance(Exception):
    def __init__(self, message="Insufficient Balance"):
        self.message = message
    def __str__(self):
        return self.message

class Account:
    def __init__(self, accountNo, balance):
        self.accountNo = accountNo
        self.balance = balance

    def showBalance(self):
        print("Your current balance is", self.balance)
    
    def withdraw(self, amount):
        if self.balance < amount: # amount > self.balance
            raise InsufficientBalance
        self.balance -= amount # self.balance = self.balance - amount
        print("You have withdrawn:", amount)
        self.showBalance()

user1 = Account(accountNo=100, balance=10000)
user1.showBalance()
try:
    user1.withdraw(3000)
    user1.withdraw(8000)
except InsufficientBalance as e:
    print(e)