import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
import math
import time

from brutal import Brutal
from nlogn import NlogN
from exceptions import InputDataError


class Factory:
    XLIM = 100
    YLIM = 100

    def __init__(self, cli):
        self.cli = cli
        self.points = None

    def solve(self):
        if self.cli.brutal:
            self.show_result("Brutal Force", self._solve(Brutal(self.get_points())))
        if self.cli.nlogn:
            self.show_result("NlogN",  self._solve(NlogN(self.get_points())))
        plt.show()


    def test(self):
        N = self.cli.test
        t0 = 0
        t1 = 0
        if self.cli.brutal:
            for i in range(0, N):
                _ , dt0 = self._solve(Brutal(self.get_points()))
                t0 += dt0
            print("Brutal Force: %f" % (t0 / N))
        if self.cli.nlogn:
            for i in range(0, N):
                _ , dt1 = self._solve(NlogN(self.get_points()))
                t1 += dt1
            print("NlogN: %f" % (t1 / N))
        return t0 / N, t1 / N


    def compare(self):
        N = self.cli.compare
        t0 = 0
        t1 = 0
        err = 0
        for i in range(0, N):
            (_, d0), dt0 = self._solve(Brutal(self.get_points()))
            t0 += dt0
            (_, d1), dt1 = self._solve(NlogN(self.get_points()))
            t1 += dt1
            if d0 != d1:
                err += 1
        print("Errors: %d\nBrutal Force: %f\nNlogN: %f" % (err, t0 / N, t1 / N))
        return t0 / N, t1 / N

    def _solve(self, sol):
        start = time.clock()
        res = sol.solve()
        end = time.clock()
        elapse = end - start
        return (res, elapse)

    def get_points(self):
        if self.points is not None:
            return self.points
        return self._get_points()

    def _get_points(self):
        if self.cli.read:
            self.points = np.loadtxt(self.cli.read, self.points)
            if self.points.shape[1] != 2:
                raise InputDataError("Input data file should have 2 columns of floating point numbers")
        elif self.cli.generate:
            self.points = np.random.rand(self.cli.generate, 2)
            self.points[:, 0] *= self.XLIM
            self.points[:, 1] *= self.YLIM
        if self.cli.edit:
            self.points = self.collect_points()
        if self.cli.write:
            np.savetxt(self.cli.write, self.points)
        return self.points

    def collect_points(self):
        fig, (l, ) = self._plot([], []) if self.points is None else self.plot()
        _points = [np.empty([0, 2])] if self.points is None else [np.copy(self.points)]

        def onclick(event):
            if not event.xdata or not event.ydata:
                return
            points = np.vstack((_points[0], [event.xdata, event.ydata]))
            _points[0] = points
            l.set_xdata(points[:, 0])
            l.set_ydata(points[:, 1])
            plt.draw()

        cid = fig.canvas.mpl_connect('button_press_event', onclick)
        plt.show()
        return _points[0]

    def show_result(self, name, res):
        (ps, d2), elapse = res
        print(name + ": %s %s %f" % (ps[0, :], ps[1, :], math.sqrt(d2)))
        print("Elapse: %f" % elapse)
        if self.cli.show:
            self.plot(ps)

    def plot(self, ps=None):
        return self._plot(self.points[:, 0], self.points[:, 1], ps)

    @classmethod
    def _plot(cls, xs, ys, ps=None):
        fig = plt.figure()
        ax = fig.add_subplot(111, aspect=1)
        res = ax.plot(xs, ys, "o")
        if ps is not None:
            ax.plot(ps[:, 0], ps[:, 1], "o", color="red")
        ax.set_xlim([0, cls.XLIM])
        ax.set_ylim([0, cls.YLIM])
        return fig, res
