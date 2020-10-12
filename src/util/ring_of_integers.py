import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

import numpy as np
from numbers import Number
from typing import Generator, Union

from src.util.exceptions import InverseNotExistsError

class RingOfIntegersModulo(Number):
    def __init__(self, element: Union[int, np.ndarray], modulo: int):
        self.__element = np.mod(element, modulo)
        self.__modulo = modulo
        self.__inv = RingOfIntegersModulo.find_inv(element, modulo)

    def __str__(self) -> str:
        return str(self.__element)

    def __add__(self, y):
        if self.__modulo != y.__modulo:
            raise TypeError("Their modulo must match!")
        return RingOfIntegersModulo(self.__element + y.__element, self.__modulo)

    def __sub__(self, y):
        if self.__modulo != y.__modulo:
            raise TypeError("Their modulo must match!")
        return RingOfIntegersModulo(self.__element - y.__element, self.__modulo)

    def __mul__(self, y):
        if self.__modulo != y.__modulo:
            raise TypeError("Their modulo must match!")
        return RingOfIntegersModulo(self.__element * y.__element, self.__modulo)

    def __neg__(self):
        return RingOfIntegersModulo(self.__modulo - self.__element, self.__modulo)

    def inv(self):
        if self.__inv:
            return RingOfIntegersModulo(self.__inv, self.__modulo)
        raise InverseNotExistsError(self.__element)

    def __truediv__(self, y):
        return self * y.inv()

    def __eq__(self, y):
        return self.__element == y.__element and self.__modulo == y.__modulo

    def __neq__(self, y):
        return not self == y

    @staticmethod
    def find_inv(element: Union[int, np.ndarray], modulo: int):
        for inv in range(modulo):
            if (element * inv) % modulo == 1:
                return inv
        return None

    @staticmethod
    def all_inv_generator(modulo: int) -> Generator[Union[int, None], None, None]:
        for a in range(modulo):
            yield RingOfIntegersModulo.find_inv(a, modulo)


def main():
    a = RingOfIntegersModulo(1, 4)
    b = RingOfIntegersModulo(2, 4)

    print(f"{a} + {b} = {a + b}")
    print(f"{a} - {b} = {a - b}")
    print(f"{a} * {b} = {a * b}")
    print(f"{b} / {a} = {b / a}")
    #print(a / b)
    print(list(RingOfIntegersModulo.all_inv_generator(4)))


if __name__ == "__main__":
    main()