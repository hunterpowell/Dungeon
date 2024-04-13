from utils import clear_screen, press_enter

def safe(player, day):

    player.health = 100
    player.weapon_charge = True

    while True:
        print("SAFE ROOM".center(90))
        print("------------------------------------------------------------------------------------------")
        print("Welcome to the safe room. You got a good night's sleep and your health has been restored.")
        if day == 4 and player.key > 0:
            tmp = input("\nFinal moments before descending the stairs to floor 2.\n\n"
                        "What Would you like to do?\n"
                        "  1. see stats\n"
                        "  2. buy heal scrolls\n"
                        "  3. see inventory\n"
                        "  4. leave the room, and descend the stairs\n"
                        "Enter here: ")
            
        elif day == 4 and player.key == 0:
            print("You didn't find a key in time. The stairway remains locked to you, and the floor is about to collapse around you. Goodbye!")
            player.death()

        else:
            tmp = input("\nWhat would you like to do?\n"
                        "  1. see stats\n"
                        "  2. buy heal scrolls\n"
                        "  3. see inventory\n"
                        "  4. leave the room\n"
                        "Enter here: ")
            
        if (tmp != "1") and (tmp != "2") and (tmp != "3") and (tmp != "4"):
            tmp = input("Please a valid number: ")
        tmp = int(tmp)

        clear_screen()

        match tmp:
            case 1:
                player.display_player()

            case 2:
                print(f"Current gold: {player.gold}")
                heal = input("\nHow many heal scrolls do you want? 75 gold each: ")
                heal_num = int(heal)
                while (player.gold < (heal_num*75)):
                    heal = input("You can't afford that many. Try again: ")
                    heal_num = int(heal)
                else:
                    player.gold -= (heal_num*75)
                    player.scrolls += heal_num
                    print(f"You now have {player.scrolls} scrolls")
                press_enter()
                clear_screen()

            case 3:
                player.inventory()

            case 4:
                break
                
