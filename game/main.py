from characters.player import Player
from lore import introduction, combat_rules
from game_loop import main_loop

if __name__ == "__main__":

    player = Player(introduction())
    combat_rules()
    main_loop(player)
