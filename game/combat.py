import random
import os
from game.characters.mob import Mob
from game.characters.boss import Boss
from game.lore import juicer_desc, hoarder_desc, ball_desc, demon_desc

def fight(player):
    
    rand = random.randint(1, 10)

    if rand == 10:
        monster = Boss.random_boss()
        money = random.randint(100, 200)
        match monster.name:
            case "THE JUICER":
                juicer_desc()
                input("Press enter to continue.")
                os.system('cls')
            case "THE HOARDER":
                hoarder_desc()
                input("Press enter to continue.")
                os.system('cls')
            case "BALL OF SWINE":
                ball_desc()
                input("Press enter to continue.")
                os.system('cls')
            case "ASYLUM DEMON":
                demon_desc()
                input("Press enter to continue.")
                os.system('cls')
            
    else:
        monster = Mob.random_enemy()
        money = random.randint(10, 30)

    max_hp = monster.health                                     # this is here for XP purposes later

    print("\t\t\tCOMBAT\n\t\t----------------------")
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
                
                print("\t\t\tCOMBAT\n\t\t----------------------")
                # attack roll to determine hit/miss
                hit = random.randint(1, 20)
                if (hit + player.atk >= monster.ac):
                    print("You hit!")                    
                    monster.defend(player.attack())
                    if monster.health > 0:
                        print(f"{monster.name} has {monster.health}hp remaining")
                    else:
                        print(f"{monster.name} has 0hp remaining!")

                elif (hit + player.atk < monster.ac):
                    print("You missed!")
                    print(f"{monster.name} has {monster.health}hp remaining")

                # do stuff if monster dies, heal by overkill, get gold, add xp, check for level up
                if monster.health <= 0:
                    print(f"\nYou beat the {monster.name}!\n")
                    overkill = 0 - monster.health
                    player.health += overkill
                    if overkill > 0:
                        print(f"You healed for {overkill}hp!")
                    player.xp += max_hp
                    print(f"You picked up {money} off the corpse!")
                    player.gold += money
                    print(f"You have earned {max_hp}xp!")
                    player.level_up()
                    print(f"Player level: {player.lvl}")
                    
                    # requires input before we break out of loop and screen clears
                    input("\nPress enter to continue.")
                    break
                
                # enemy attacks
                enemy_attack = random.randint(1, 20)
                if (enemy_attack + monster.atk >= player.ac):
                    print("\nEnemy hit!")
                    player.defend(monster.attack())
                    print(f"You have {player.health}hp remaining!")
                else:
                    print("\nEnemy missed!")
                    print(f"You have {player.health}hp remaining!")
                
            case "run":
                os.system('cls')
                loss = random.randint(5, 15)
                print(f"You ran away! You dropped {loss} gold on the way out.                (bitch)\n")
                player.gold -= loss
                input("Press enter to continue.")
                break
            
            case "item": 
                os.system('cls')
                player.usable_items()
                use = input("What would you like to use?: ")
                while use != "scroll":
                    use = input("Please enter [scroll]")

                if use == "scroll" and player.scrolls > 0:
                    player.scrolls -= 1
                    player.health += 25
                    print("25hp restored. HP remaining: ", player.health)
                else:
                    print("You are out of healing scrolls")

        if player.health <= 0:
            player.death()
            