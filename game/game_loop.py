from game.safe_room import safe
from game.combat import explore

def main_loop(player):
    where = input("\nDo you want to [explore], or look for a [safe] room?: " )
    while (where != "explore") & (where != "safe"):
        where = input("Enter [explore] or [safe]: ")

    

    if (where == "safe"):
        safe(player)
    if (where == "explore"):
        explore(player)