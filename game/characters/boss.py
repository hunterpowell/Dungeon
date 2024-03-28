import random
from game.characters.character import Character

class Boss(Character):
    def __init__(self, name, health, atk, dmg, ac):
        super().__init__(name, health, atk, dmg, ac)

    @classmethod
    def random_boss(cls):
        bosses = [
            ("THE JUICER", 200, 10, 10, 15),
            ("THE HOARDER", 300, 0, 5, 15),
            ("BALL OF SWINE", 100, 20, 15, 15)
        ]

        name, health, atk, dmg, ac = random.choice(bosses)
        return cls(name, health, atk, dmg, ac)
