def safe(player):


    print("Welcome to the safe room. Your health has been restored.\n")

    tmp = input("What would you like to do?\n"
                "see [stats]\n"
                "buy [heal] scrolls\n"
                "Enter here: ")
    
    if (tmp != "stats") & (tmp != "heal"):
        tmp = input("Please enter something valid: ")
    
    if (tmp == "stats"):
        player.display()


    match tmp:
        case "stats":
            player.display()
        case "heal":
            player.scrolls = input("How many heal scrolls do you want? ")

            
