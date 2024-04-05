def safe(player, day):

    print("\n-----------------------------------------------------------------------------------------")
    print("Welcome to the safe room. You got a good night's sleep and your health has been restored.")
    player.health = 100

    while True:
        if day == 5:
            tmp = input("\nFinal moment before descending the stairs to floor 2\n"
                        "What Would you like to do?\n"
                        "see [stats]\n"
                        "buy [heal] scrolls\n"
                        "see [inventory]\n"
                        "[leave] the room, and descend the stairs\n"
                        "Enter here: ")
        else:
            tmp = input("\nWhat would you like to do?\n"
                        "see [stats]\n"
                        "buy [heal] scrolls\n"
                        "see [inventory]\n"
                        "[leave] the room\n"
                        "Enter here: ")
            
        if (tmp != "stats") and (tmp != "heal") and (tmp != "leave") and (tmp != "inventory"):
            tmp = input("Please enter something valid: ")

        match tmp:
            case "stats":
                player.display()

            case "heal":
                heal = input("\nHow many heal scrolls do you want? 20 gold each: ")
                # FIX THIS, input sanitization isn't working right
                while not heal.isdigit():
                    heal = input("please enter a number: ")
                    heal_num = int(heal)
                while (player.gold < (heal_num*20)):
                    heal = input("You can't afford that many. Try again: ")
                    heal_num = int(heal)
                else:
                    player.gold -= (heal_num*20)
                    player.scrolls += heal_num
                    print(f"You now have {player.scrolls} scrolls")

            case "inventory":
                player.inventory()

            case "leave":
                break
                
