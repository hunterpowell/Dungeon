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
                damage = (super().attack() * 2 + self.lvl)
                print(f"Flurry of blows! You did {damage} damage!")
                mob.health -= damage
                print(f"{mob.name} has {mob.health}hp remaining")
            case "Sentient Shotgun":
                damage = (super().attack() * 5 + self.lvl)
                print(f"Bullet rain! You did {damage} damage!")
                mob.health -= damage
                print(f"{mob.name} has {mob.health}hp remaining")
            case "War Gauntlet":
                damage = (super().attack() + 40 + self.lvl)
                print(f"Seismic Toss! You did {damage} damage!")
                mob.health -= damage
                print(f"{mob.name} has {mob.health}hp remaining")
            case "Cleric's Chime":
                healing = (random.randint(1,12) + 60 + self.lvl)
                print(f"Healing word! You healed for {healing}hp!")
                self.health += healing
                print(f"{mob.name} has {mob.health}hp remaining")

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
        press_enter()
        clear_screen()
    
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

    def monster_death(self, monster, key, money, max_hp):
        print(f"\nYou beat the {monster.name}!")
        print(f"You have {self.health}hp remaining!\n")
        # heal by half of overkill
        overkill = (0 - monster.health)/2
        self.health += int(overkill)
        if overkill > 0:
            print(f"You healed for {(int(overkill))}hp!")
        self.xp += max_hp
        print(f"You picked up {money} gold off the corpse!")
        self.gold += money
        print(f"You have earned {max_hp}xp!")
        self.level_up()
        if key == True and self.key == False:
            print("You found a key! You can now descend the stairs when the floor ends.")
            self.key = key
        press_enter()
            
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

    