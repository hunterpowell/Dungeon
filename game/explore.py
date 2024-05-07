import random
from utils import press_enter, clear_screen
from combat import fight
from lore import weapon_lore, ring_desc, armor_desc


def explore(player):
    
    num = random.randint(0,3)

    if (num <= 2):
        fight(player)
    
    else:
        
        num2 = random.randint(0, 5)
        weapon = player.weapons()
        ring = player.rings()
        armor = player.armors()

        while num2 == 4 and player.floor == 1:
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

        while num2 == 4 and player.floor == 2:
            pickup = input(f"You found {armor}!\n"
                   "What would you like to do??\n"
                   "  1. Equip armor (this will discard current armor)\n"
                   "  2. See armor description\n"
                   "  3. Discard armor\n"
                   "Enter here: "
                )
            
            while pickup != "1" and pickup != "2" and pickup != "3":
                pickup = input("Please enter a valid number: ")
            
            pickup = int(pickup)
            match pickup:
                # equips new weapon and resets special attack
                case 1:
                    print(f"\n{armor} equipped!")
                    player.unequip_amor(player.armor)
                    player.armor = armor
                    player.equip_armor(armor)
                    break
                
                case 2:
                    armor_desc()

                case 3:
                    print(f"\n{armor} discarded. I sure hope you don't regret that in the near future!")
                    break


        if num2 == 3: 
            print("You found a healing potion!")
            player.potions += 1
            print(f"You now have {player.potions} potions.")

        while num2 == 5:
            pickup = input(f"You found a {ring}!\n"
                "What would you like to do??\n"
                "  1. Equip ring\n"
                "  2. See ring description\n"
                "  3. Discard ring\n"
                "Enter here: "
            )
            
            while pickup != "1" and pickup != "2" and pickup != "3":
                pickup = input("Please enter a valid number: ")
            
            pickup = int(pickup)
            
            match pickup:
                case 1:
                    if player.ring1 != "None" and player.ring2 != "None":
                        clear_screen()
                        print("Both of your ring slots are full. Which ring would you like to replace?")
                        print(f"  1. {player.ring1}")
                        print(f"  2. {player.ring2}")
                        print("  3. Discard ring")
                        which = input("Enter here: ")
                        while which != "1" and which != "2" and which != "3":
                            which = input("Please enter a valid number: ")

                        if which == "1":
                            player.unequip_ring(player.ring1)
                            player.ring1 = "None"
                        elif which == "2":
                            player.unequip_ring(player.ring2)
                            player.ring2 = "None"
                        else:
                            print(f"\n{ring} discarded. I sure hope you don't regret that in the near future!")
                            break
                    
                    if player.ring1 == "None":    
                        player.ring1 = ring
                        player.equip_ring(ring)
                    elif player.ring2 == "None":
                        player.ring2 = ring
                        player.equip_ring(ring)

                    print(f"{ring} equipped!")
                    break

                case 2:
                    ring_desc(ring)

                case 3:
                    print(f"\n{ring} discarded. I sure hope you don't regret that in the near future!")
                    break
            

        if num2 == 0 or num2 == 1 or num2 == 2:
            print("You found some loot!")
            money = random.randint(20,50)
            player.gold += money
            print(f"{money} gold acquired!")
  
        press_enter()
