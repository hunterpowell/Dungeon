import tkinter as tk
from dungeon_gui import DungeonGUI
from game_loop import GameLoop

if __name__ == "__main__":
    root = tk.Tk()
    game = GameLoop(root)
    root.mainloop()