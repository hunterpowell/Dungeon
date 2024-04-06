import random
import os
from game.combat import fight


def explore(player):
    
    num = random.randint(0,3)

    if (num <= 2):
        fight(player)
    
    else:
        print("\nYou found some loot!")
        money = random.randint(10,50)
        player.gold += money
        print(f"{money} gold acquired!")

    os.system('cls')
