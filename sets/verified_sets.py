from collections.abc import Iterable
from typing import Any
from numbers import Integral

class VerifiedSet(set):
    
    def __init__(self, value):
        super().__init__(value)
        self._verify(value)
        
    def _verify(self, value):
        raise NotImplementedError
    
    def add(self, value):
        self._verify(value)
        super().add(value)
        
    def update(self, other):
        for value in other:
            self._verify(value)
        super().update(other)
    
    def symmetric_difference_update(self, other):
        for value in other:
            self._verify(value)
        super().symmetric_difference_update(other)
        
    def union(self, *others):
        verified_others = [type(self)(other) for other in others]
        ans = super().union(*verified_others)
        return type(self)(ans)

    def intersection(self, *others):
        verified_others = [type(self)(other) for other in others]
        ans = super().intersection(*verified_others)
        return type(self)(ans)

    def difference(self, *others):
        verified_others = [type(self)(other) for other in others]
        ans = super().difference(*verified_others)
        return type(self)(ans)

    def symmetric_difference(self, other):
        verified_other = type(self)(other)
        ans = super().symmetric_difference(verified_other)
        return type(self)(ans)

    def copy(self):
        ans = super().copy()
        return type(self)(ans)


class UniquenessError(KeyError):
    pass


class IntSet(VerifiedSet):
    
    def _verify(self, value):
        if isinstance(value, Integral):
            return True
        elif isinstance(value, Iterable):
            for item in value:
                if not isinstance(item, Integral):
                    raise TypeError(f"IntSet expected an iterable of integers, got an iterable with {type(item).__name__} at element {value.index(item)}")
            return True
        else:
            raise TypeError(f"IntSet expected an integer or iterable of integers, got a {type(value).__name__}")


        

class UniqueSet(VerifiedSet):
    
    def _verify(self, value):
        if value in self:
            raise UniquenessError(f"{value} is already in the set.")