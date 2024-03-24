from game.characters.player import Player
from game.intro import introduction
from game.game_loop import main_loop

if __name__ == "__main__":


    p1 = Player(introduction())
    print("hi ", p1.name)
    main_loop(p1)

