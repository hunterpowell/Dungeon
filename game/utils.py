import os
import random

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter():
    input("\nPress enter to continue...")

def two_d6():
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    return num1 + num2