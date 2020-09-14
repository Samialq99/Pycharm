import random
import part2

class Coin:
    def __init__(self):
        self.__sideup = 'heads'

    # the init method is used in python to initialize all objects attribs
    # the self word tells function you are working on this objects
    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = 'Heads'
        else:
            self.__sideup = 'Tails'

    def get_sideup(self):
        return self.__sideup




def main():
    my_coin = Coin()
    print("this side up")
    print(my_coin.get_sideup())
    print("tossing coin")
    my_coin.toss()

    my_coin.__sideup = "Heads"
    print("this is the side up now = " + my_coin.get_sideup())
    print("now we do it ten times")

    for count in range(10):
        my_coin.toss()
        print("this is the side up now = " + my_coin.get_sideup())

    starting_bal =(input('Enter the starting account balance in number'))
    Savingsacct = part2.BankAccount(starting_bal)
    print(Savingsacct.get_Balance())
    print("Im going to deposit 55$ in your account now see balance = ")
    Savingsacct.deposit(55)
    print(Savingsacct.get_Balance())
    print("Im going to withdraw 20$ in your account now see balance = ")
    Savingsacct.withdraw(20)
    print(Savingsacct.get_Balance())
# name = input("what is your name ?")
# print(name)


main()
