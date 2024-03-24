class Player:
    def __init__(self, name):
        self.name = name   
        self.health = 100           # default health is 100
        self.atk = 5                # default atk bonus is 5
        self.scrolls = 0

    def display_player(self):
        print("\n    STATS")
        print("=============")
        print("Name:    ", self.name)
        print("Health:  ", self.health)
        print("Attack:  ", self.atk)
        print("Scrolls: ", self.scrolls)