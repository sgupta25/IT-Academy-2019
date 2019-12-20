# Sarvesh Gupta
# Alien Blaster Lab 9

import random

class Hero(object):
    def __init__(self, name = "Arnold", health = 10, shield = 10, life = 1):
        self.name = name
        self.health = health
        self.shield = shield
        self.life = life

    def blast(self, enemy):
        print("The hero blasts an enemy.")
        enemy.die()

    def die(self):
        if self.life != 0:
            print("You just nicked me.\n")
            self.health = self.health - 1

        if self.health == 0:
            self.life = 0
            print("Ok, you got me. ", self.name, " dies.")
            print("We will now have a moment of silence for our friend,", self.name,".\n")

class Alien(object):
    def __init__(self, name = "Alien", health = 10, shield = 10, life = 1):
        self.name = name
        self.health = health
        self.shield = shield
        self.life = life

    def blast(self, enemy):
        print("The alien blasts the player.")
        enemy.die()

    def die(self):
        if self.life != 0:
            print("You can't even hit a schlurg.\n")
            self.health = self.health - 1

        if self.health == 0:
            self.life = 0
            print("The alien gasps and says, 'Oh, this is it.  This is the big one. \n"
                "Yes, it's getting dark now.  Tell my 1.6 million larvae that I loved them... \n"
                "Good-bye, cruel universe.'\n" 
                "  ... we will now give silence for a few seconds for each larvae to say a few words for Zxblrb. \n" 
                "Wklsdf fdocmvowz foew. \n" 
                "Wklsdf fdocmvowz foew. \n" 
                "Ok, shut up!\n")


def main():
    print("\t\tThe Alien Wars\n")

    hero = Hero()
    invader = Alien()


    while hero.life != 0 and invader.life != 0:
        hit_or_no = random.randint(0, 1)

        if hit_or_no == 1:
            hero.blast(invader)
        else:
            invader.blast(hero)

main()
print("Game Over")
input("\n\nPress the enter key to exit.")
