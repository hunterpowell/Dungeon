from game.safe_room import safe
from game.explore import explore

def main_loop(player):
    
    while (player.health > 0):    
        
        where = input("\nDo you want to [explore], or look for a [safe] room?: " )
        while (where != "explore") & (where != "safe"):
            where = input("Enter [explore] or [safe]: ")

        
        if (where == "safe"):
            safe(player)
        if (where == "explore"):
            explore(player)