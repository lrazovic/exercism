from math import floor
from random import seed, sample


def modifier(score: int) -> int:
    return floor((score - 10) / 2)


class Character:
    def __init__(self):
        seed()
        self.strength = self.ability()
        self.dexterity = self.ability()
        self.constitution = self.ability()
        self.intelligence = self.ability()
        self.wisdom = self.ability()
        self.charisma = self.ability()
        self.hitpoints = 10 + modifier(self.constitution)

    @staticmethod
    def ability() -> int:
        dices = sample(range(1, 7), 4)
        return sum(dices) - min(dices)

