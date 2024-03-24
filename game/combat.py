import random
from game.characters.mob import Mob

def fight(player):
    
    monster = Mob()
    

    txt = "You've run into a {}!"
    print(txt.format(monster.name))

    userin = input("What would you like to do? [attack], [run], use [item]: ")

    while (userin != "attack") & (userin != "run") & (userin != "item"):
        userin = input("Please enter [attack], [run], or [item]: ")

    match userin:
        case "attack":
            hit = random.randint(6)

        # case "run":
            
        # case "item": 
            