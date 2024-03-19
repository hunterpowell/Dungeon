
def introduction():
    print_intro = input("\n\nYou have awoken at the bottom of the stairs in a bizarre place. \
Do you want to hear some lore or do you want to go in blind? [lore] or [blind]: ")
    
    while (print_intro != "lore") & (print_intro != "blind"):
        print_intro = input("Please enter [lore] or [blind]: ")
    
    if (print_intro == "lore"):
        print("\nYou are on the first level of the World Dungeon. Everyone on the surface of your planet is either dead, or down here with you.\n\
You woke up at the bottom of the stairs, in a dark hallway with nothing but the clothes on your back and whatever is in your pockets.\n")
        
    name = input("What is your name? ")
    return name
# introduction()