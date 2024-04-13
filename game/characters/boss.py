import random
from characters.character import Character

class Boss(Character):
    def __init__(self, name, health, atk, dmg, ac):
        super().__init__(name, health, atk, dmg, ac)

    @classmethod
    def random_boss(cls):
        bosses = [
            ("THE JUICER", 125, 10, 10, 10),
            ("THE HOARDER", 200, 0, 5, 10),
            ("BALL OF SWINE", 100, 20, 15, 10),
            ("ASYLUM DEMON", 150, 15, 10, 10)
        ]

        name, health, atk, dmg, ac = random.choice(bosses)
        return cls(name, health, atk, dmg, ac)
