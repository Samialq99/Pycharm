class BankAccount:
    def __init__(self, bal=int):
        self.__balance = int(bal)


    def deposit(self, amount=int):
        self.__balance=int(self.__balance) + int(amount)

    def withdraw(self, amount=int):
        self.__balance = int(self.__balance) - int(amount)
    def get_Balance(self):
        return self.__balance