import random
from game.combat import fight


def explore(player):
    
    num = random.randint(0,3)

    if (num <= 2):
        fight(player)
    
    else:
        print("You found some loot!")
    

