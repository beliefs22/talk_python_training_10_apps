import random


class Creature:
    def __init__(self, name, level):
        self.name = name
        self.level = level

    def get_defensive_role(self):
        return random.randint(1, 12) * self.level


class Wizard(Creature):

    def attack(self, creature):
        my_roll = self.get_defensive_role()
        creature_roll = creature.get_defensive_role()
        print("The hero rolls {} and the creature rolls {}".format(my_roll, creature_roll))

        if my_roll >= creature_roll:
            return True
        else:
            return False


class SmallAnimal(Creature):
    def get_defensive_role(self):
        base_roll = super().get_defensive_role()
        return base_roll / 2


class Dragon(Creature):
    def __init__(self, name, level, scaliness, breaths_fire):
        super().__init__(name, level)
        self.scaliness = scaliness
        self.breaths_fire = breaths_fire

    def get_defensive_role(self):
        base_roll = super().get_defensive_role()
        fire = 5 if self.breaths_fire else 1
        scales = self.scaliness / 10
        return base_roll * fire * scales