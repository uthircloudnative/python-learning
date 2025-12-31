class BankAccount:
    def __init__(self, account_holder_name,account_number,balance):
        self.account_holder_name = account_holder_name
        self._account_number = account_number
        self.__balance = balance
        
    def get_balance(self):
        return self.__balance
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount
        else:
            print("Invalid amount")
            
    def withdraw(self, amount):
        if amount > 0 and  amount <= self.__balance:
            self.__balance = self.__balance - amount
        else:
            print("Insufficent Balance")
        
        