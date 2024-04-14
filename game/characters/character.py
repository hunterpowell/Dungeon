import random

class Character:
    def __init__(self, name, health, atk, dmg, ac):
        self.name = name
        self.health = health
        self.atk = atk
        self.dmg = dmg
        self.ac = ac
        self.die_type = 6
    
    def defend(self, damage):
        self.health -= damage

    def display(self):
        print("      STATS")
        print("=================")
        print("Name:        ", self.name)
        print("Health:      ", self.health)
        print("Atk bonus:   ", self.atk)
        print("Dmg bonus:   ", self.dmg)
        print("Armor:       ", self.ac)

    # normal attack
    def attack(self):
        if self.die_type == 6:
            tmp = random.randint(1, 6)
            tmp2 = random.randint(1, 6)
            return(tmp + tmp2)
        elif self.die_type == 12:
            tmp = random.randint(1, 12)
            return(tmp)
    
    # atk roll crit 
    def crit(self):
        if self.die_type == 6:
            tmp = random.randint(1,6)
            tmp2 = random.randint(1,6)
            tmp3 = random.randint(1,6)
            return(tmp + tmp2 + tmp3)
        elif self.die_type == 12:
            tmp = random.randint(1, 12)
            tmp2 = random.randint(1, 12)
            return(tmp + tmp2)
