import os
from game.characters.player import Player
from game.lore import introduction, combat_rules
from game.game_loop import main_loop

if __name__ == "__main__":

    os.system('cls')
    p1 = Player(introduction())
    combat_rules()
    main_loop(p1)
