from utils import clear_screen, press_enter

def safe(player, day):

    # heals to 100hp if less than that, but doesn't erase overhealth
    if player.health < 100:
        player.health = 100
    player.weapon_charge = True
    max_heals = 5                   # limits amount of available scrolls per day

    while True:
        print("SAFE ROOM".center(90))
        print("------------------------------------------------------------------------------------------")
        print("Welcome to the safe room. You got a good night's sleep and your health has been restored.")
        if day == 4 and player.key > 0:
            tmp = input("\nFinal moments before descending the stairs to floor 2.\n\n"
                        "What Would you like to do?\n"
                        "  1. see stats\n"
                        "  2. check item shop\n"
                        "  3. see inventory\n"
                        "  4. leave the room, and descend the stairs\n"
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
                weapon2 = player.weapons()
                while True:
                    clear_screen()
                    print("ITEM SHOP".center(40))
                    print("----------------------------------------")
                    print("Current gold: ", player.gold)
                    shop = input("  1. Healing scrolls\n"
                                f"  2. {weapon1} - 500 gold\n"
                                f"  3. {weapon2} - 500 gold\n"
                                "  4. Leave shop\n"
                                "Enter here: "
                                )
                    
                    while shop != "1" and shop != "2" and shop != "3" and shop != "4":
                        shop = input("Enter a valid number: ")
                    shop = int(shop)
                    
                    match shop:
                        case 1:
                            player.buy_heals(max_heals)

                        case 2:
                            player.buy_weapon(weapon1)
                            player.equip_weapon(player.weapon_stats())
                        
                        case 3:
                            player.buy_weapon(weapon2)
                            player.equip_weapon(player.weapon_stats())

                        case 4:
                            clear_screen()
                            break

                    

            case 3:
                player.inventory()

            case 4:
                break
                
