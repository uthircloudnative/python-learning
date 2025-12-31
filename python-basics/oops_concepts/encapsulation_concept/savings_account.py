from bank_account import BankAccount

class SavingsAccount(BankAccount):
    def __init__(self,account_holder_name,account_number,balance, type_of_account):
        super().__init__(account_holder_name,account_number,balance)
        self.type_of_account = type_of_account
        