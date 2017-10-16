from actors import Creature, SmallAnimal, Dragon, Wizard
import time
import random

def main():
    print_header()
    game_loop()
    pass


def print_header():
    print("-------------------")
    print("     Wizard Battle")
    print("-------------------")


def game_loop():
    creatures = [
        Creature('Tiger', 12),
        SmallAnimal('Bat', 1),
        SmallAnimal('Rat', 2),
        Dragon('Nice Dragon', 50, 5, True),
        Wizard('Evil Wizard', 100)
    ]

    hero = Wizard('Gandolf', 75)
    while True:

        creature = random.choice(creatures)
        print("A {} of level {} appears".format(creature.name, creature.level))
        cmd = input("[a]ttack [r]unaway [l]ookaround [q]uit ")
        if cmd.lower() == "a":
            if hero.attack(creature):
                print("{} defeated {}".format(hero.name, creature.name))
                creatures.remove(creature)
            else:
                print("You shouldn't have done that.....Go get some rest")
                time.sleep(5)
                print("You are rested. Please make better life choices")
        elif cmd.lower() == "r":
            print("That was probably a good choice")
        elif cmd.lower() == "l":
            for c in creatures:
                # Skip creature you are currently fighting
                if c == creature:
                    continue
                print("- A {} of level {}".format(c.name, c.level))
        else:
            print("Goodluck on your wizarding journey")
            break

        if not creatures:
            print("The hero has triumphed")
            break


if __name__ == '__main__':
    main()
