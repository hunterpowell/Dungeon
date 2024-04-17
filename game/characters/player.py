import random
import math
from characters.character import Character
from utils import clear_screen, press_enter 
from lore import weapon_lore

class Player(Character):
    def __init__(self, name):
        super().__init__(name, health = 100, atk = 3, dmg = 5, ac = 10)
        self.scrolls = 0
        self.gold = 20
        self.lvl = 1
        self.xp = 0
        self.key = False
        self.ring1 = "None"
        self.ring2 = "None"
        self.job = "<Unassigned>"
        self.weapon_charge = True
        self.weapon = "Fists"
        self.martial = 0
        self.finesse = 0
        self.arcana = 0
        self.attunement = 0
        self.resolve = 0

    def weapons(self):
        weapon_list = [
                    "Sentient Shotgun",
                    "War Gauntlet",
                    "Cleric's Chime",
                    "Lifehunt Scythe",
                    "Staff of Rot"          #STAFF INFECTION
                    ]
        return random.choice(weapon_list)
    
    def weapon_stats(self):
        # balancing numbers- martial, finesse, arcana, attunement, resolve
        match self.weapon:
            case "Fists":
                return 0, 0, 0, 0, 0
            case "Sentient Shotgun":
                return 2, 1, 0, 0, 0
            case "War Gauntlet":
                return 1, 2, 0, 0, 0
            case "Cleric's Chime":
                return 0, 0, 0, 2, 1
            case "Lifehunt Scythe":
                return 1, 1, 1, 0, 0
            case "Staff of Rot":
                return 1, 0, 0, 2, 0
    
    def equip_weapon(self, martial, finesse, arcana, attunement, resolve):
        self.martial += martial
        self.finesse += finesse
        self.arcana += arcana
        self.attunement += attunement
        self.resolve += resolve

    def unequip_weapon(self, martial, finesse, arcana, attunement, resolve):
        self.martial -= martial
        self.finesse -= finesse
        self.arcana -= arcana
        self.attunement -= attunement
        self.resolve -= resolve

    def weapon_atk(self):
        return(super().attack() + self.dmg + self.martial)
    
    def special_atk(self, mob):
        match self.weapon:
            case "Fists":
                damage = (super().attack() * 2 + self.dmg + self.martial + self.lvl)
                print(f"Flurry of blows! You did {damage} damage!")
                mob.defend(damage)
            case "Sentient Shotgun":
                damage = (super().attack() * 5 + self.dmg + self.martial + self.lvl)
                print(f"Bullet rain! You did {damage} damage!")
                mob.defend(damage)
            case "War Gauntlet":
                damage = (super().attack() + 20 + self.dmg + self.martial + self.lvl)
                print(f"Rending Strike! You did {damage} damage!")
                mob.defend(damage)
            case "Cleric's Chime":
                healing = (random.randint(1,12) + 60 + self.lvl*self.attunement)
                print(f"Healing word! You healed for {healing}hp!")
                self.health += healing
                print(f"{mob.name} has {mob.health}hp remaining")
            case "Lifehunt Scythe":
                damage = (super().attack() * 4 + self.dmg + self.lvl)
                healing = math.ceil(damage*0.3)
                print(f"Sanguine Flare! You did {damage} damage, and healed for {healing}hp!")
                mob.defend(damage)
                self.health += healing
            case "Staff of Rot":
                damage = (super().attack())
                print(f"Staff Infection! You've poisoned the enemy! They'll take ")
                mob.poisoned = True
                print(f"{mob.name} has {mob.health}hp remaining")

    def buy_weapon(self, weapon):
        clear_screen()
        while True:
            pickup = input(f"You selected {weapon}\n"
                "What would you like to do??\n"
                "  1. Buy and equip weapon (this will discard current weapon)\n"
                "  2. See weapon description\n"
                "  3. Return to shop\n"
                "Enter here: "
                )
            while pickup.isdigit() == False:
                pickup = input("Please enter a number: ")
            
            while pickup != "1" and pickup != "2" and pickup != "3":
                pickup = input("Please enter a valid number: ")
            
            pickup = int(pickup)
            match pickup:
                case 1:
                    if self.gold >= 500:    
                        print(f"\n{weapon} equipped!")
                        self.unequip_weapon(self.weapon_stats()[0], self.weapon_stats()[1], self.weapon_stats()[2], self.weapon_stats()[3], self.weapon_stats()[4])
                        self.weapon = weapon
                        self.equip_weapon(self.weapon_stats()[0], self.weapon_stats()[1], self.weapon_stats()[2], self.weapon_stats()[3], self.weapon_stats()[4])
                        self.gold -= 500
                        press_enter()
                        break
                    else:
                        print("You can't afford this weapon! Skill issue.")
                        press_enter()
                        break
                    
                case 2:
                    weapon_lore(weapon)

                case 3:
                    break

    def rings(self):
        ring_list = [
            "Life ring",
            "Havel's ring",
            "Knight's ring",
            "Red tearstone ring",
            "Gambler's ",
            "Ring of divine suffering"
        ]

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
    
    def buy_health(self, max):
        print(f"Current gold: {self.gold}")
        print(f"Scrolls in stock: {max}")
        heal = input("\nHow many heal scrolls do you want? 100 gold each: ")
        while heal.isdigit() == False:
            heal = input("Please enter a valid number: ")
        #putting heal into a new variable as it's cast because of inconsistent behavior when trying heal = int(heal)
        heal_num = int(heal)
        while heal_num > max:
            heal = input(f"There are only {max} left for purchase today.\nTry again:")
            heal_num = int(heal)
        while (self.gold < (heal_num*100)):
            heal = input("You can't afford that many. Try again: ")
            heal_num = int(heal)
        else:
            self.gold -= (heal_num*100)
            self.scrolls += heal_num
            max -= heal_num
            print(f"You now have {self.scrolls} scrolls")
        press_enter()
        clear_screen()

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
        overkill = (0 - monster.health)//2
        self.health += overkill
        if overkill > 0:
            print(f"You healed for {overkill}hp!")
        self.xp += max_hp
        print(f"You picked up {money} gold off the corpse!")
        self.gold += money
        print(f"You have earned {max_hp}xp!")
        self.level_up()
        if key == True and self.key == False:
            print("You found a key! You can now descend the stairs when the floor ends.")
            self.key = key
        press_enter()

    def is_poisoned(self, mob):
        if mob.poisoned == True:
            poison = (mob.health // 20) + self.attunement
            print(f"{mob.name} is poisoned! It took {poison} damage!")
            mob.health -= poison

    def display_player(self):
        super().display()
        print("Level:       ", self.lvl)
        print("Experience:  ", self.xp)
        print("Martial:     ", self.martial)
        print("Finesse:     ", self.finesse)
        print("Attunement:  ", self.attunement)
        print("Arcana:      ", self.arcana)
        print("Resolve:     ", self.resolve)
        press_enter()
        clear_screen()

    def death(self):
        print("\nYOU DIED")
        print(f"Nice try {self.name}, you made it further than any of us thought you would. Have fun in hell!\n")
        self.display_player()

    