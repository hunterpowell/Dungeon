import os
from game.safe_room import safe
from game.explore import explore

def main_loop(player):
    
    day = 0

    while day < 5:    
        
        os.system('cls')
        print(f"\t\t\tDay: {day + 1}\n\t\t----------------------")
        where = input("Do you want to [explore], or end the day and look for a [safe] room?: " )
        while (where != "explore") and (where != "safe"):
            where = input("Enter [explore] or [safe]: ")

        if (where == "safe"):
            os.system('cls')
            safe(player, day)
            day += 1
        if (where == "explore"):
            os.system('cls')
            explore(player)

