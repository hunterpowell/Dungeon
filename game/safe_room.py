import os

def safe(player, day):

    print("-----------------------------------------------------------------------------------------")
    print("Welcome to the safe room. You got a good night's sleep and your health has been restored.")
    player.health = 100
    player.weapon_charge = True

    while True:
        if day == 4 and player.key > 0:
            tmp = input("\nFinal moments before descending the stairs to floor 2.\n\n"
                        "What Would you like to do?\n"
                        "see [stats]\n"
                        "buy [heal] scrolls\n"
                        "see [inventory]\n"
                        "[leave] the room, and descend the stairs\n"
                        "Enter here: ")
        elif day == 4 and player.key == 0:
            print("You didn't find a key in time. The stairway remains locked to you, and the floor is about to collapse. Goodbye!")
            player.death()
        else:
            tmp = input("\nWhat would you like to do?\n"
                        "see [stats]\n"
                        "buy [heal] scrolls\n"
                        "see [inventory]\n"
                        "[leave] the room\n"
                        "Enter here: ")
            
        if (tmp != "stats") and (tmp != "heal") and (tmp != "leave") and (tmp != "inventory"):
            tmp = input("Please enter something valid: ")

        os.system('cls')

        match tmp:
            case "stats":
                player.display_player()

            case "heal":
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

            case "inventory":
                player.inventory()

            case "leave":
                break
                
