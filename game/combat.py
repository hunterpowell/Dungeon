import random
import os
from game.characters.mob import Mob
from game.characters.boss import Boss
from game.lore import juicer_desc, hoarder_desc, ball_desc, demon_desc

def fight(player):
    
    rand = random.randint(1, 5)

    if rand == 5:
        monster = Boss.random_boss()
        money = random.randint(100, 200)
        key = True
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
        key = False

    max_hp = monster.health                                     # this is here for XP purposes later

    print("\t\t\tCOMBAT\n\t\t----------------------")
    print(f"You've run into a {monster.name}!")
    print(f"{monster.name} has {monster.health}hp")
    monster.display

    while (monster.health > 0) and (player.health > 0):
        userin = input("\nWhat would you like to do?\n"
                       "1. Basic attack\n"
                       "2. Special Attack\n"
                       "3. Use item\n"
                       "4. Run away\n"
                       "Enter here: ")

        while (userin != "1") and (userin != "2") and (userin != "3") and (userin != "4"):
            userin = input("Please enter a valid number: ")
        userin = int(userin)

        match userin:
            case 1:
                
                os.system('cls')
                print("\t\t\tCOMBAT\n\t\t----------------------")
                # attack roll to determine hit/miss
                hit = random.randint(1, 20)
                if (hit + player.atk >= monster.ac):
                    damage = player.attack()
                    monster.defend(damage)
                    print(f"You hit for {damage} damage!")                    
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
                    player.health += int(overkill/2)
                    if overkill > 0:
                        print(f"You healed for {(int(overkill/2))}hp!")
                    player.xp += max_hp
                    print(f"You picked up {money} gold off the corpse!")
                    player.gold += money
                    print(f"You have earned {max_hp}xp!")
                    player.level_up()
                    if key == True and player.key == False:
                        print("You found a key! You can now descend the stairs when the floor ends.")
                        player.key = key
                    
                    # requires input before we break out of loop and screen clears
                    input("\nPress enter to continue.")
                    break
                
                # enemy attacks
                enemy_attack = random.randint(1, 20)
                if (enemy_attack + monster.atk >= player.ac):
                    damage = monster.attack()
                    player.defend(damage)
                    print(f"\nEnemy hit for {damage} damage!")
                    print(f"You have {player.health}hp remaining!")
                else:
                    print("\nEnemy missed!")
                    print(f"You have {player.health}hp remaining!")

            case 2:
                os.system('cls')
                print("\t\t\tCOMBAT\n\t\t----------------------")
                # ult
                if player.weapon_charge == True:
                    player.special_atk(monster)
                    player.weapon_charge = False
                else:
                    print("You wasted you turn dumbass! You don't have any weapon charges left.")
                    print(f"Enemy has {monster.health}hp remaining.")

                # enemy claps back
                enemy_attack = random.randint(1, 20)
                if (enemy_attack + monster.atk >= player.ac):
                    damage = monster.attack()
                    player.defend(damage)
                    print(f"\nEnemy hit for {damage} damage!")
                    print(f"You have {player.health}hp remaining!")
                else:
                    print("\nEnemy missed!")
                    print(f"You have {player.health}hp remaining!")
                

            case 3: 
                while True:
                    os.system('cls')
                    player.usable_items()
                    use = input("\nWhat would you like to do\n"
                                "1. Use healing scroll\n"
                                "2. PLACEHOLDER\n"
                                "3. Go back to combat\n"
                                "Enter here: "
                                )
                    while use != "1" and use != "2" and use != "3":
                        use = input("Please enter a valid number: ")
                    use = int(use)

                    match use:
                        case 1:
                            player.heal()
                            
                            #enemy attacks despite player healing (asshole)
                            enemy_attack = random.randint(1, 20)
                            if (enemy_attack + monster.atk >= player.ac):
                                damage = monster.attack()
                                player.defend(damage)
                                print(f"\nEnemy hit for {damage} damage!")
                                print(f"You have {player.health}hp remaining!")
                            else:
                                print("\nEnemy missed!")
                                print(f"You have {player.health}hp remaining!")
                                input()
                        
                        # case 2:
                        case 3:
                            break


            case 4:
                os.system('cls')
                loss = random.randint(5, 15)
                print(f"You ran away! You dropped {loss} gold on the way out.                (bitch)\n")
                player.gold -= loss
                input("Press enter to continue.")
                break


    if player.health <= 0:
        player.death()
            