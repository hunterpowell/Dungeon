import random
from utils import press_enter
from combat import fight


def explore(player):
    
    num = random.randint(0,3)

    if (num <= 2):
        fight(player)
    
    else:
        num2 = random.randint(0, 4)

        if num2 == 4:
            weapon = player.weapons()
            pickup = input(f"You found a {weapon}!\n"
                  "Equipping will remove any other weapon you have.\n"
                  "Would you like to equip it? [y] or [n]: ")
            if pickup == "y":
                print(f"{weapon} equipped!")
                player.weapon = weapon
            else:
                print(f"{weapon} discarded. I sure hope you don't regret that in the near future!\n")
        
        else:
            print("You found some loot!")
            money = random.randint(20,50)
            player.gold += money
            print(f"{money} gold acquired!")
  
        press_enter()
