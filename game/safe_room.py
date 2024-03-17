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

    
    # TODO make this work, the dictionary doesn't seem to be doing much
    # cases = {0 : "stats",
    #          1 : "heal"
    #          }
    
    # match tmp:
    #     case 0:
    #         player.display()
    #     case 1:
    #         scrolls = input("How many heal scrolls do you want? ")
