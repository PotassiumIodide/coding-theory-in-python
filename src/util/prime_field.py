import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))

from src.finite_rings.modulo_m import RingOfIntegersModulo
from src.util.exceptions import NotPrimeError
from src.util.judge_prime import fermat_test, improved_fermat_test, miller_rabin_test

prime = int

prime_checker = [lambda x: True, fermat_test, improved_fermat_test, miller_rabin_test]

class PrimeField(RingOfIntegersModulo):
    def __init__(self, element: int, p: prime, prime_check_level: int=3):
        if prime_check_level not in range(len(prime_checker)):
            raise ValueError(f"Prime Check Level must be from 0 to {len(prime_checker)}!")
        if prime_check_level and not prime_checker[prime_check_level](p):
            raise NotPrimeError(p)
        return super().__init__(element, p)


def main():
    a = PrimeField(1, 4)
    b = PrimeField(1, 3)

    print(type(a+b))
    print(f"{a} + {b} = {a + b}")


if __name__ == "__main__":
    main()