import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

import numpy as np

from src.util.ring_of_integers import RingOfIntegersModulo

class Vector(np.ndarray):
    def __new__(cls, vector, dtype=float):
        return super().__new__(cls, (1, len(vector)), dtype=dtype)

    def __init__(self, vector, dtype=float):
        for i, vi in enumerate(vector):
            self[0, i] = vi

    def __str__(self):
        return "[" + ", ".join((str(v) for v in self[0])) + "]"

    def __eq__(self, vector):
        if len(self[0]) != len(vector[0]):
            return False
        return all((i==j for i,j in zip(self[0], vector[0])))


def main():
    to_modulo4 = lambda x: RingOfIntegersModulo(x, 4)
    a = Vector([*map(to_modulo4, [1,2,3])], dtype=RingOfIntegersModulo)
    b = Vector([*map(to_modulo4, [1,6,3])], dtype=RingOfIntegersModulo)

    print(f"{a} + {b} = {a + b}")
    print(a == b)
    print(len(a))


if __name__ == "__main__":
    main()