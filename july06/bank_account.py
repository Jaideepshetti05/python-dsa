class BankAccount:

    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance")

    def show_balance(self):
        print("Balance:", self.balance)


account = BankAccount(1000)

account.deposit(500)
account.withdraw(200)
account.show_balance()