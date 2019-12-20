# Sarvesh Gupta
# Coin Toss Lab 8

import random
class Coin(object):
    """ description """

    def __init__(self, amount=20):
        self.__amount = amount
        self.toss()

    def toss(self):
        if random.uniform(0, 2) > 1:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_sideup(self):
        return self.__sideup

    def set_amount(self, amount):
        self.__amount = self.__amount + amount

    def get_amount(self):
        return str(self.__amount)


def main():
    coin1 = Coin()
    coin2 = Coin()
    while input("Do you want to continue? ").lower() == 'y':
        coin1.toss()
        coin2.toss()
        if coin1.get_sideup() == coin2.get_sideup():
            coin1.set_amount(1)
            coin2.set_amount(-1)
            print("Player 1 Wins!")
        else:
            coin1.set_amount(-1)
            coin2.set_amount(1)
            print("Player 2 Wins!")
        print("Player 1 tossed a " + coin1.get_sideup() + " and Player 2 tossed " + coin2.get_sideup())
    print("Player 1 : " + coin1.get_amount() + " cents, and Player 2 : " + coin2.get_amount() + " cents.")
    input("<ENTER> to quit.")

main()


