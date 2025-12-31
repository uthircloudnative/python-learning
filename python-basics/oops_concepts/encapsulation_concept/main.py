from bank_account import BankAccount
from savings_account import SavingsAccount


savings_bank_account = SavingsAccount("Jhon", 12345,0, "Savings Account")
balance = savings_bank_account.get_balance()

print(balance)

# Deposit Amount

# This won't update the balance instead create a temproray varibale with 10 without making any change to balance.

#savings_bank_account.balance = 10
#balance = savings_bank_account.get_balance()

savings_bank_account.deposit(10)
balance = savings_bank_account.get_balance()

print(f"Balance after deposit {balance}")

savings_bank_account.deposit(30)
balance = savings_bank_account.get_balance()
print(f"Balance after deposit {balance}")
print(f"Account Number: {savings_bank_account._account_number} and Balance: {balance}")

savings_bank_account.withdraw(10)
after_withdraw = savings_bank_account.get_balance()
print(f"Balance after withdraw {after_withdraw}")
print(f"Account Number: {savings_bank_account._account_number} and Balance: {after_withdraw}")


