import random

class Character:
    def __init__(self, name, health, atk, dmg, ac):
        self.name = name
        self.health = health
        self.atk = atk
        self.dmg = dmg
        self.ac = ac
    
    def defend(self, damage):
        self.health -= damage

    def display(self):
        print("    STATS")
        print("=============")
        print("Name:    ", self.name)
        print("Health:  ", self.health)
        print("Attack:  ", self.atk)
        print("Damage:  ", self.dmg)
        print("Armor:   ", self.ac)

    def attack(self):
        tmp = random.randint(1, 6)
        tmp2 = random.randint(1, 6)
        return(tmp + tmp2 + self.dmg)