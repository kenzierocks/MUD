__author__ = 'Kenzie Togami'
from abc import ABC, abstractmethod
import collections.abc as collabc


class Comparable(ABC):
    @abstractmethod
    def __cmp__(self, other):
        return None

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __hash__(self):
        return None  # unorderable by default

    def __lt__(self, other):
        return self.__cmp__(other) < 0

    def __gt__(self, other):
        return self.__cmp__(other) > 0

    def __le__(self, other):
        return self.__cmp__(other) <= 0

    def __ge__(self, other):
        return self.__cmp__(other) >= 0
