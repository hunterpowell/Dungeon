import random

class Mob:
    def __init__(self):
        
        num = random.randint(0,3)
        match num:
            case 0:
                self.name = "rat"
                self.health = 10
                self.atk = 2
            case 1: 
                self.name = "goblin"
                self.health = 30
                self.atk = 5
            case 2:
                self.name = "slime"
                self.health = 50
                self.atk = 1
            case 3: 
                self.name = "BOSS: The Juicer!"
                self.health = 200
                self.atk= 10

    def display_mob(self):
        print("\n    STATS")
        print("=============")
        print("Name:    ", self.name)
        print("Health:  ", self.health)
        print("Attack:  ", self.atk)

