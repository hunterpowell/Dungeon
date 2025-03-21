import random
import math

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
            return(tmp)
        
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
        
        stats_text = ("STATS\n")
        stats_text += ("=================\n")
        stats_text += (f"Name:       {self.name}\n")
        stats_text += (f"Health:      {self.health}\n")
        stats_text += (f"Base accuracy: {self.accuracy}\n")
        stats_text += (f"Base on-hit:   {self.on_hit}\n")
        stats_text += (f"Armor:        {self.ac}\n")
        return stats_text

        
    def is_poisoned(self, opponent):
        if self.poisoned == True:
            poison = math.ceil((self.health / 20) + opponent.attunement)
            print(f"{self.name} is poisoned! It took {poison} damage!")
            self.health -= poison