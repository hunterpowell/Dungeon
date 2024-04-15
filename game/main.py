from characters.player import Player
from utils import clear_screen
from lore import introduction, combat_rules
from game_loop import main_loop

if __name__ == "__main__":

    p1 = Player(introduction())
    combat_rules()
    main_loop(p1)

