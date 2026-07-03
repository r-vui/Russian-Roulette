import random
import sys

def main():
    bullets = validateBullets(input("How many bullets (1-6)"))
    chamber = loadChamber(bullets)
    fire(chamber)


def validateBullets(n):
    try:
        n = int(n)
    except ValueError:
        print("Enter an integer between 1 and 6")
    else:
        if n < 1 or n > 6:
            print("Enter an integer between 1 and 6")
        else:
            return n

def loadChamber(b):
    chamber = []
    for i in range(b):
        chamber.append(1)
    while len(chamber) < 6:
        chamber.append(0)
    random.shuffle(chamber)
    return chamber

def fire(chamber):
    alive = True
    while alive:
        print(f"{len(chamber)} spins left.")
        input("Press enter to fire")
        if chamber[0] == 1:
            print("you shot yourself")
            alive = False
        else:
            print("you survived")
            chamber.pop(0)

main()