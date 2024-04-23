from utils import clear_screen, press_enter

def safe(player, day):

    # heals to 100hp if less than that, but doesn't erase overhealth
    if player.health < player.max_hp:
        player.health = player.max_hp
    player.weapon_charge = player.max_charges
    max_heals = 5                   # limits amount of available potions per day
    max_pots = 2

    while True:
        print("SAFE ROOM".center(90))
        print("-" * 90)
        print("Welcome to the safe room. You got a good night's sleep and your health has been restored.")
        if day == 4 and player.key > 0:
            tmp = input("\nFinal moments before descending the stairs to floor 2.\n\n"
                        "What Would you like to do?\n"
                        "  1. See stats\n"
                        "  2. Check item shop\n"
                        "  3. See inventory\n"
                        "  4. Leave the room, and descend the stairs\n"
                        "Enter here: ")
            
        elif day == 4 and player.key == 0:
            clear_screen()
            print("You didn't find a key in time. The stairway remains locked to you, and the floor is about to collapse around you. Goodbye!")
            player.health = 0
            break

        else:
            tmp = input("\nWhat would you like to do?\n"
                        "  1. See stats\n"
                        "  2. Check item shop\n"
                        "  3. See inventory\n"
                        "  4. Leave the room\n"
                        "Enter here: ")
            
        if (tmp != "1") and (tmp != "2") and (tmp != "3") and (tmp != "4"):
            tmp = input("Please a valid number: ")
        tmp = int(tmp)

        clear_screen()

        match tmp:
            # see stats
            case 1:
                player.display_player()

            # item shop
            case 2:
                weapon1 = player.weapons()
                ring = player.rings()
                ring2 = player.rings()
                while True:
                    clear_screen()
                    print("ITEM SHOP".center(40))
                    print("----------------------------------------")
                    print("Current gold: ", player.gold)
                    shop = input("  1. Healing potions - 50 gold\n"
                                "  2. Rot Pot - 100\n"
                                f"  3. {weapon1} - 500 gold\n"
                                f"  4. {ring} - 200 gold\n"
                                f"  5. {ring2} - 200 gold\n"
                                "  6. Leave shop\n"
                                "Enter here: "
                                )
                    
                    while shop != "1" and shop != "2" and shop != "3" and shop != "4" and shop != "5" and shop != "6":
                        shop = input("Enter a valid number: ")
                    shop = int(shop)
                    
                    match shop:
                        case 1:
                            max_heals = player.buy_heals(max_heals)

                        case 2: 
                            max_pots = player.buy_pot(max_pots)
                        
                        case 3:
                            player.buy_weapon(weapon1)
                        
                        case 4:
                            player.buy_ring(ring)
                            if player.health < player.max_hp:
                                player.health = player.max_hp
                        
                        case 5:
                            player.buy_ring(ring2)
                            if player.health < player.max_hp:
                                player.health = player.max_hp

                        case 6:
                            clear_screen()
                            break

            case 3:
                player.inventory()

            case 4:
                break
                
