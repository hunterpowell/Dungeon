from game.safe_room import safe
# from game.combat import fight

def main_loop(player):
    where = input("\nDo you want to look for a [fight], or a [safe] room?: " )
    while (where != "fight") & (where != "safe"):
        where = input("Enter [fight] or [safe]: ")

    if (where == "safe"):
        safe(player)
    # if (where == "fight"):
    #     fight(player)