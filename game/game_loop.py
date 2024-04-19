from characters.player import Player
from utils import clear_screen, press_enter
from safe_room import safe
from explore import explore

def main_loop(player):
    
    while True:
        # psuedo-godmode if player name is Admin
        if player.name == "Admin":
            player.health = 99999
            player.gold = 99999
        day = 0
        while day < 5 and player.health > 0:    
            
            clear_screen()
            print(f"\t\t\tDay: {day + 1}\n\t\t----------------------")
            where = input("What would you like to do?\n"
                        "  1. Explore\n"
                        "  2. Use healing scroll\n"
                        "  3. Show stats\n"
                        "  4. Check inventory\n"
                        "  5. End the day and go to a safe room\n"
                        "Enter here: ")
            while (where != "1") and (where != "2") and (where != "3") and (where != "4") and (where != "5"):
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

                case 4:
                    clear_screen()
                    player.inventory()

                # safe room
                case 5:
                    clear_screen()
                    safe(player, day)
                    day += 1
        
        else: 
            if player.health > 0:
                print("You've descended the stairs! Congrats!                           (still a bitch tho)")
                player.display_player()
            else:
                player.death()

            #TODO fix this bestie
            tmp = input("Would you like to play again? [y] or [n]: ")
            if tmp == "y":
                player = Player(player.name)
            else: 
                exit()
        
