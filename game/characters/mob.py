import random

class Mob:
    def __init__(self):
        
        num = random.randint(0,3)
        match num:
            case 0:
                self.name = "rat"
                self.health = 10
                self.atk = 2        # bonus to attack roll (determines hit/miss)
                self.dmg = 0        # damage added to the dmg roll
                self.ac = 1
            case 1: 
                self.name = "goblin"
                self.health = 30
                self.atk = 5
                self.dmg = 3
                self.ac = 5
            case 2:
                self.name = "slime"
                self.health = 50
                self.atk = 1
                self.dmg = 0
                self.ac = 10


    def display_mob(self):
        print("\n    STATS")
        print("=============")
        print("Name:    ", self.name)
        print("Health:  ", self.health)
        print("Attack:  ", self.atk)
        print("Armor:   ", self.ac)
