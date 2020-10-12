class InverseNotExistsError(Exception):
    def __init__(self, element):
        self.__element = element

    def __str__(self):
        return f"The element {self.__element} has no inverse element!"


class NotPrimeError(Exception):
    def __init__(self, integer: int):
        self.__integer = integer

    def __str__(self):
        return f"The integer {self.__integer} is not a prime!"