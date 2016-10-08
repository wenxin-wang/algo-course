import math
import time
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import pandas as pd

sqrt5 = np.float64(math.sqrt(5))
ph0 = np.float64((1 - sqrt5) / 2)
ph1 = np.float64((1 + sqrt5) / 2)


def numeric(n):
    return (ph1**n - ph0**n) / sqrt5


def brutal(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return brutal(n - 1) + brutal(n - 2)


def mat(n):
    # a b | j k
    # c d | l m
    def acc(n, a, b, c, d, j, k, l, m):
        if n % 2 == 1:
            j1 = a * j + b * l
            k1 = a * k + b * m
            l1 = c * j + d * l
            m1 = c * k + d * m
            j = j1
            k = k1
            l = l1
            m = m1
            n -= 1
        if n == 0:
            return l
        return acc(n // 2, a**2 + b * c, a * b + b * d, a * c + b * d,
                   b * c + d**2, j, k, l, m)
    return acc(n, *np.float64([1, 1, 1, 0, 1, 0, 0, 1]))


def timeit(f, n):
    start = time.clock()
    res = f(n)
    end = time.clock()
    return res, end - start


nv = np.vectorize(lambda n: timeit(numeric, n))
bv = np.vectorize(lambda n: timeit(brutal, n))
mv = np.vectorize(lambda n: timeit(mat, n))

ox = np.array(range(0, 1000))
bx = np.array(range(0, 38))

def run(f, n, N):
    times = []
    for i in range(0, N):
        res, time = f(n)
        times.append(time)
    return pd.DataFrame(data={"value": res, "time": np.mean(times, axis=0)}, index=n)


pn = pd.Panel(data={"numeric": run(nv, ox, 10),
                    "matrix": run(mv, ox, 10),
                    "brutal": run(bv, bx, 10)
}).transpose(2, 1, 0)
fig = plt.figure()
fig.set_size_inches(6 * 1.3, 6)
ax = fig.add_subplot(111)
pn.loc["time", :, :].plot.line(ax=ax, marker=".")
ax.set_xlabel("n")
ax.set_ylabel("Time (s)")
fig.savefig("../../figs/hw2/fib.pdf", bbox_inches="tight")
ax.clear()
pn.loc["time", range(0, 15), :].plot.line(ax=ax, marker=".")
ax.set_xlabel("n")
ax.set_ylabel("Time (s)")
fig.savefig("../../figs/hw2/fib-nm.pdf", bbox_inches="tight")
ax.clear()
pn.loc["value", :, :].plot.line(ax=ax, marker=".")
ax.set_xlabel("n")
ax.set_ylabel("Value")
fig.savefig("../../figs/hw2/fib-val.pdf", bbox_inches="tight")
#np.savetxt("numeric.txt", , fmt="%d %.18ef %.18ef")
