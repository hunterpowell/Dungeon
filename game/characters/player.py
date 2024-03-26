class Player:
    def __init__(self, name):
        self.name = name   
        self.health = 100           # default health is 100
        self.atk = 3                # default atk bonus is 5 (determines hit/miss)
        self.dmg = 5                # default dmg bonus is 5 (determines damage)
        self.ac = 15                # default ac is 15, will iterate per level
        self.scrolls = 0

    def display_player(self):
        print("\n    STATS")
        print("=============")
        print("Name:    ", self.name)
        print("Health:  ", self.health)
        print("Attack:  ", self.atk)
        print("Damage:  ", self.dmg)
        print("Armor:   ", self.ac)
        print("Scrolls: ", self.scrolls)