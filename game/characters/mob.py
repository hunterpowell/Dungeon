import random
from characters.character import Character

class Mob(Character):
    def __init__(self, name, health, accuracy, on_hit, ac):
        super().__init__(name, health, accuracy, on_hit, ac)

    @classmethod
    def random_enemy1(cls):
        enemies = [
            ("Rat", 10, 2, 2, 1),
            ("Goblin", 30, 5, 5, 5),
            ("Slime", 50, 1, 1, 10),
            ("Scatterer", 20, 3, 5, 3),
            ("Rot Sticker", 25, 5, 3, 5)
        ]

        name, health, accuracy, on_hit, ac = random.choice(enemies)
        return cls(name, health, accuracy, on_hit, ac)
    
    def random_enemy2(cls):
        enemies = [
            ("Brindle Grub", 20, 3, 3, 5)
            ("Danger Dingo", 50, 5, 5, 10)
            ("Mind Horror", 35, 7, 3, 5)
            ("Kobold", 50, 7, 7, 8)
            ("Slime", 100, 3, 3, 10)
        ]

        name, health, accuracy, on_hit, ac = random.choice(enemies)
        return cls(name, health, accuracy, on_hit, ac)
