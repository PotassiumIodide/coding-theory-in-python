import numpy as np
from collections.abc import Set
from typing import Iterator, List, Tuple

class VectorSet(Set):
    def __init__(self, vectors: List[np.ndarray]):
        """
        Instance
        Arguments:
        vectors: {List[numpy.ndarray]} - Vectors with the same dimension
        """
        self.__elements: List[np.ndarray] = [*map(np.array, list({*map(tuple, vectors)}))]

    def __str__(self) -> str:
        """
        String Expression of VectorSet
        Returns:
        {str} -- the string expression of VectorSet
        """
        return "".join(["{", ", ".join(map(str, self.__elements)), "}"])

    def __contains__(self, vector: np.ndarray) -> bool:
        """
        Judge whether the VectorSet contains a given vector.
        Argument:
        vector: {numpy.ndarray} - A vector to be judged whether VectorSet contains
        Returns:
        {bool} - True if the VectorSet contains the vector, False otherwise
        """
        return isinstance(vector, np.ndarray) and \
               tuple(vector) in map(tuple, self.__elements)

    def __iter__(self) -> Iterator[np.ndarray]:
        """
        Transform the type from VectorSet into Iterator[numpy.ndarray]
        Returns:
        {Iterator[numpy.ndarray]} - Iterator Expression of VectorSet
        """
        return iter(self.__elements)

    def __len__(self) -> int:
        """
        Return the cardinality of the VectorSet
        Returns:
        {int} - the number of vectors in the VectorSet
        """
        return len(self.__elements)  

    def __eq__(self, vs) -> bool:
        """
        Judge whether this VectorSet is equal to a given VectorSet.
        Argument:
        vs: {VectorSet} - A VectorSet to be judged whether it equals to this VectorSet
        Returns:
        {bool} - True when the two vectors are equal, False otherwise
        """
        return {*map(tuple, self.__elements)} == {*map(tuple, vs)}

    def __lt__(self, vs) -> bool:
        """
        Judge whether this VectorSet is the subset of a given VectorSet
        Argument:
        vs: {VectorSet} - A VectorSet to be judged whether it contains this VectorSet
        Returns:
        {bool} - True if this is the subset of a given VectorSet, False otherwise.
        """
        vt = map(tuple, vs)
        for v in map(tuple, self.__elements):
            if v not in map(tuple, vt):
                return False
        return True

    def __gt__(self, vs) -> bool:
        """
        Judge whether this VectorSet is the superset of a given VectorSet
        Argument:
        vs: {VectorSet} - A VectorSet to be judged whether it is contained this VectorSet
        Returns:
        {bool} - True if this is the superset of a given VectorSet, False otherwise.
        """
        return vs <= self

    def __add__(self, vs):
        """
        The Union of this VectorSet and a given VectorSet
        (Based on the idea of coproduct in Category Theory)
        Argument:
        vs: {VectorSet} - A VectorSet to be added to this VectorSet
        Returns:
        {VectorSet} - The union of this VectorSet and a given VectorSet
        """
        ret = self.__elements
        for v in map(tuple, vs):
            if v not in map(tuple, ret):
                ret.append(np.array(v))
        return ret

    def __sub__(self, vs):
        """
        The difference set of this VectorSet by a given VectorSet
        Argument:
        vs: {VectorSet} - The set of removed vectors from this VectorSet
        Returns:
        {VectorSet} - The difference set of this VectorSet by a given VectorSet        
        """
        return [v for v in self.__elements if tuple(v) not in map(tuple, vs)]

    def __mul__(self, vs) -> List[Tuple[np.ndarray, np.ndarray]]:
        """
        Return the direct product of this VectorSet and a given VectorSet
        Argument:
        vs: {VectorSet} - A VectorSet to be directly producted to this VectorSet
        Returns:
        {List[Tuple[numpy.ndarray, numpy.ndarray]]}
        """
        return sum([[*map(lambda u: (u, v), self.__elements)] for v in vs], [])

    def __and__(self, vs):
        """
        Return the intersection of this VectorSet and a given VectorSet
        Argument:
        vs: {VectorSet} - A VectorSet to be intersected by this VectorSet
        Returns:
        {VectorSet} - The intersection of the two VectorSets
        """
        smaller, larger = (self.__elements, vs) if len(self.__elements) <= len(vs) else (vs, self.__elements)
        return [v for v in smaller if tuple(v) in map(tuple, larger)]

    def __or__(self, vs):
        """
        Return the union of this VectorSet and a given VectorSet
        Argument:
        vs: {VectorSet} - A VectorSet to be taken the union with this vector
        Returns:
        {VectorSet} - The union of this VectorSet and a given VectorSet
        """
        return self + vs


def main():
    S = VectorSet([np.array([1,2,3]), np.array([4,5,6]), np.array([7,8,9])])
    T = VectorSet([np.array([1,2,3]), np.array([7,7,9])])
    print(np.array([1,2,3]) in S)
    print(S <= T)
    print(S - T)
    print(S * S)
    print(S & T)
    print(S + T)


if __name__ == "__main__":
    main()