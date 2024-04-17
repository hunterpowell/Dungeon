import random

class Test:
    def __init__(self):
        self.name = 1
        self.age = 2
        self.num = 3

    def equip(self, name, age, num):
        self.name += name
        self.age += age
        self.num += num

    def unequip(self, name, age, num):
        self.name -= name
        self.age -= age
        self.num -= num


def main():
    print("hi")
    uwu = Test()
    print(select())
    # uwu.equip(1, 2, 3)
    # uwu.equip(select()[0], select()[1], select()[2])
    uwu.unequip(select()[0], select()[1], select()[2])
    print(uwu.name, uwu.age, uwu.num)

def select():
    return 1, 2, 3



main()