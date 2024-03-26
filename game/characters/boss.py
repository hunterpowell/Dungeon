class Boss:
    def __init__(self):
        self.name = "THE JUICER"
        self.health = 200
        self.atk = 10
        self.dmg = 10
        self.ac = 15

    def display_mob(self):
        print("\n    STATS")
        print("=============")
        print("Name:    ", self.name)
        print("Health:  ", self.health)
        print("Attack:  ", self.atk)
        print("Armor:   ", self.ac)