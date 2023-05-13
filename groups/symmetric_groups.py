from example_code.groups import Group
import numpy as np

class SymmetricGroup(Group):

    symbol = "S"
  
    def _validate(self, value):
        value = np.asarray(value)
        if np.size(value) == 1 or not (sorted(value) == [n for n in range(0, self.n)]):
            raise ValueError("Not a valid permutation")

    def operation(self, a, b):
        return a[b]

