from game.safe_room import safe
from game.explore import explore

def main_loop(player):
    
    day = 0

    while day < 5:    
        
        print(f"\n\t\t\tDay: {day + 1}\n\t\t----------------------")
        where = input("Do you want to [explore], or end the day and look for a [safe] room?: " )
        while (where != "explore") & (where != "safe"):
            where = input("Enter [explore] or [safe]: ")

        if (where == "safe"):
            safe(player, day)
            day += 1
        if (where == "explore"):
            explore(player)
