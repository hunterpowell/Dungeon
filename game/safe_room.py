def safe(player):

    print("Welcome to the safe room. You got a good night's sleep and your health has been restored.\n")

    while True:
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
                heal = input(int("How many heal scrolls do you want? "))
                while not heal.isdigit():
                    heal = input(int("please enter a number: "))
                player.scrolls += heal
            case "leave":
                break
                
