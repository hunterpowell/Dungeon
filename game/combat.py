import random
from utils import clear_screen, press_enter
from characters.mob import Mob
from characters.boss import Boss
from lore import monster_lore

def fight(player):
    
    rand = random.randint(1, 5)

    # 20% chance for boss, this chooses random boss and displays description, gives key if defeated
    if rand == 5:
        if player.floor == 1 :
            monster = Boss.random_boss1()
            money = random.randint(100, 200)
        elif player.floor == 2:
            monster = Boss.random_boss2()
            money = random.randint(200, 300)
        key = True
        monster_lore(monster)

    # 80% chance for random mob, no key!
    else:
        if player.floor == 1:
            monster = Mob.random_enemy1()
            money = random.randint(10, 30)
        elif player.floor == 2:
            monster = Mob.random_enemy2()
            money = random.randint(20, 60)
        key = False

    # this is here for XP purposes later
    max_hp = monster.health

    print("COMBAT".center(40))
    print("----------------------".center(40))
    print(f"You've run into a {monster.name}!")
    print(f"{monster.name} has {monster.health}hp")
    print(f"You have {player.health}hp")
    monster.display

    while (monster.health > 0) and (player.health > 0):
        userin = input("\nWhat would you like to do?\n"
                       "  1. Basic attack\n"
                       "  2. Special Attack\n"
                       "  3. Use item\n"
                       "  4. Run away\n"
                       "Enter here: ")

        while (userin != "1") and (userin != "2") and (userin != "3") and (userin != "4"):
            userin = input("Please enter a valid number: ")
        userin = int(userin)

        match userin:
            # basic attack
            case 1:
                
                clear_screen()
                print("COMBAT".center(40))
                print("----------------------".center(40))
                # attack roll to determine hit/miss
                hit = random.randint(1, 20)
                if (hit + player.accuracy + player.finesse >= monster.ac):
                    # crit if nat 20
                    if (hit == 20):
                        damage = player.weapon_crit()
                    else:
                        damage = player.weapon_atk()
                    monster.defend(damage)

                elif (hit + player.accuracy < monster.ac):
                    print("You missed!")
                    print("")

                # do stuff if monster dies, heal by overkill, get gold, add xp, check for level up
                if monster.health <= 0:
                    player.monster_death(monster, key, money, max_hp)
                    break
                
                monster.is_poisoned(player)
                if monster.health <= 0:
                    player.monster_death(monster, key, money, max_hp)
                    break

            # special attack
            case 2:
                clear_screen()
                print("COMBAT".center(40))
                print("----------------------".center(40))
                # ult
                if player.weapon_charge >= 1:
                    player.special_atk(monster)
                    player.weapon_charge -= 1
                else:
                    print("You wasted your turn dumbass! You don't have any weapon charges left.")

                # do stuff if monster dies, heal by overkill, get gold, add xp, check for level up
                if monster.health <= 0:
                    player.monster_death(monster, key, money, max_hp)
                    break
                
                monster.is_poisoned(player)
                if monster.health <= 0:
                    player.monster_death(monster, key, money, max_hp)
                    break
                
            # use item    
            case 3: 
                clear_screen()
                print("COMBAT".center(40))
                print("----------------------".center(40))
                menu = input("What would you like to do?\n"
                      f"  1. Drink healing potion ({player.potions} remaining)\n"
                      f"  2. Throw rot pot ({player.rotpot} remaining)\n"
                      "Enter here: ")
                while menu != "1" and menu != "2":
                    menu = input("Please enter a valid number: ")

                if menu == "1":
                    clear_screen()
                    print("COMBAT".center(40))
                    print("----------------------".center(40))
                    player.heal()
                    monster.is_poisoned(player)
                    if monster.health <= 0:
                        player.monster_death(monster, key, money, max_hp)
                        break

                if menu == "2":
                    clear_screen()
                    print("COMBAT".center(40))
                    print("----------------------".center(40))
                    
                    if player.rotpot > 0:
                        monster.poisoned = True
                        print(f"{monster.name} has been poisoned!")
                    else:
                        print("You are out of rot pots! Way to waste your turn dumbass")

            # run
            case 4:
                clear_screen()
                loss = random.randint(25, 50)
                print(f"You ran away! You dropped {loss} gold on the way out.                (bitch)\n")
                player.gold -= loss
                press_enter()
                break

        # enemy attacks
        enemy_attack = random.randint(1, 20)
        if (enemy_attack + monster.accuracy >= player.ac):
            damage = monster.attack() - player.resolve
            print(f"Enemy hit you for {damage} damage!")
            player.defend(damage)
        else:
            print("Enemy missed!")

        print("-" * 40)
        print(f"{player.name} health - {player.health}/{player.max_hp}".center(40))
        if monster.health >= 0:
            print(f"{monster.name} health - {monster.health}/{max_hp}".center(40))
        else:
            print(f"{monster.name} health - 0".center(40))
        print("-" * 40)

