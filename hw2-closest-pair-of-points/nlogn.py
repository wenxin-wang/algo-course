import numpy as np
import math

from solution import Solution
from brutal import Brutal
from exceptions import DataError


class NlogN(Solution):
    def __init__(self, points, xsorted=False):
        self.points = points if xsorted else self.sort(points)

    def solve(self):
        if self.points.shape[0] <= 4:
            return Brutal(self.points).solve()
        (ps0, D0), segs = self.split()
        yres = self.extract_x(segs, D0)
        if not yres:
            return (ps0, D0)
        ps1, D1 = yres
        if D0 < D1:
            return (ps0, D0)
        else:
            return (ps1, D1)

    def split(self):
        segs = np.array_split(self.points, 2)
        ps1, D1 = NlogN(segs[0], True).solve()
        ps2, D2 = NlogN(segs[1], True).solve()
        if D1 < D2:
            return (ps1, D1), segs
        else:
            return (ps2, D2), segs

    def extract_x(self, segs, D):
        seg0 = segs[0][::-1, ...]
        seg1 = segs[1]
        midx = (seg0[0, 0] + seg1[0, 0]) / 2
        d = math.sqrt(D)
        seg0 = self.near_d(seg0, midx, d)
        seg1 = self.near_d(seg1, midx, d)
        if seg0 is not None and seg1 is not None:
            return self.solve_y(np.vstack((seg0, seg1)))
        elif seg0:
            return self.solve_y(seg0)
        elif seg1:
            return self.solve_y(seg1)
        else:
            return None

    @classmethod
    def solve_y(cls, ps):
        ps = cls.sort(ps, x=False, copy=False)
        n = ps.shape[0]
        if n < 2:
            raise DataError("At least two points are needed")
        m = None
        ia = -1
        ib = -1
        for i in range(0, n):
            a = ps[i, :]
            for j in range(i + 1, min(i + 8, n)):
                d2 = cls.dist2(a, ps[j, :])
                if not m or d2 < m:
                    m = d2
                    ia = i
                    ib = j
        return (ps[(ia, ib), :], m)

    def near_d(self, seg, midx, d):
        res = []
        for p in seg:
            if abs(p[0] - midx) <= d:
                res.append(p)
            else:
                break
        if not res:
            return None
        elif len(res) == 1:
            return res[0]
        else:
            return np.vstack(res)

    @staticmethod
    def sort(points, x=True, copy=True):
        f = 'f0' if x else 'f1'
        if copy:
            return np.sort(
                points.view('float64,float64'), order=[f],
                axis=0).view(points.dtype)
        else:
            points.view('float64,float64').sort(
                order=[f], axis=0)
            return points
