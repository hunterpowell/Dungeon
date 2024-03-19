import random

def initialize():
    
    num = random.randint(0,3)

    match num:
        case 0:
            name = "rat"
            health = 10
            atk = 2
        case 1: 
            name = "goblin"
            health = 30
            atk = 5
        case 2:
            name = "slime"
            health = 50
            atk = 1
        case 3: 
            name = "BOSS: The Juicer!"
            health = 200
            atk = 10

    return name, health, atk