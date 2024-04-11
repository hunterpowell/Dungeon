from game.characters.player import Player
from game.utils import clear_screen
from game.lore import introduction, combat_rules
from game.game_loop import main_loop

if __name__ == "__main__":

    clear_screen()
    p1 = Player(introduction())
    combat_rules()
    main_loop(p1)
