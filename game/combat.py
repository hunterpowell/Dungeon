import random
from utils import clear_screen, press_enter
from characters.mob import Mob
from characters.boss import Boss
from lore import juicer_desc, hoarder_desc, ball_desc, demon_desc

def fight(player):
    
    rand = random.randint(1, 5)

    # 20% chance for boss, this chooses random boss and displays description, gives key if defeated
    if rand == 5:
        monster = Boss.random_boss()
        money = random.randint(100, 200)
        key = True
        match monster.name:
            case "THE JUICER":
                juicer_desc()
                press_enter()
                clear_screen()
            case "THE HOARDER":
                hoarder_desc()
                press_enter()
                clear_screen()
            case "BALL OF SWINE":
                ball_desc()
                press_enter()
                clear_screen()
            case "ASYLUM DEMON":
                demon_desc()
                press_enter()
                clear_screen()

    # 80% chance for random mob, no key!
    else:
        monster = Mob.random_enemy()
        money = random.randint(10, 30)
        key = False

    # this is here for XP purposes later
    max_hp = monster.health

    print("\t\t\tCOMBAT\n\t\t----------------------")
    print(f"You've run into a {monster.name}!")
    print(f"{monster.name} has {monster.health}hp")
    monster.display

    while (monster.health > 0) and (player.health > 0):
        userin = input("\nWhat would you like to do?\n"
                       "  1. Basic attack\n"
                       "  2. Special Attack\n"
                       "  3. Use healing scroll\n"
                       "  4. Run away\n"
                       "Enter here: ")

        while (userin != "1") and (userin != "2") and (userin != "3") and (userin != "4"):
            userin = input("Please enter a valid number: ")
        userin = int(userin)

        match userin:
            case 1:
                
                clear_screen()
                print("\t\t\tCOMBAT\n\t\t----------------------")
                # attack roll to determine hit/miss
                hit = random.randint(1, 20)
                if (hit + player.atk >= monster.ac):
                    # crit if nat 20
                    if (hit == 20):
                        damage = player.crit() + player.dmg
                        print(f"You crititcally hit for {damage} damage!")
                    else:
                        damage = player.weapon_atk() + player.dmg
                        print(f"You hit for {damage} damage!")                    
                    monster.defend(damage)
                    if monster.health > 0:
                        print(f"{monster.name} has {monster.health}hp remaining")
                    # prevents monster from displaying negative hp
                    else:
                        print(f"{monster.name} has 0hp remaining!")

                elif (hit + player.atk < monster.ac):
                    print("You missed!")
                    print(f"{monster.name} has {monster.health}hp remaining")

                # do stuff if monster dies, heal by overkill, get gold, add xp, check for level up
                if monster.health <= 0:
                    player.monster_death(monster, key, money, max_hp)
                    break
                
            case 2:
                clear_screen()
                print("\t\t\tCOMBAT\n\t\t----------------------")
                # ult
                if player.weapon_charge == True:
                    player.special_atk(monster)
                    player.weapon_charge = False
                else:
                    print("You wasted your turn dumbass! You don't have any weapon charges left.")
                    print(f"Enemy has {monster.health}hp remaining.")

                # do stuff if monster dies, heal by overkill, get gold, add xp, check for level up
                if monster.health <= 0:
                    player.monster_death(monster, key, money, max_hp)
                    break
                
            case 3: 
                clear_screen()
                print("\t\t\tCOMBAT\n\t\t----------------------")
                player.heal()

            case 4:
                clear_screen()
                loss = random.randint(25, 50)
                print(f"You ran away! You dropped {loss} gold on the way out.                (bitch)\n")
                player.gold -= loss
                press_enter()
                break

        # enemy attacks
        enemy_attack = random.randint(1, 20)
        if (enemy_attack + monster.atk >= player.ac):
            damage = monster.attack() + monster.dmg
            player.defend(damage)
            print(f"\nEnemy hit for {damage} damage!")
            print(f"You have {player.health}hp remaining!")
        else:
            print("\nEnemy missed!")
            print(f"You have {player.health}hp remaining!")


            