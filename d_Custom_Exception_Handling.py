# Scenario: You are designing a banking application that processes withdrawals from an account.
# Each account has a minimum balance that must be maintained. If a withdrawal would reduce the
# balance below this minimum, it should raise a custom exception called InsufficientFundsError.
#---------------------------
# Question:
# Create a custom exception InsufficientFundsError with an appropriate message. Define a class
# BankAccount with attributes balance and min_balance. Write a method withdraw(amount) in
# BankAccount that raises an InsufficientFundsError if the withdrawal amount would bring the
# balance below the minimum allowed. Test the class and custom exception with a sample account.
#---------------------------
# Answer:
#---------------------------


# Define custom exception
class InsufficientFundsError(Exception):
    def __init__(self, message="Withdrawal denied: Insufficient funds to maintain the minimum balance."):
        super().__init__(message)

# Define the BankAccount class
class BankAccount:
    def __init__(self, balance, min_balance):
        self.balance = balance
        self.min_balance = min_balance

    def withdraw(self, amount):
        if self.balance - amount < self.min_balance:
            raise InsufficientFundsError(
                f"Cannot withdraw ${amount}. Minimum balance of ${self.min_balance} must be maintained."
            )
        self.balance -= amount
        print(f"Withdrawal successful! New balance: ${self.balance:.2f}")

# Test the implementation
try:
    # Create an account with a balance of $1000 and a minimum balance of $500
    account = BankAccount(balance=1000, min_balance=500)
    
    print("Attempting to withdraw $400:")
    account.withdraw(400)  # Should succeed

    print("\nAttempting to withdraw $200:")
    account.withdraw(200)  # Should raise InsufficientFundsError

except InsufficientFundsError as e:
    print(f"Error: {e}")
