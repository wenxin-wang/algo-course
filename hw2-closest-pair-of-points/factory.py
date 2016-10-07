import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt


class Factory:
    XLIM = 100
    YLIM = 100

    def __init__(self, cli):
        self.cli = cli
        self.points = None

    def get_points(self):
        if self.points:
            return self.points
        if self.cli.read:
            self.points = np.loadtxt(self.cli.read, self.points)
        elif self.cli.generate:
            self.points = np.random.rand(self.cli.generate, 2)
            self.points[:, 0] *= self.XLIM
            self.points[:, 1] *= self.YLIM
        elif self.cli.interactive:
            self.points = self.collect_points()
        if self.cli.write:
            np.savetxt(self.cli.write, self.points)
        return self.points

    def collect_points(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, aspect=1)
        ax.set_xlim([0, self.XLIM])
        ax.set_ylim([0, self.YLIM])
        l, = ax.plot([], [], "o")
        _points = [np.empty([0, 2])]
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


    def plot(self):
        fig = plt.figure()
        ax = fig.add_subplot(111, aspect=1)
        ax.plot(self.points[:, 0], self.points[:, 1], "o")
        ax.set_xlim([0, self.XLIM])
        ax.set_ylim([0, self.YLIM])
        plt.show()
