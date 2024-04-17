import random
from characters.character import Character

class Mob(Character):
    def __init__(self, name, health, accuracy, on_hit, ac):
        super().__init__(name, health, accuracy, on_hit, ac)

    @classmethod
    def random_enemy(cls):
        enemies = [
            ("Rat", 10, 2, 3, 1),
            ("Goblin", 30, 5, 7, 5),
            ("Slime", 50, 1, 3, 10),
            ("Scatterer", 20, 3, 5, 3),
            ("Rot Sticker", 25, 5, 3, 5),
        ]

        name, health, accuracy, on_hit, ac = random.choice(enemies)
        return cls(name, health, accuracy, on_hit, ac)
