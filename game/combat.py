import random
from game.mob import Mob

def fight(player):
    
    monster = Mob()

    txt = "You've run into a {}!"
    print(txt.format(monster.name))

    input = input("What would you like to do? [attack], [run], use [item]: ")

    while (input != "attack" & input != "run" & input != "item"):
        input = input("Please enter [attack], [run], or [item]: ")

    match input:
        case "attack":
            hit = random.randint(6)

        # case "run":
            