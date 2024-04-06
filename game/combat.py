import random
import os
from game.characters.mob import Mob
from game.characters.boss import Boss
from game.lore import juicer_desc, hoarder_desc, ball_desc

def fight(player):
    
    rand = random.randint(1, 10)

    if rand == 10:
        monster = Boss.random_boss()
        if monster.name == "THE JUICER":
            juicer_desc()
        elif monster.name == "THE HOARDER":
            hoarder_desc()
        else:
            ball_desc()
            
    else:
        monster = Mob.random_enemy()

    print(f"You've run into a {monster.name}!")
    print(f"{monster.name} has {monster.health}hp")
    monster.display

    while (monster.health > 0) and (player.health > 0):
        userin = input("\nWhat would you like to do? [attack], [run], use [item]: ")

        while (userin != "attack") and (userin != "run") and (userin != "item"):
            userin = input("Please enter [attack], [run], or [item]: ")

        match userin:
            case "attack":
                
                os.system('cls')
                # attack roll to determine hit/miss
                hit = random.randint(1, 20)
                if (hit + player.atk >= monster.ac):
                    print("You hit!")                    
                    # monster gets hit 
                    monster.defend(player.attack())
                    print(f"{monster.name} has {monster.health}hp remaining")
                
                elif (hit + player.atk < monster.ac):
                    print("You missed!")

                # if mob dies, heals player by overkill amount
                if monster.health <= 0:
                    print(f"You beat the {monster.name}!")
                    overkill = 0 - monster.health
                    player.health += overkill
                    if overkill > 0:
                        print(f"You healed for {overkill}hp!\n")
                    input()
                    break
                
                # enemy attacks
                enemy_attack = random.randint(1, 20)
                if (enemy_attack + monster.atk >= player.ac):
                    print("\nEnemy hit!")
                    player.defend(monster.attack())
                    print(f"You have {player.health}hp remaining!")
                else:
                    print("Enemy missed!")
                
            case "run":
                os.system('cls')
                loss = random.randint(5, 15)
                print(f"You ran away! You dropped {loss} gold on the way out.                (bitch)\n")
                player.gold -= loss
                break
            
            case "item": 
                os.system('cls')
                player.inventory()
                use = input("What would you like to use?")
                while use != "scroll":
                    use = input("Please enter [scroll]")

                if use == "scroll":
                    player.scrolls -= 1
                    player.health += 25
                    print("25hp restored. HP remaining: ", player.health)



        if player.health <= 0:
            player.death()
            