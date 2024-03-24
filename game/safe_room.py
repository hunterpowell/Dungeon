def safe(player):


    print("Welcome to the safe room. Your health has been restored.\n")

    tmp = input("What would you like to do?\n"
                "see [stats]\n"
                "buy [heal] scrolls\n"
                "Enter here: ")
    
    if (tmp != "stats") & (tmp != "heal"):
        tmp = input("Please enter something valid: ")


    match tmp:
        case "stats":
            player.display_player()
        case "heal":
            player.scrolls = input("How many heal scrolls do you want? ")

            
