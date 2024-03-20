import random
from game.mob import Mob


def explore(player):
    
    monster = Mob()

    num = random.randint(0,3)

    if (num <= 2):
        txt = "You found a {}!"
        print(txt.format(monster.name))
    
    else:
        print("You found some loot!")
    

