# pip install pytest
import pytest

class BankAccount:

    def __init__(self, owner: str, initial_balance: float = 0.0):

        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")

        self.owner = owner
        self.balance = initial_balance


    def deposit(self, amount: float):

        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self.balance += amount

        return self.balance


    def withdraw(self, amount: float):

        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount

        return self.balance


    def transfer(self, amount: float, target_account: "BankAccount"):

        if not isinstance(target_account, BankAccount):
            raise TypeError("Target must be BankAccount")

        self.withdraw(amount)

        target_account.deposit(amount)

        return True


    def get_balance(self):

        return self.balance



# Unit tests using pytest
def test_create_account():

    account = BankAccount("Alice", 100)

    assert account.owner == "Alice"
    assert account.balance == 100

print(test_create_account())


# Deposit tests
def test_deposit():

    account = BankAccount("Alice", 100)

    new_balance = account.deposit(50)

    assert new_balance == 150

print(test_deposit())


# Withdraw tests
def test_withdraw():

    account = BankAccount("Alice", 100)

    new_balance = account.withdraw(40)

    assert new_balance == 60

print(test_withdraw())


# Test insufficient funds
def test_withdraw_insufficient():

    account = BankAccount("Alice", 100)

    with pytest.raises(ValueError):

        account.withdraw(200)

print(test_withdraw_insufficient())


# test transfer between accounts
def test_transfer():

    alice = BankAccount("Alice", 100)
    bob = BankAccount("Bob", 50)

    alice.transfer(30, bob)

    assert alice.balance == 70
    assert bob.balance == 80

print(test_transfer())


# deposit negative amount should raise error
def test_deposit_negative():

    account = BankAccount("Alice", 100)

    with pytest.raises(ValueError):

        account.deposit(-10)

print(test_deposit_negative())


