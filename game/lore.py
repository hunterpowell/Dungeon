
def introduction():
   
    print_intro = input("\n\nYou have awoken at the bottom of the stairs in a bizarre place. \
Do you want to hear some lore or do you want to go in blind? [lore] or [blind]: ")
    
    while (print_intro != "lore") and (print_intro != "blind"):
        print_intro = input("Please enter [lore] or [blind]: ")
    
    if (print_intro == "lore"):
        print("\nYou are on the first level of the World Dungeon. Everyone on the surface of your planet is either dead, or down here with you.\n\
You woke up at the bottom of the stairs, in a dark hallway with nothing but the clothes on your back and whatever is in your pockets.\n\
You have 5 days before this floor collapses, going to a safe room will end the day.\n")
        
    name = input("What is your name? ")
    return name

def combat_rules():

    display_rules = input("\nDo you want to hear the rules of combat? [y] or [n]: ")
    while (display_rules != "y") and (display_rules != "n"):
        display_rules = input("Please enter [y] or [n]: ")

    if display_rules == "y":
        print(
            "_________________________RULES______________________________\n"
            "You will survive as long as your health remains above 0.\n"
            "A mob will die if you deplete their health.\n"
            "Overkilling a mob will heal you by the amount you overkill by (if you reduce the mob to -5hp, you will heal by 5hp).\n"
            "A boss will be denoted by a long description, and a much tougher fight.\n"
            )

def juicer_desc():
    print("With a body enhanced by the finest anabolic steroids the dark web has to offer, the Juicer spends his days pushing iron, \n\
snapping necks, and crying that his pimple-infested sac is a third the size it once was. Having reached a plateau, rage now fills his enlarged heart.\n\
All he ever wanted was to gain, but right now he'll settle on bringing out……the paaaaain!\n")
    print("\nThe Juicer looks like a humanoid competition body builder with a lizard head and scaley body.\n")

def hoarder_desc():
    print("Trapped in her pile of rubbish, abandoned by society, the war inside her head has seeped out of her mind and infected both her body and her surroundings.\n\
Now nothing more than a garbage troll, the Hoarder is a horrific reminder of what can happen to those who fall out of the light!\n")
    print("\nThe Hoarder is a comically large woman drowning in garbage, who has also adopted an almost cockroach like appearance.\n")

def ball_desc():
    print("Also known as the Porkchop Express, the Ball of Swine is one of the rarest, most deadly battle formations of the Tuskling.\n\
Encompassing at least 30 Tuskling knights and their lady loves, a Ball formation requires a specific set of circumstances to create. Combine a gathering of \n\
Tuskling aristocracy, add an alcohol-fueled, sexually-charged orgy of war lust, and sometimes, just sometimes, the wild, ancient battle magic that permeates their war-torn world \n\
casts the spell, forming the ball. The Tusklings, the ruling class of the Orcish Supremacy, shape into an inseparable sphere that rolls onto the countryside. The ball of pork\n\
won't stop its night of terror until it has crushed the poor, the weak, and the lesser citizens under its unstoppable weight.\n")
    print("\nThe Ball of Swine is  massive ball of pink, rippling flesh embedded with eyes, tusks, and scraps of tuxedos and red sequined dresses. It rolls shockingly fast, relying on \n\
its momentum to do very high damage.\n")