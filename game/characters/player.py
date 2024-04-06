# import random
from game.characters.character import Character

class Player(Character):
    def __init__(self, name):
        super().__init__(name, health = 100, atk = 3, dmg = 5, ac = 15)
        self.scrolls = 0
        self.gold = 20
        self.lvl = 1
        # self.weapon = ADD WEAPONS, USE DICT TO DETERMINE BONUS DAMAGE 
        # self.class = ADD CLASSES, DIFF SPECIAL ABILITY BASED ON CLASS, DIFF CLASSES available BASED ON WEAPON



    def inventory(self):
        print("    INVENTORY")
        print("=================")
        print("Scrolls: ", self.scrolls)
        print("Gold:    ", self.gold)


    def death(self):
        print(f"Nice try {self.name}, you made it further than any of us thought you would. Have fun in hell!\n")
        self.display()
        input()                    # requires enter to be pressed before program closes
        exit()

        