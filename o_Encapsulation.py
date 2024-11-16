# Scenario: Imagine you are developing a software application for a bank that includes a
# BankAccount class. The class should manage customers' account balances, allowing deposits,
# withdrawals, and balance checks. For security and integrity, it’s important to restrict direct access
# to the account balance, ensuring only authorized methods can modify or view it.
#---------------------------
# Question:
##########
# 1. Create a BankAccount class that includes the following:
# ○ A private variable for the account balance.
# ○ Public methods for:
# ■ Deposit: Adds a specified amount to the account balance.
# ■ Withdraw: Subtracts a specified amount from the account balance,
# ensuring the balance does not go below zero.
# ■ Check Balance: Returns the current balance without allowing direct
# access to the balance variable.
##########
# 2. Perform the following actions:
# ○ Deposit money into an account.
# ○ Attempt a withdrawal larger than the current balance to ensure the account does
# not go negative.
# ○ Check the balance.
#---------------------------
# Answer:
#---------------------------



class BankAccount:
    def __init__(self, initial_balance=0):
        # Private variable for account balance
        self._balance = initial_balance

    # Public method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}. Current balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")

    # Public method to withdraw money
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
                print(f"Withdrew ${amount}. Current balance: ${self._balance}")
            else:
                print("Insufficient funds for withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    # Public method to check balance (no direct access to _balance)
    def check_balance(self):
        return f"Current balance: ${self._balance}"


# Creating an account with an initial balance of $100
account = BankAccount(100)

# 1. Deposit money into the account
account.deposit(50)

# 2. Attempt a withdrawal larger than the current balance
account.withdraw(200)  # Insufficient funds

# 3. Check the balance
print(account.check_balance())
