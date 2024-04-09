import os

def introduction():
   
    print_intro = input("You have awoken at the bottom of the stairs in a bizarre place.\n\
Do you want to hear some lore or do you want to go in blind? [lore] or [blind]: ")
    
    while (print_intro != "lore") and (print_intro != "blind"):
        print_intro = input("Please enter [lore] or [blind]: ")
    
    os.system('cls')
    
    if (print_intro == "lore"):
        print("You are on the first level of the World Dungeon. Everyone on the surface of your planet is either dead, or down here with you.\n\
You woke up at the bottom of the stairs, in a dark hallway with nothing but the clothes on your back and whatever is in your pockets.\n\
You have 5 days before this floor collapses, going to a safe room will end the day.\n")
        
    name = input("What is your name? ")
    return name


def combat_rules():

    display_rules = input("Do you want to hear the rules of combat? [y] or [n]: ")
    while (display_rules != "y") and (display_rules != "n"):
        display_rules = input("Please enter [y] or [n]: ")

    if display_rules == "y":
        os.system('cls')
        print(
            "_________________________RULES______________________________\n"
            "You will survive as long as your health remains above 0.\n"
            "A mob will die if you deplete their health.\n"
            "Overkilling a mob will heal you by half the amount you overkill by (if you reduce the mob to -4hp, you will heal by 2hp).\n"
            "A boss will be denoted by a long description, and a much tougher fight.\n"
            "Your stats will automatically increase every 5 levels.\n"
            "You MUST kill at least one boss per floor to acquire a staircase key. Without a key you cannot descend.\n"
            )
        input("Press enter to continue.")
    

def juicer_desc():
    print(
        "\t\t\tYOU'VE ENCOUTNERED THE JUICER!\n"
        "\nWith a body enhanced by the finest anabolic steroids the dark web has to offer, the Juicer spends his days pushing iron,\n"
        "snapping necks, and crying that his pimple-infested sac is a third the size it once was. Having reached a plateau, rage now fills his enlarged heart.\n"
        "All he ever wanted was to gain, but right now he'll settle on bringing out……the paaaaain!\n"
        "\nThe Juicer looks like a humanoid competition body builder with a lizard head and scaley body.\n"
        )

def hoarder_desc():
    print(
        "\t\t\tYOU'VE ENCOUNTERED THE HOARDER!\n"
        "Trapped in her pile of rubbish, abandoned by society, the war inside her head has seeped out of her mind and infected both her body and her surroundings.\n"
        "Now nothing more than a garbage troll, the Hoarder is a horrific reminder of what can happen to those who fall out of the light!\n"
        "\nThe Hoarder is a comically large woman drowning in garbage, who has adopted an almost cockroach like appearance.\n"
        )

def ball_desc():
    print(
        "\t\t\tYOU'VE ENCOUNTERED THE BALL OF SWINE!\n"
        "Also known as the Porkchop Express, the Ball of Swine is one of the rarest, most deadly battle formations of the Tuskling.\n"
        "Encompassing at least 30 Tuskling knights and their lady loves, a Ball formation requires a specific set of circumstances to create. Combine a gathering of \n"
        "Tuskling aristocracy, add an alcohol-fueled, sexually-charged orgy of war lust, and sometimes, just sometimes, the wild, ancient battle magic that permeates their war-torn world \n"
        "casts the spell, forming the ball. The Tusklings, the ruling class of the Orcish Supremacy, shape into an inseparable sphere that rolls onto the countryside. The ball of pork\n"
        "won't stop its night of terror until it has crushed the poor, the weak, and the lesser citizens under its unstoppable weight.\n"
        "\nThe Ball of Swine is  massive ball of pink, rippling flesh embedded with eyes, tusks, and scraps of tuxedos and red sequined dresses. It rolls shockingly fast,\n"
        "relying on its momentum to do very high damage.\n"
        )
    
def demon_desc():
    print(
        "\t\t\tYOU'VE ENCOUNTERED AN ASYLUM DEMON\n"
        "Within the gloomy confines of the asylum, the Asylum Demon, a grotesque fusion of muscle and misery, lumbers about. Its makeshift armor hangs \n"
        "off its bulging frame like a poorly tailored suit, while its frenzied attacks turn victims to paste. With eyes that only a mother could love,\n"
        "it stands guard over the asylum's secrets, a figure of relentless destruction.\n"

        "\nThe Asylum Demon has an almost draconic appearance, with spotted blue-green scales all over its body and a pair of stubby wings on its back.\n"
        )