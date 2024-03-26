import random
from game.characters.mob import Mob
from game.characters.boss import Boss

def fight(player):
    
    rand = random.randint(1, 10)

    if rand == 10:
        monster = Boss()
    else:
        monster = Mob()

    print(f"You've run into a {monster.name}!")
    print(f"{monster.name} has {monster.health}hp")

    while (monster.health > 0) & (player.health > 0):
        userin = input("\nWhat would you like to do? [attack], [run], use [item]: ")

        while (userin != "attack") & (userin != "run") & (userin != "item"):
            userin = input("Please enter [attack], [run], or [item]: ")

        match userin:
            case "attack":
                
                hit = random.randint(1, 20)
                if (hit + player.atk >= monster.ac):
                    
                    print("Hit!")
                    # 1 d6
                    die = random.randint(1, 6)
                    # 2 d6
                    damage = (random.randint(1, 6) + die)
                    
                    monster.health -= damage
                    print(f"{monster.name} has {monster.health}hp remaining")
                
                elif (hit + player.atk < monster.ac):
                    print("Miss!")




        # case "run":
            
        # case "item": 
            