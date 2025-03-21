from characters.player import Player
from utils import clear_screen, press_enter
from safe_room import safe
from explore import explore
from lore import intro2, intro3
import tkinter as tk


class GameLoop:
    def __init__(self, root):
        self.root = root
        self.root.title("World Dungeon")

        self.player = None
        self.day = 1
        self.final_day = 5

        self.setup_ui()

        self.show_intro()

    def setup_ui(self):
        self.main_frame = tk.Frame(self.root, bg = "black")
        self.main_frame.pack(fill = "both", expand = True)

        # game info area
        self.info_frame = tk.Frame(self.main_frame, bg = "black")
        self.info_frame.pack(fill = "x", padx = 10, pady = 5)

        # day info
        self.day_label = tk.Label(self.info_frame, text = "Day: 1", fg = "white", bg = "black", font = ("Courier", 12))
        self.day_label.pack(side = tk.LEFT)

        # health info
        self.health_label = tk.Label(self.info_frame, text = "Health: 100", fg = "white", bg = "black", font = ("Courier", 12))
        self.health_label.pack(side = tk.RIGHT)

        # text area
        self.text_area = tk.Text(self.main_frame, bg = "black", fg = "white", font = ("Courier", 12), wrap = tk.WORD)
        self.text_area.pack(fill = "both", expand = True, padx = 10, pady = 5)
        self.text_area.config(state = tk.DISABLED)

        # button area
        self.button_frame = tk.Frame(self.main_frame, bg="black")
        self.button_frame.pack(fill="x", padx=10, pady=10)
    
    def clear_buttons(self):
        for widget in self.button_frame.winfo_children():
            widget.destroy()

    def update_day(self):
        self.day_label.config(text = f"Day: {self.day}")

    def update_health(self):
        self.health_label.config(text = f"Health: {self.player.health}")
    
    def add_text(self, text):
        self.text_area.config(state = tk.NORMAL)
        self.text_area.insert(tk.END, text)
        self.text_area.see(tk.END)
        self.text_area.config(state = tk.DISABLED)

    def clear_text(self):
        self.text_area.config(state=tk.NORMAL)
        self.text_area.delete(1.0, tk.END)
        self.text_area.config(state=tk.DISABLED)

    def show_intro(self):
        self.clear_text()
        self.clear_buttons()

        intro_text = ("You have awoken at the bottom of the stairs in a bizarre place.\n")
        self.add_text(intro_text)

        lore_btn = tk.Button(self.button_frame, text = "Hear Lore", command = self.show_lore)
        lore_btn.pack(side = tk.LEFT, padx = 5)

        blind_btn = tk.Button(self.button_frame, text = "Go in Blind", command = self.ask_name)
        blind_btn.pack(side = tk.RIGHT, padx = 5)

    def show_lore(self):
        self.clear_text()
        self.clear_buttons()

        lore_text = ("You are on the first level of the World Dungeon. Everyone on the surface of your planet is either dead, or down here with you. "
            "You woke up at the bottom of the stairs, in a dark hallway with nothing but the clothes on your back and whatever is in your pockets. "
            "You have 5 days before this floor collapses, going to a safe room will end the day.\n")
        self.add_text(lore_text)

        continue_btn = tk.Button(self.button_frame, text = "Continue", command=self.ask_name)
        continue_btn.pack()

    def ask_name(self):
        self.clear_text()
        self.clear_buttons()

        self.add_text("What is your name?\n")

        name_entry = tk.Entry(self.button_frame)
        name_entry.pack(side = tk.LEFT, padx = 5)

        submit_btn = tk.Button(self.button_frame, text="Submit",
                               command = lambda: self.start_game(name_entry.get()))
        submit_btn.pack(side = tk.LEFT, padx = 5)

    def start_game(self, name):
        self.player = Player(name)

        if name == "Admin":
            self.player.health = 99999
            self.player.gold = 99999
            self.player.key = True

        self.show_combat_rules()

    def show_combat_rules(self):
        self.clear_text()
        self.clear_buttons()
        self.add_text("BRUHASHDFH")

    def show_main_menu(self):
        self.clear_text()
        self.clear_buttons()

        self.update_health()
        self.update_day()

        self.add_text("What would you like to do?")

        explore_btn = tk.Button(self.button_frame, text = "Explore", 
                                command = self.handle_explore)
        explore_btn.pack(side = tk.LEFT, padx = 5)
        
        heal_btn = tk.Button(self.button_frame, text="Use Healing Potion", 
                           command = self.handle_heal)
        heal_btn.pack(side = tk.LEFT, padx=5)
        
        stats_btn = tk.Button(self.button_frame, text="Show Stats", 
                            command = self.show_stats)
        stats_btn.pack(side = tk.LEFT, padx=5)
        
        inv_btn = tk.Button(self.button_frame, text="Check Inventory", 
                          command = self.show_inv)
        inv_btn.pack(side = tk.LEFT, padx=5)
        
        safe_btn = tk.Button(self.button_frame, text="Go to Safe Room", 
                           command = self.go_to_safe)
        safe_btn.pack(side = tk.LEFT, padx=5)
        

    def handle_explore(self):
        self.clear_text()
        
        self.add_text("Exploring...")
        
        back_btn = tk.Button(self.button_frame, text="Continue", 
                           command=self.show_main_menu)
        back_btn.pack(side=tk.BOTTOM, pady=10)

    def handle_heal(self):
        pass

    def show_stats(self):
        pass

    def show_inv(self):
        pass

    def go_to_safe(self):
        pass





if __name__ == "__main__":
    root = tk.Tk()
    game = GameLoop(root)
    root.mainloop()

def main_loop(player):
    
    day = 1

    while True:
        # psuedo-godmode if player name is Admin
        if player.name == "Admin":
            player.health = 99999
            player.gold = 99999
            player.key = True
        
        if player.floor == 1:
            final_day = 5
        if player.floor == 2:
            final_day = 7
        if player.floor == 3:
            final_day = 10
        while day < final_day and player.health > 0:    
            
            clear_screen()
            print(f"\t\t\tDay: {day}\n\t\t----------------------")
            where = input("What would you like to do?\n"
                        "  1. Explore\n"
                        "  2. Use healing potion\n"
                        "  3. Show stats\n"
                        "  4. Check inventory\n"
                        "  5. End the day and go to a safe room\n"
                        "Enter here: ")
            while (where != "1") and (where != "2") and (where != "3") and (where != "4") and (where != "5"):
                where = input("Enter a valid number: ")
            where = int(where)

            match where:
                # explore
                case 1:
                    clear_screen()
                    explore(player)
                
                # heal
                case 2:
                    clear_screen()
                    player.heal()
                    press_enter()

                # stats
                case 3:
                    clear_screen()
                    player.display_player()

                # inv
                case 4:
                    clear_screen()
                    player.inventory()

                # safe room
                case 5:
                    clear_screen()
                    safe(player, day)
                    day += 1
        
        if player.health > 0:
            print("You've descended the stairs! Congrats!                      (still a bitch tho)\n")
            player.floor += 1
            player.key = False
            day = 0
            # TODO can maybe swap out for an iterator, but you still need a conditional for the intro i guess
            if player.floor == 1:
                player.floor = 2
                intro2()
            elif player.floor == 2:
                player.floor = 3
                intro3()
        else:
            player.death()  
            tmp = input("Would you like to play again? [y] or [n]: ")
            tmp = tmp.lower()
            while tmp != "y" and tmp != "n":
                tmp = input("Please enter [y] or [n]")
            if tmp == "y":
                player = Player(player.name)
                player.floor = 1
                player.key = False
                day = 1
            else: 
                exit()
            
