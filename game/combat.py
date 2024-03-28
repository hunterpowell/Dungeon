import random
from game.characters.mob import Mob
from game.characters.boss import Boss

def fight(player):
    
    rand = random.randint(1, 10)

    if rand == 10:
        monster = Boss.random_boss()
    else:
        monster = Mob.random_enemy()

    print(f"You've run into a {monster.name}!")
    print(f"{monster.name} has {monster.health}hp")
    monster.display

    while (monster.health > 0) & (player.health > 0):
        userin = input("\nWhat would you like to do? [attack], [run], use [item]: ")

        while (userin != "attack") & (userin != "run") & (userin != "item"):
            userin = input("Please enter [attack], [run], or [item]: ")

        match userin:
            case "attack":
                
                # attack roll to determine hit/miss
                hit = random.randint(1, 20)
                if (hit + player.atk >= monster.ac):
                    print("\nYou hit!")                    
                    # monster gets hit 
                    monster.defend(player.attack())
                    print(f"{monster.name} has {monster.health}hp remaining")
                
                elif (hit + player.atk < monster.ac):
                    print("You missed!")

                if monster.health <= 0:
                    break
                
                # enemy attacks
                enemy_attack = random.randint(1, 20)
                if (enemy_attack + monster.atk >= player.ac):
                    print("\nEnemy hit!")
                    player.defend(monster.attack())
                    print(f"You have {player.health}hp remaining!")
                else:
                    print("Enemy missed!")
                
                # if player.health <= 0:
                #     player.death()

        # case "run":
            
        # case "item": 

        if monster.health <= 0:
            print(f"You beat the {monster.name}!")

        if player.health <= 0:
            player.death()
            