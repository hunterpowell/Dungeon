from game.utils import clear_screen, press_enter
from game.safe_room import safe
from game.explore import explore

def main_loop(player):
    
    day = 0

    while day < 5:    
        
        clear_screen()
        print(f"\t\t\tDay: {day + 1}\n\t\t----------------------")
        where = input("What would you like to do?\n"
                      "1. Explore\n"
                      "2. Use healing scroll\n"
                      "3. Show stats\n"
                      "4. End the day and go to a safe room\n"
                      "Enter here: ")
        while (where != "1") and (where != "2") and (where != "3") and (where != "4"):
            where = input("Enter a valid number: ")
        where = int(where)

        match where:
            # explore
            case 1:
                clear_screen()
                explore(player)
            
            # heal
            case 2:
                clear_screen()
                player.heal()
                press_enter()

            # stats
            case 3:
                clear_screen()
                player.display_player()

            # safe room
            case 4:
                clear_screen()
                safe(player, day)
                day += 1
    else: 
        print("You've descended the stairs! Congrats!                           (still a bitch tho)")
    
