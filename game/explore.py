import random
from utils import press_enter
from combat import fight
from lore import weapon_lore


def explore(player):
    
    num = random.randint(0,3)

    if (num <= 2):
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
            
            while pickup != "1" and pickup != "2" and pickup != "3":
                pickup = input("Please enter a valid number: ")
            
            pickup = int(pickup)
            match pickup:
                # equips new weapon and resets special attack
                case 1:
                    print(f"\n{weapon} equipped!")
                    player.unequip_weapon(player.weapon_stats()[0], player.weapon_stats()[1], player.weapon_stats()[2], player.weapon_stats()[3], player.weapon_stats()[4])
                    player.weapon = weapon
                    player.equip_weapon(player.weapon_stats()[0], player.weapon_stats()[1], player.weapon_stats()[2], player.weapon_stats()[3], player.weapon_stats()[4])
                    if player.weapon_charges == 0:
                        player.weapon_charges = player.max_charges
                    break
                
                case 2:
                    weapon_lore(weapon)

                case 3:
                    print(f"\n{weapon} discarded. I sure hope you don't regret that in the near future!")
                    break

        if num2 == 3: 
            print("You found a healing potion!")
            player.potions += 1
            print(f"You now have {player.potions} potions.")

        if num2 == 0 or num2 == 1 or num2 == 2:
            print("You found some loot!")
            money = random.randint(20,50)
            player.gold += money
            print(f"{money} gold acquired!")
  
        press_enter()
