import random
import string
from itertools import product

ALPHABET = string.ascii_uppercase
prefix = ["".join(p) for p in product(ALPHABET, ALPHABET)]
suffix = [str(n).zfill(3) for n in range(1000)]
available_names = ["".join(p) for p in product(prefix, suffix)]
used_names = []


class Robot:
    def __init__(self):
        self.name = self.generate_random_name()

    def reset(self):
        self.__init__()

    @staticmethod
    def generate_random_name():
        name = random.choice(available_names)
        available_names.remove(name)
        used_names.append(name)
        return name
