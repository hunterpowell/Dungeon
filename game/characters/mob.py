import random
from game.characters.character import Character

class Mob(Character):
    def __init__(self, name, health, atk, dmg, ac):
        super().__init__(name, health, atk, dmg, ac)

    # GOATED WAY TO HANDLE THIS SHIT, INHERITANCE BABY
    @classmethod
    def random_enemy(cls):
        enemies = [
            ("Rat", 10, 2, 2, 1),
            ("Goblin", 30, 5, 5, 5),
            ("Slime", 50, 1, 1, 10)
        ]

        name, health, atk, dmg, ac = random.choice(enemies)
        return cls(name, health, atk, dmg, ac)


