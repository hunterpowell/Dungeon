import tkinter as tk
from tkinter import font

from characters.player import Player
from lore import introduction, combat_rules
from game_loop import main_loop


class DungeonGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("World Dungeon")
        self.root.geometry("600x800")
        
        # main frame
        self.main_frame = tk.Frame(root, bg = "black")
        self.main_frame.pack(fill="both", expand=True)

        self.text_display = tk.Text(self.main_frame, bg = "black", fg = "white",
                                    font = ("Courier", 12), wrap = tk.WORD)
        self.text_display.pack(fill="both", expand = True, padx = 20, pady = 20)
        self.text_display.config(state=tk.DISABLED)

        self.button_frame = tk.Frame(self.main_frame, bg = "black")
        self.button_frame.pack(fill = "x", padx = 20, pady = 20)

        self.show_introduction()

    def clear_screen(self):
        # clears text
        self.text_display.config(state = tk.NORMAL)
        self.text_display.delete(1.0, tk.END)
        self.text_display.config(state = tk.DISABLED)

        # remove all buttons
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def add_text(self, text):
        self.text_display.config(state = tk.NORMAL)
        self.text_display.insert(tk.END, text)
        self.text_display.config(state = tk.DISABLED)
        self.text_display.see(tk.END)

    def add_button(self, text, command):
        button = tk.Button(self.button_frame, text = text, command = command,
                           bg = "dark gray", fg = "black", width = 20)
        button.pack(side = tk.LEFT, padx = 5, pady = 5)
        return button

    def show_introduction(self):
        self.clear_screen

        intro_art = """
        ===============================
        |       WORLD DUNGEON        |
        ===============================
        """
        self.add_text(intro_art + "\n\n")
        self.add_text("You have awoken at the bottom of the stairs in a bizarre place.\n")
        self.add_text("Do you want to hear some lore or do you want to go in blind?\n")

        self.add_button("Hear Lore", self.show_lore)
        self.add_button("Go in Blind", self.ask_name)

    def show_lore(self):
        self.clear_screen()
        lore_text = ("You are on the first level of the World Dungeon. Everyone on the surface of your planet is either dead, or down here with you. "
            "You woke up at the bottom of the stairs, in a dark hallway with nothing but the clothes on your back and whatever is in your pockets. "
            "You have 5 days before this floor collapses, going to a safe room will end the day.\n")
        self.add_text(lore_text)
        self.add_button("Continue", self.ask_name)

    def ask_name(self):
        self.clear_screen()
        self.add_text("What is your name?\n\n")

        name_var = tk.StringVar()
        name_entry = tk.Entry(self.button_frame, textvariable = name_var, width = 40)
        name_entry.pack(side = tk.LEFT, padx = 5, pady = 5)

        submit_btn = tk.Button(self.button_frame, text = "Submit", 
                               command = lambda: self.start_game(name_var.get()),
                               bg = "dark gray", fg = "black", width = 10)
        submit_btn.pack(side = tk.LEFT, padx = 5, pady = 5)

    def start_game(self, player_name):
        self.player = Player(player_name)
        self.show_combat_rules()

    def show_combat_rules(self):
        self.clear_screen()
        self.add_text("TEEEEEEEEEEST")
        pass

if __name__ == "__main__":
    root = tk.Tk()
    game = DungeonGUI(root)
    root.mainloop()