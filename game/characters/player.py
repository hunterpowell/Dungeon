import random
import math
from characters.character import Character
from utils import clear_screen, press_enter, two_d6
from lore import weapon_desc, ring_desc, armor_desc

class Player(Character):
    def __init__(self, name):
        super().__init__(name, health = 100, accuracy = 3, on_hit = 4, ac = 10)
        self.potions = 0
        self.rotpot = 0
        self.gold = 50
        self.lvl = 1
        self.xp = 0
        self.key = False
        self.can_heal = True
        self.job = "<Unassigned>"
        self.gear = {"ring1": "None",
                     "ring2": "None",
                     "weapon": "Fists",
                     "armor": "None"
                    }
        self.action = 1
        self.max_actions = 1
        self.max_charges = 1
        self.weapon_charges = 1
        self.floor = 1
        self.stats = {"martial": 0, 
                      "finesse": 0,
                      "arcana": 0,
                      "attunement": 0,
                      "resolve": 0}

    def weapons(self):
        weapon_list = [
                    "Sentient Shotgun",
                    "War Gauntlet",
                    "Cleric's Chime",
                    "Lifehunt Scythe",
                    "Staff of Rot",                  #STAFF INFECTION
                    "Hammer of Mithrix"
                    ]
        return random.choice(weapon_list)
    
    def weapon_stats(self):
        # balancing numbers- martial, finesse, arcana, attunement, resolve
        match self.gear["weapon"]:
            case "Fists":
                return 0, 0, 0, 0, 0
            case "Sentient Shotgun":
                return 2, 0, 1, 0, 0
            case "War Gauntlet":
                return 1, 2, 0, 0, 0
            case "Cleric's Chime":
                return 0, 0, 0, 2, 1
            case "Lifehunt Scythe":
                return 0, 1, 2, 0, 0
            case "Staff of Rot":
                return 1, 0, 0, 2, 0
            case "Hammer of Mithrix":
                return 2, 0, 0, 0, 1
    
    def equip_weapon(self, martial, finesse, arcana, attunement, resolve):
        self.stats["martial"] += martial
        self.stats["finesse"] += finesse
        self.stats["arcana"] += arcana
        self.stats["attunement"] += attunement
        self.stats["resolve"] += resolve

    def unequip_weapon(self, martial, finesse, arcana, attunement, resolve):
        self.stats["martial"] -= martial
        self.stats["finesse"] -= finesse
        self.stats["arcana"] -= arcana
        self.stats["attunement"] -= attunement
        self.stats["resolve"] -= resolve

    def weapon_atk(self):
        damage = (super().attack() + self.stats["martial"])
        heal = math.ceil(damage * (self.stats["arcana"] * .05))
        self.health += heal
        print(f"You hit for {damage} damage!")
        if heal > 0:    
            print(f"You healed for {heal}hp!")
        return damage
    
    def weapon_crit(self):
        damage = (super().crit() + self.stats["martial"])
        heal = math.ceil(damage * (self.stats["arcana"] * .05))
        self.health += heal
        print(f"You hit for {damage} damage!")
        if heal > 0:    
            print(f"You healed for {heal}hp!")
        return damage
    
    def special_atk(self, mob):
        damage = 0
        healing = 0
        match self.gear["weapon"]:
            case "Fists":
                damage = (two_d6() * 2 + self.on_hit + self.stats["martial"] + self.lvl)
                print(f"Flurry of Blows! You did {damage} damage!")
                mob.defend(damage)
            case "Sentient Shotgun":
                damage = (two_d6() * 5 + self.on_hit + self.stats["martial"] + self.lvl)
                print(f"Bullet Rain! You did {damage} damage!")
                mob.defend(damage)
            case "War Gauntlet":
                damage = (two_d6() + 20 + self.on_hit + self.stats["martial"] + self.lvl)
                print(f"Rending Strike! You did {damage} damage!")
                mob.defend(damage)
            case "Cleric's Chime":
                healing = (random.randint(1,12) + 60 + self.lvl + (2 * self.stats["attunement"]))
                print(f"Healing Word!")
            case "Lifehunt Scythe":
                damage = (two_d6() * 4 + self.on_hit + self.stats["martial"] + self.lvl)
                if self.can_heal == True:
                    healing = math.ceil(damage*0.3)
                    print(f"Sanguine Flare! You did {damage} damage")
                mob.defend(damage)
                self.health += healing
            case "Staff of Rot":
                damage = (two_d6() * 2 + self.on_hit + self.stats["martial"] + self.lvl)
                print(f"Staff Infection! You did {damage} damage and poisoned the enemy!")
                mob.defend(damage)
                mob.poisoned = True
            case "Hammer of Mithrix":
                damage = (two_d6() * 5 + self.on_hit + self.stats["martial"] + self.lvl)
                print(f"Earth Shatter! You did {damage} damage")
                mob.defend(damage)
        healing += math.ceil(damage * (self.stats["arcana"] * .05))
        if healing > 0:    
            print(f"You healed for {healing}hp!")
        self.health += healing

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
                        self.gear["weapon"] = weapon
                        self.equip_weapon(self.weapon_stats()[0], self.weapon_stats()[1], self.weapon_stats()[2], self.weapon_stats()[3], self.weapon_stats()[4])
                        self.gold -= 500
                        press_enter()
                        break
                    else:
                        print("You can't afford this weapon! Skill issue.")
                        press_enter()
                        break
                    
                case 2:
                    weapon_desc(weapon)

                case 3:
                    break

    def rings(self):
        ring_list = [
            "Life ring",
            "Havel's ring",
            "Knight's ring",
            "Gambler's token",
            "Ring of divine suffering",
            "Duelist's secret",
            "Arcanist's ring"
        ]
        return random.choice(ring_list)
    
    def equip_ring(self, ring):
        match ring:
            case "Life ring":
                self.max_hp += 25
            case "Havel's ring":
                self.stats["resolve"] += 2
            case "Knight's ring":
                self.stats["martial"] += 2
            case "Gambler's token":
                self.stats["martial"] += 3
                self.stats["finesse"] -= 3
            case "Ring of divine suffering":
                self.can_heal = False
                self.stats["martial"] += 5
                self.stats["finesse"] += 5
            case "Duelist's secret":
                self.max_charges += 1
                self.weapon_charges = self.max_charges
            case "Arcanist's ring":
                self.stats["arcana"] += 2
        
    def unequip_ring(self, ring):
        match ring:
            case "Life ring":
                self.max_hp -= 25
            case "Havel's ring":
                self.stats["resolve"] -= 2
            case "Knight's ring": 
                self.stats["martial"] -= 2
            case "Gambler's token":
                self.stats["martial"] -= 3
                self.stats["finesse"] += 3
            case "Ring of divine suffering":
                self.can_heal = False
                self.stats["martial"] -= 5
                self.stats["finesse"] -= 5
            case "Duelist's secret":
                self.max_charges -= 1
            case "Arcanist's ring":
                self.stats["arcana"] += 2

    def buy_ring(self, ring):
        clear_screen()
        while True:
            pickup = input(f"You selected {ring}\n"
                "What would you like to do?\n"
                "  1. Buy and equip ring\n"
                "  2. See ring description\n"
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
                    if self.gold >= 200:    
                        if self.gear["ring1"] != "None" and self.gear["ring2"] != "None":
                            clear_screen()
                            print("Both of your ring slots are full. Which ring would you like to replace?")
                            print(f"  1. {self.gear["ring1"]}")
                            print(f"  2. {self.gear["ring2"]}")
                            print("  3. Back to menu")
                            which = input("Enter here: ")
                            while which != "1" and which != "2" and which != "3":
                                which = input("Please enter a valid number: ")

                            if which == "1":
                                self.unequip_ring(self.gear["ring1"])
                                self.gear["ring1"] = "None"
                            elif which == "2":
                                self.unequip_ring(self.gear["ring2"])
                                self.gear["ring2"] = "None"
                            else:
                                break
                        
                        if self.gear["ring1"] == "None":    
                            self.gear["ring1"] = ring
                            self.equip_ring(ring)
                        elif self.gear["ring2"] == "None":
                            self.gear["ring2"] = ring
                            self.equip_ring(ring)

                        print(f"{ring} equipped!")
                        self.gold -= 200
                        press_enter()
                        break
                    else:
                        print("You can't afford this ring! Skill issue.")
                        press_enter()
                        break
                    
                case 2:
                    ring_desc(ring)

                case 3:
                    break

    def armors(self):
        armor_list = [
                    "Chainmail Breastplate",
                    "Enchanted Trollskin Shirt of Pummeling",
                    "Cloak of Obscurity",
                    "Mithril Shirt",
                    "Enchanted Suspenders of Suspension",
                    "Living Armor"
                    ]
        return random.choice(armor_list)

    def equip_armor(self, armor):
        match armor:
            case "Chainmail Breastplate":
                self.stats["resolve"] += 3
            case "Enchanted Trollskin Shirt of Pummeling":
                self.stats["resolve"] += 1
                self.stats["martial"] += 3
            case "Cloak of Obscurity":
                self.ac += 5
            case "Mithril Shirt":
                self.stats["resolve"] += 3
                self.ac += 2
            case "Enchanted Suspenders of Suspension":
                self.max_charges += 2
            case "Living Armor":
                self.stats["resolve"] += 2
                self.stats["arcana"] += 3

    def unequip_armor(self, armor):
        match armor:
            case "Chainmail Breastplate":
                self.stats["resolve"] -= 3
            case "Enchanted Trollskin Shirt of Pummeling":
                self.stats["resolve"] -= 1
                self.stats["martial"] -= 3
            case "Cloak of Obscurity":
                self.ac -= 5
            case "Mithril Shirt":
                self.stats["resolve"] -= 3
                self.ac -= 2
            case "Enchanted Suspenders of Suspension":
                self.max_charges -= 2
            case "Living Armor":
                self.stats["resolve"] -= 2
                self.stats["arcana"] -= 3

    def buy_armor(self, armor):
        clear_screen()
        while True:
            pickup = input(f"You selected {armor}\n"
                "What would you like to do??\n"
                "  1. Buy and equip armor (this will discard current armor)\n"
                "  2. See armor description\n"
                "  3. Return to shop\n"
                "Enter here: "
                )
            
            while pickup != "1" and pickup != "2" and pickup != "3":
                pickup = input("Please enter a valid number: ")
            
            match pickup:
                case "1":
                    if self.gold >= 500:    
                        print(f"\n{armor} equipped!")
                        self.unequip_armor(self.gear["armor"])
                        self.gear["armor"] = armor
                        self.equip_armor(armor)
                        self.gold -= 500
                        press_enter()
                        break
                    else:
                        print("You can't afford this armor! Skill issue.")
                        press_enter()
                        break
                    
                case "2":
                    armor_desc(armor)

                case "3":
                    break

    def hats(self):
        hat_list = [
                "Sage's Big Hat",
                "Helm of Punching Things Really Hard", 
                "Cinemetographer's Beret",                  # ACTION, ACTION, ACTION, gives an extra action
                "Mining Helmet"                             # who fckin knows man
                ]

    def buy_pot(self, max):
        clear_screen()
        print("ITEM SHOP".center(40))
        print("----------------------------------------")
        print(f"Current gold: {self.gold}")
        print(f"Pots in stock: {max}")
        pot = input("\nHow many pots do you want? 100 gold each: ")
        while pot.isdigit() == False:
            pot = input("Please enter a valid number: ")
        pot_num = int(pot)
        while pot_num > max:
            pot = input(f"There are only {max} left for purchase today.\nTry again: ")
            pot_num = int(pot)
        while (self.gold < (pot_num*100)):
            pot = input("You can't afford that many. Try again: ")
            pot_num = int(pot)
        else:
            self.gold -= (pot_num*100)
            self.rotpot += pot_num
            max -= pot_num
            print(f"You now have {self.rotpot} rot pots")
        press_enter()
        clear_screen()
        return max

    def inventory(self):
        # inv_text =("INVENTORY\n")
        # inv_text +=("=================\n")
        inv_text =(f"Gold:      {self.gold}\n")
        inv_text +=(f"Potions:   {self.potions}\n")
        inv_text +=(f"Rot pots:  {self.rotpot}\n")
        inv_text +=(f"Weapon:    {self.gear["weapon"]}\n")
        inv_text +=(f"Ring 1:    {self.gear["ring1"]}\n")
        inv_text +=(f"Ring 2:    {self.gear["ring2"]}\n")
        inv_text +=(f"Armor:     {self.gear["armor"]}\n")
        inv_text +=(f"Key:       {self.key}\n")
        return inv_text
    
    def usable_items(self):
        print("Potions:  ", self.potions)
        print("Rot pots: ", self.rotpot)

    def heal(self):
        if self.can_heal == True:
            if (self.potions > 0):    
                self.potions -= 1
                self.health += 50
                return ("50hp restored!")
            else:
               return ("You are out of healing potions! (dumbass)")
        else:
            return("You cannot heal!")  
    
    def buy_heals(self, max):
        clear_screen()
        print("ITEM SHOP".center(40))
        print("----------------------------------------")
        print(f"Current gold: {self.gold}")
        print(f"potions in stock: {max}")
        heal = input("\nHow many heal potions do you want? 50 gold each: ")
        while heal.isdigit() == False:
            heal = input("Please enter a valid number: ")
        #putting heal into a new variable as it's cast because of inconsistent behavior when trying heal = int(heal)
        heal_num = int(heal)
        while heal_num > max:
            heal = input(f"There are only {max} left for purchase today.\nTry again: ")
            heal_num = int(heal)
        while (self.gold < (heal_num*50)):
            heal = input("You can't afford that many. Try again: ")
            heal_num = int(heal)
        else:
            self.gold -= (heal_num*50)
            self.potions += heal_num
            max -= heal_num
            print(f"You now have {self.potions} potions")
        press_enter()
        clear_screen()
        return max

    def level_up(self):
        while self.xp > (self.lvl/0.3)**2:
            print(f"Leveled up to {self.lvl + 1}!!")
            self.lvl += 1
            # +1 accuracy, on_hit, ac per 5 levels
            if self.lvl % 5 == 0:
                self.accuracy += 1
                self.on_hit += 1
                self.ac += 1

    def monster_death(self, monster, key, money, max_hp):
        print(f"\nYou beat the {monster.name}!")
        # heal by half of overkill
        overkill = 0
        if self.can_heal == True:    
            overkill = (0 - monster.health)//2
        self.health += overkill
        if overkill > 0:
            print(f"You healed for {overkill}hp!")
        self.xp += max_hp
        print(f"You have {self.health}hp remaining.")
        print(f"You picked up {money} gold off the corpse.")
        self.gold += money
        print(f"You have earned {max_hp}xp.")
        self.level_up()
        if key == True and self.key == False:
            print("You found a key! You can now descend the stairs when the floor ends.")
            self.key = key
        press_enter()

    def display_player(self):
        stats_text = super().display()
        stats_text += (f"Level:         {self.lvl}\n")
        stats_text += (f"Experience:    {self.xp}\n")
        stats_text += (f"Wpn charges:   {self.weapon_charges}\n")
        stats_text += (f"Martial:       {self.stats["martial"]}\n")
        stats_text += (f"Finesse:       {self.stats["finesse"]}\n")
        stats_text += (f"Attunement:    {self.stats["attunement"]}\n")
        stats_text += (f"Arcana:        {self.stats["arcana"]}\n")
        stats_text += (f"Resolve:       {self.stats["resolve"]}\n")


        return stats_text

    def death(self):
        print("\nYOU DIED")
        print(f"Nice try {self.name}, you made it further than any of us thought you would. Have fun in hell!\n")
        self.display_player()

    