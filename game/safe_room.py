def safe(player, day):

    print("Welcome to the safe room. You got a good night's sleep and your health has been restored.\n")

    while True:
        if day == 5:
            tmp = input("Final moment before descending the stairs to floor 2\n"
                        "What Would you like to do?\n"
                        "see [stats]\n"
                        "buy [heal] scrolls\n"
                        "[leave] the room, and descend\n"
                        "Enter here: ")
        else:
            tmp = input("What would you like to do?\n"
                        "see [stats]\n"
                        "buy [heal] scrolls\n"
                        "[leave] the room\n"
                        "Enter here: ")
            
        if (tmp != "stats") & (tmp != "heal") & (tmp != "leave"):
            tmp = input("Please enter something valid: ")

        match tmp:
            case "stats":
                player.display_player()
            case "heal":
                heal = input("How many heal scrolls do you want? ")
                while not heal.isdigit():
                    heal = input("please enter a number: ")
                player.scrolls += int(heal)
            case "leave":
                break
                
