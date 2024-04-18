import random
from characters.character import Character

class Boss(Character):
    def __init__(self, name, health, accuracy, on_hit, ac):
        super().__init__(name, health, accuracy, on_hit,  ac)

    @classmethod
    def random_boss1(cls):
        bosses = [
            ("JUICER", 125, 10, 10, 10),
            ("HOARDER", 200, 0, 5, 10),
            ("BALL OF SWINE", 100, 20, 15, 10),
            ("ASYLUM DEMON", 150, 15, 10, 10)
        ]

        name, health, accuracy, on_hit, ac = random.choice(bosses)
        return cls(name, health, accuracy, on_hit, ac)
    
    @classmethod
    def random_boss2(cls):
        bosses = [
            ("RALPH", 125, 20, 5, 15),
            ("KRAKAREN", 300, 3, 5, 15),
            ("CAPRA DEMON", 225, 10, 10, 10),
            ("BELL GARGOYLE", 175, 10, 20, 10) 
        ]

        name, health, accuracy, on_hit, ac = random.choice(bosses)
        return cls(name, health, accuracy, on_hit, ac)
