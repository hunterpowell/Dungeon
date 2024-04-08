import math
from game.characters.character import Character

class Player(Character):
    def __init__(self, name):
        super().__init__(name, health = 100, atk = 3, dmg = 5, ac = 10)
        self.scrolls = 0
        self.gold = 20
        self.lvl = 1
        self.xp = 0
        self.key = False
        # self.weapon = ADD WEAPONS, USE DICT TO DETERMINE BONUS DAMAGE. ADD UNIQUE ATTACKS PER WEAPON?
        # self.class = ADD CLASSES, DIFF SPECIAL ABILITY BASED ON CLASS, DIFF CLASSES available BASED ON WEAPON

    def inventory(self):
        print("    INVENTORY")
        print("=================")
        print("Scrolls:  ", self.scrolls)
        print("Gold:     ", self.gold)
        print("Key:      ", self.key)
    
    def usable_items(self):
        print("    INVENTORY")
        print("=================")
        print("Scrolls:  ", self.scrolls)

    def level_up(self):
        while self.xp > (self.lvl/0.3)**2:
            print("Leveled up to %d!!" % (self.lvl + 1))
            self.lvl += 1
            # +1 atk, dmg, ac per 5 levels
            if self.lvl % 5 == 0:
                self.atk += 1
                self.dmg += 1
                self.ac += 1
            
    def display_player(self):
        super().display()
        print("Level:       ", self.lvl)
        print("Experience:  ", self.xp)

    def death(self):
        print("\nYOU DIED")
        print(f"Nice try {self.name}, you made it further than any of us thought you would. Have fun in hell!\n")
<<<<<<< HEAD
        self.display()
=======
        self.display_player()
>>>>>>> combat
        input()                    # requires enter to be pressed before program closes
        exit()

    