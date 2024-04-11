import random
from game.characters.character import Character
from game.utils import clear_screen, press_enter 

class Player(Character):
    def __init__(self, name):
        super().__init__(name, health = 100, atk = 3, dmg = 5, ac = 10)
        self.scrolls = 0
        self.gold = 20
        self.lvl = 1
        self.xp = 0
        self.key = False
        self.weapon = "Fists"
        self.weapon_charge = True
        # self.class = ADD CLASSES, DIFF SPECIAL ABILITY BASED ON CLASS, DIFF CLASSES available BASED ON current WEAPON

    def special_atk(self, mob):
        match self.weapon:
            case "Fists":
                print("Flurry of blows!")
                damage = (super().attack() * 2 + self.lvl)
                print(f"You did {damage} damage!")
                mob.health -= damage
            case "Sentient Shotgun":
                print("Bullet rain!")
                damage = (super().attack() * 5 + self.lvl)
                print(f"You did {damage} damage!")
                mob.health -= damage
            case "War Gauntlet":
                print("Iron fist!")
                damage = (super().attack() + 40 + self.lvl)
                print(f"You did {damage} damage!")
                mob.health -= damage
            case "Cleric's Chime":
                print("Healing word!")
                healing = (random.randint(1,12) + 60 + self.lvl)
                print(f"You healed for {healing}hp!")
                self.health += healing

    def weapons(self):
        weapon_list = [
                    "Sentient Shotgun",
                    "War Gauntlet",
                    "Cleric's Chime"
        ]
        return random.choice(weapon_list)

    def inventory(self):
        print("    INVENTORY")
        print("=================")
        print("Scrolls:  ", self.scrolls)
        print("Gold:     ", self.gold)
        print("Weapon:   ", self.weapon)
        print("Key:      ", self.key)
    
    def usable_items(self):
        print("    INVENTORY")
        print("=================")
        print("Scrolls:  ", self.scrolls)

    def heal(self):
        if (self.scrolls > 0):    
            self.scrolls -= 1
            self.health += 50
            print("50hp restored!\n"
                  f"You have {self.health}hp remaining")
        else:
            print("You are out of healing scrolls! (dumbass)\n"
                  f"You have {self.health}hp remaining")

    def level_up(self):
        while self.xp > (self.lvl/0.3)**2:
            print(f"Leveled up to {self.lvl + 1}!!")
            self.lvl += 1
            # +1 atk, dmg, ac per 5 levels
            if self.lvl % 5 == 0:
                self.atk += 1
                self.dmg += 1
                self.ac += 1
            
    def display_player(self):
        super().display()
        print("Level:       ", self.lvl)
        print("Experience:  ", self.xp)
        print("Weapon:      ", self.weapon)
        press_enter()
        clear_screen()

    def death(self):
        print("\nYOU DIED")
        print(f"Nice try {self.name}, you made it further than any of us thought you would. Have fun in hell!\n")
        self.display_player()
        exit()

    