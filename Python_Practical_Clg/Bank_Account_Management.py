# Bank Account Management System

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Amount deposited:", amount)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn:", amount)
        else:
            print("Insufficient balance!")

    def display(self):
        print("Account Holder:", self.name)
        print("Current Balance:", self.balance)


# Creating an object
account = BankAccount("Anshu", 5000)

account.display()
account.deposit(2000)
account.withdraw(1000)
account.display()


OUTPUT
Account Holder: Anshu
Current Balance: 5000
Amount deposited: 2000
Amount withdrawn: 1000
Account Holder: Anshu
Current Balance: 6000

