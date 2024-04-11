import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def press_enter():
    input("\nPress enter to continue...")