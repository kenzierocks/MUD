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


class ReverseDict(collabc.MutableMapping, Comparable):
    def __init__(self, rdict=dict(), idict=dict()):
        self.rdict = rdict
        self.idict = idict
        self.__cache_dict = None

    def invert(self):
        if not self.__cache_dict:
            self.__cache_dict = ReverseDict(self.idict, self.rdict)
        return self.__cache_dict

    def __setitem__(self, key, value):
        if value in self.idict:
            raise ValueError("reverse mapping impossible")
        self.idict.__setitem__(value, key)
        return self.rdict.__setitem__(key, value)

    def __getitem__(self, item):
        return self.rdict.__getitem__(item)

    def __delitem__(self, key):
        self.idict.__delitem__(self.rdict.__getitem__(key))
        return self.rdict.__delitem__(key)

    def __iter__(self):
        return self.rdict.__iter__()

    def __len__(self):
        return self.rdict.__len__()

    def __cmp__(self, other):
        return isinstance(other, ReverseDict) and (self.rdict > other.rdict) - (self.rdict < other.rdict)
