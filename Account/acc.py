class Account:

    def __init__(self, filepath):
        self.filepath = filepath
        with open(filepath, "r") as file:
            self.balance = int(file.read())

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def commit(self):
        with open(self.filepath, "w") as file:
            file.write(str(self.balance))

class Checking(Account):
    """This is a docstring"""

    def __init__(self, filepath):
        Account.__init__(self, filepath)

    def transfer(self, amount):
        self.balance -= amount
        return print(f"You have successfully transferred ${self.balance - amount} from your account\nYour remaining balance is {self.balance}.")

checking = Checking("balance.txt")
print(checking.balance)
checking.deposit(100)
print(checking.balance)
checking.commit()

print(checking.__doc__)
