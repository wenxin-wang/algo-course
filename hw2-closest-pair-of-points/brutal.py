import numpy as np
from solution import Solution
from exceptions import DataError


class Brutal(Solution):
    def solve(self):
        n = self.points.shape[0]
        if n < 2:
            raise DataError("At least two points are needed")
        m = None
        ia = -1
        ib = -1
        for i in range(0, n):
            a = self.points[i, :]
            for j in range(i + 1, n):
                d2 = self.dist2(a, self.points[j, :])
                if not m or d2 < m:
                    m = d2
                    ia = i
                    ib = j
        return (self.points[(ia, ib), :], m)

