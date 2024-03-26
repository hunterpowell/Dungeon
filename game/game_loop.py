from game.safe_room import safe
from game.explore import explore

def main_loop(player):
    
    day = 0

    while day < 5:    
        
        print(f"\n\tDay {day + 1}\n---------------------")
        where = input("\nDo you want to [explore], or end the day and look for a [safe] room?: " )
        while (where != "explore") & (where != "safe"):
            where = input("Enter [explore] or [safe]: ")

        if (where == "safe"):
            safe(player)
            day += 1
        if (where == "explore"):
            explore(player)
