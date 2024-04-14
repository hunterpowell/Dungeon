import random
from utils import press_enter, clear_screen
from combat import fight
from lore import fist_desc, shotgun_desc, gauntlet_desc, chime_desc, scythe_desc


def explore(player):
    
    num = random.randint(0,3)

    #MAKE THIS 2 AGAIN TO FIX
    if (num <= 0):
        fight(player)
    
    else:
        
        num2 = random.randint(0, 4)
        weapon = player.weapons()

        while num2 == 4:
            pickup = input(f"You found a {weapon}!\n"
                   "Equipping will remove any other weapon you have.\n"
                   "What would you like to do??\n"
                   "  1. Equip weapon (this will discard current weapon)\n"
                   "  2. See weapon description\n"
                   "  3. Discard weapon\n"
                   "Enter here: "
                )
            while pickup.isdigit() == False:
                pickup = input("Please enter a number: ")
            
            while pickup != "1" and pickup != "2" and pickup != "3":
                pickup = input("Please enter a valid number: ")
            
            pickup = int(pickup)
            match pickup:
                case 1:
                    print(f"\n{weapon} equipped!")
                    player.weapon = weapon
                    break
                
                case 2:
                    clear_screen()
                    match weapon:
                        case "Fists":
                            fist_desc()
                        case "Sentient Shotgun":
                            shotgun_desc()
                        case "War Gauntlet":
                            gauntlet_desc()
                        case "Cleric's Chime":
                            chime_desc()
                        case "Lifehunt Scythe":
                            scythe_desc()
                    press_enter()
                    clear_screen()

                case 3:
                    print(f"\n{weapon} discarded. I sure hope you don't regret that in the near future!\n")
                    break

        else:
            print("You found some loot!")
            money = random.randint(20,50)
            player.gold += money
            print(f"{money} gold acquired!")
  
        press_enter()
