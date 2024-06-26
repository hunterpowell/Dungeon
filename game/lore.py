import textwrap
from utils import clear_screen, press_enter

def introduction():
   
    clear_screen()
    print_intro = input(
        "You have awoken at the bottom of the stairs in a bizarre place.\n"
        "Do you want to hear some lore or do you want to go in blind?\n"
        "  1. Lore\n"
        "  2. Blind\n"
        "Enter here: ")
    
    while (print_intro != "1") and (print_intro != "2"):
        print_intro = input("Please enter a valid number: ")
    
    clear_screen()
    
    if (print_intro == "1"):
        intro = (
            "You are on the first level of the World Dungeon. Everyone on the surface of your planet is either dead, or down here with you. "
            "You woke up at the bottom of the stairs, in a dark hallway with nothing but the clothes on your back and whatever is in your pockets. "
            "You have 5 days before this floor collapses, going to a safe room will end the day.\n"
        )
        print(textwrap.fill(intro, 80))
        
    name = input("What is your name? ")
    return name


def combat_rules():

    while True:
        clear_screen()
        display = input("What would you like to do?\n"
                    "  1. Display rules of the dungeon.\n"
                    "  2. Show brief explanation of stats\n"
                    "  3. Begin the crawl\n"
                    "Enter here: "
                    )
        while display != "1" and display != "2" and display != "3":
            display = input("Please enter a valid number: ")

        match display:
            case "1":
                clear_screen()
                print("RULES".center(60))
                print("-" * 60)
                print(
                    "You will survive as long as your health remains above 0.\n"
                    "A mob will die if you deplete their health.\n"
                    "Overkilling a mob will heal you by half the amount you overkill by.\n"
                    "A boss will be denoted by a long description, and a much tougher fight.\n"
                    "Your special attack is weapon dependant and strengthens with levels.\n"
                    "Special attacks can be used once per day, this can be increased with items.\n"
                    "All special attack charges replenish upon picking up a new weapon\n"
                    "You MUST kill at least one boss per floor to acquire a staircase key.\n"
                    "Without a key, you cannot descend and you will die."
                )
                press_enter()
            
            case "2":
                clear_screen()
                print("STATS".center(60))
                print("-" * 60)
                print(
                    "Level:       Current player level. Stats automatically increase every 5 levels.\n"
                    "Wpn charges: Total special attack charges you currently have.\n"
                    "Martial:     Your martial ability. Increases on-hit damage.\n"
                    "Finesse:     Your accuracy bonus. Improves attack rolls.\n"
                    "Attunement:  Your magical prowess. Strengthens healing and status effects.\n"
                    "Arcana:      A glimpse into the Void. Grants forbidden knowledge, imparting lifesteal.\n"
                    "Resolve:     Your ability to ignore damage. Reduces incoming damage."
                )
                press_enter()

            case "3":
                clear_screen()
                break


def juicer_desc():
    print("YOU'VE ENCOUNTERED THE JUICER!\n".center(80))
    juicer = ("With a body enhanced by the finest anabolic steroids the dark web has to offer, the Juicer spends his days pushing iron,"
            "snapping necks, and crying that his pimple-infested sac is a third the size it once was. Having reached a plateau, rage now fills his enlarged heart. "
            "All he ever wanted was to gain, but right now he'll settle on bringing out……the paaaaain\n")
    print(textwrap.fill(juicer, 80))
    print("\nThe Juicer looks like a humanoid competition body builder with a lizard head and scaley body.")

def hoarder_desc():
    print("YOU'VE ENCOUNTERED THE HOARDER!\n".center(80))
    hoarder = ("Trapped in her pile of rubbish, abandoned by society, the war inside her head has seeped out of her mind and infected both her body and her surroundings."
             "Now nothing more than a garbage troll, the Hoarder is a horrific reminder of what can happen to those who fall out of the light!\n")
    print(textwrap.fill(hoarder, 80))
    print("\nThe Hoarder is a comically large woman drowning in garbage, who has adopted an almost cockroach like appearance.")
    

def ball_desc():
    print("YOU'VE ENCOUNTERED THE BALL OF SWINE!\n".center(80))
    ball = ("Also known as the Porkchop Express, the Ball of Swine is one of the rarest, most deadly battle formations of the Tuskling. "
            "Encompassing at least 30 Tuskling knights and their lady loves, a Ball formation requires a specific set of circumstances to create. Combine a gathering of "
            "Tuskling aristocracy, add an alcohol-fueled, sexually-charged orgy of war lust, and sometimes, just sometimes, the wild, ancient battle magic that permeates their war-torn world "
            "casts the spell, forming the ball. The Tusklings, the ruling class of the Orcish Supremacy, shape into an inseparable sphere that rolls onto the countryside. The ball of pork "
            "won't stop its night of terror until it has crushed the poor, the weak, and the lesser citizens under its unstoppable weight.\n")
    ball2 = ("The Ball of Swine is  massive ball of pink, rippling flesh embedded with eyes, tusks, and scraps of tuxedos and red sequined dresses. It rolls shockingly fast,\n"
            "relying on its momentum to do very high damage.")
    print(textwrap.fill(ball, 80))
    print(textwrap.fill(ball2, 80))
    
    
def demon_desc():
    print("YOU'VE ENCOUNTERED AN ASYLUM DEMON\n".center(80))
    demon = ("Within the gloomy confines of the asylum, the Asylum Demon, a grotesque fusion of muscle and misery, lumbers about. Its makeshift armor hangs "
            "off its bulging frame like a poorly tailored suit, while its frenzied attacks turn victims to paste. With eyes that only a mother could love, " 
            "it stands guard over the asylum's secrets, a figure of relentless destruction.\n")
    demon2 = ("The Asylum Demon has an almost draconic appearance, with spotted blue-green scales all over its body and a pair of stubby wings on its back.")
    print(textwrap.fill(demon, 80))
    print(textwrap.fill(demon2, 80))

def monster_lore(mob):
    match mob.name:
        case "JUICER":
            juicer_desc()
            press_enter()
            clear_screen()
        case "HOARDER":
            hoarder_desc()
            press_enter()
            clear_screen()
        case "BALL OF SWINE":
            ball_desc()
            press_enter()
            clear_screen()
        case "ASYLUM DEMON":
            demon_desc()
            press_enter()
            clear_screen()


def fist_desc():
    print(
        "Bare fists. Not very impressive as far as weapons go.\n"
        "Special Attack: Flurry of Blows. Two rapid punches that cannot miss.\n"
        "Damage roll: 4d6 + on_hit bonus + level"
    )

def shotgun_desc():
    print(
        "Sentient Shotgun. It appears to be a full-auto shotgun with an infinite ammo enchantment.\n"
        "Special Attack: Bullet Rain. Sends a frankly comical amount of lead towards the enemy doing massive damage.\n"
        "Special attack damage roll: 10d6 + on_hit bonus + level\n"
        "Grants +2 to martial ability and +1 to arcana.\n"
        "You swear you hear something speaking to you every shot, something old and powerful. Surely it's just your imagination."
    )
    
def gauntlet_desc():
    print(
        "War Gauntlet. A wrist bracer that turns into a spiked gauntlet when the hand is shaped into a fist.\n"
        "Special Attack: Rending Strike. A punch that the monster's grandchildren will feel.\n"
        "Damage roll: 2d6 + 20 + on_hit bonus + level\n"
        "Grants +2 to finesse and +1 to martial ability."
    )

def chime_desc():
    print(
        "Cleric's Chime. A small chime impbued with divine energy.\n"
        "Special Attack: Healing Word. Massive spell that heals the caster for a significant amount.\n"
        "Heal roll: 1d12 + 60 + (2 * level)\n"
        "Grants +2 to attunement and +1 to resolve."
    )
    
def scythe_desc():
    print(
        "Lifehunt Scythe. Ethereal scythe with a shimmering red aura.\n"
        "Special Attack: Sanguine Flare. Sweeping attack that heals the attacker for 30% of damage done.\n"
        "Damage roll: 8d6 + on_hit bonus + level\n"
        "Grants +1 to martial, +1 to finesse, and +1 to arcana."
    )

def staff_desc():
    print(
        "Staff of Rot. Large staff made of gnarled and twisted wood.\n"
        "Special Attack: Staff Infection. Cloud attack that inflicts poison on the enemy.\n"
        "Special attack also does 4d6 + on_hit bonus + level\n"
        "Poison damage per turn: %5 enemy max health + attunment\n"
        "Grants +1 to martial ability and +2 to attunement"
    )

def weapon_lore(weapon):
    clear_screen()
    match weapon:
        case "Fists":
            fist_desc()
        case "Sentient Shotgun":
            shotgun_desc()
        case "War Gauntlet":
            gauntlet_desc()
        case "Cleric's Chime":
            chime_desc()
        case "Lifehunt Scythe":
            scythe_desc()
        case "Staff of Rot":
            staff_desc()
    press_enter()
    clear_screen()

def ring_desc(ring):
    clear_screen()
    match ring:
        case "Life ring":
            print(
                "Red gem in a black metal band.\n"
                "Grants +25 to max health."
                )
        case "Havel's ring":
            print(
                "Dull grey ring that appears to be made of stone.\n"
                "Grants +5 to resolve."
            )
        case "Knight's ring":
            print(
                "Gold ring with the likeness of a knight on it.\n"
                "Grants +2 to martial ability."
            )
        case "Gambler's token":
            print(
                "Small poker chip with a grey band hastily attached.\n"
                "Grants +3 to martial ability.\n"
                "Grants -3 to finesse."
            )
        case "Ring of divine suffering":
            print(
                "Ornate ring with a red gem that glimmers with enchantment.\n"
                "Grants +5 to martial ability.\n"
                "Grants +5 to finesse.\n"
                "Removes your ability to heal. (safe room still heals you)"
            )
        case "Duelist's secret":
            print(
                "Small emblem portraying two crossed daggers.\n"
                "Grants +1 weapon charge.\n"
                "This does stack with other items that grant extra weapon charges."
            )
        case "Arcanist's ring":
            print(
                "Plain red band with an ever-moving smoky pattern.\n"
                "Grants +2 to arcana.\n"
                "You swear you can see a glimpse of something much bigger than yourself..."
            )
    press_enter()
    clear_screen()