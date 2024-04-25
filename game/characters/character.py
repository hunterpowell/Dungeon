import random

class Character:
    def __init__(self, name, health, accuracy, on_hit, ac):
        self.name = name
        self.health = health
        self.max_hp = health
        self.accuracy = accuracy
        self.on_hit = on_hit
        self.ac = ac
        self.die_type = 6
        self.poisoned = False
    
    def defend(self, damage):
        self.health -= damage

    # normal attack
    def attack(self):
        if self.die_type == 6:
            tmp = random.randint(1, 6)
            tmp2 = random.randint(1, 6)
            return(tmp + tmp2 + self.on_hit)
        elif self.die_type == 12:
            tmp = random.randint(1, 12)
            return(tmp + self.on_hit)
    
    # accuracy roll crit 
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
    
    def display(self):
        print("      STATS")
        print("=================")
        print("Name:        ", self.name)
        print("Health:      ", self.health)
        print("Accuracy:    ", self.accuracy)
        print("On-hit bonus:", self.on_hit)
        print("Armor:       ", self.ac)

        
