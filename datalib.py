__author__ = 'Kenzie Togami'
from abc import ABC, abstractmethod
import collections.abc as collabc


def compare(a, b):
    return (a > b) - (a < b)


class Comparable(ABC):
    @abstractmethod
    def __cmp__(self, other):
        raise NotImplemented()

    def __eq__(self, other):
        return self.__cmp__(other) == 0

    def __ne__(self, other):
        return not self.__eq__(other)

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


class Comparator(Comparable):
    def __init__(self, item):
        self.item = item
        if hasattr(item, '__hash__'):
            self.__hash__ = lambda _: hash(item)
        if hasattr(item, '__cmp__'):
            self.__direct_cmp = item.__cmp__

    def __cmp__(self, other):
        if isinstance(other, Comparator):
            if hasattr(self, '__direct_cmp'):
                return self.__direct_cmp(other.item)
            else:
                return compare(self.item, other.item)
        raise NotImplemented()
