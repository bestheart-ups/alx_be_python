# bank_account.py

class BankAccount:
    """A simple bank account class that encapsulates banking operations."""

    def __init__(self, initial_balance=0):
        """
        Initialize a bank account with an optional initial balance.

        Args:
            initial_balance (float): Starting balance for the account (default: 0)
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Add the specified amount to the account balance.

        Args:
            amount (float): Amount to deposit (should be positive)
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Deduct the amount from account balance if funds are sufficient.

        Args:
            amount (float): Amount to withdraw

        Returns:
            bool: True if withdrawal successful, False if insufficient funds
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False

        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.2f}")
