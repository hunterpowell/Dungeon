import random
from game.characters.character import Character

class Player(Character):
    def __init__(self, name):
        super().__init__(name, health = 100, atk = 3, dmg = 5, ac = 10)
        self.scrolls = 0
        self.gold = 20
        self.lvl = 1
        self.xp = 0
        self.key = False
        self.weapon = "fists"
        # self.class = ADD CLASSES, DIFF SPECIAL ABILITY BASED ON CLASS, DIFF CLASSES available BASED ON WEAPON

    def special_atk(self, mob):
        match self.weapon:
            case "fists":
                print("Flurry of blows!")
                damage = (super().attack() * 2)
                print(f"You did {damage} damage!")
                mob.health -= damage
            case "shotgun":
                print("Bullet rain!")
                damage = (super().attack() * 5)
                print(f"You did {damage} damage!")
                mob.health -= damage
            case "war gauntlet":
                print("Iron fist!")
                damage = (super().attack() + 40)
                print(f"You did {damage} damage!")
                mob.health -= damage
            case "cleric's chime":
                print("Healing word!")
                healing = (random.randint(1,12) + 60)
                print(f"You healed for {healing}hp!")
                self.health += healing

    def inventory(self):
        print("    INVENTORY")
        print("=================")
        print("Scrolls:  ", self.scrolls)
        print("Gold:     ", self.gold)
        print("Key:      ", self.key)
    
    def usable_items(self):
        print("    INVENTORY")
        print("=================")
        print("Scrolls:  ", self.scrolls)

    def heal(self):
        if (self.scrolls > 0):    
            self.scrolls -= 1
            self.health += 50
            print("50hp restored. HP remaining: ", self.health)
        else:
            print("You are out of healing scrolls")

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

    def death(self):
        print("\nYOU DIED")
        print(f"Nice try {self.name}, you made it further than any of us thought you would. Have fun in hell!\n")
        self.display_player()
        input()                    # requires enter to be pressed before program closes
        exit()

    