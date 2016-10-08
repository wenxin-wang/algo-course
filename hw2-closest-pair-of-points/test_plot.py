import numpy as np
import matplotlib as mpl
mpl.use('pdf')
#mpl.use('TkAgg')
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import pandas as pd
from scipy.optimize import curve_fit


def read_stat(f, name):
    return pd.read_table(f, delim_whitespace=True, header=None, index_col=0,
                         names=["N", name])


def pg(x, y, *args, **kwargs):
    z = np.polyfit(x, y, *args, **kwargs)
    res = float(0)
    line = "y = "
    for i in range(0, len(z)):
        res *= x
        res += z[i]
        if i == len(z) - 1:
            line += "%.2e" % z[i]
        elif i == len(z) - 2:
            line += "%.2e x + " % z[i]
        else:
            line += "%.2e x^%d + " % (z[i], len(z) - i - 1)
    return res, line

def cf(x, y):
    def nln(x, a, b):
        return a * x * np.log(x) + b
    popt, = curve_fit(cf, x, y)
    return nln(x, *popt), "%.2e x lnx + %.2e" % popt

brutal = read_stat("brutal.txt", "brutal")
nlogn = read_stat("nlogn.txt", "nlogn")
df = pd.concat([brutal, nlogn], axis=1)
#brutal_rg, bline = pg(brutal.index.values, brutal, 3)
#nlogn_rg, line = pg(df.index.values, df["nlogn"], 1)
#print(bline, brutal_rg)
df.index = df.index.map(str)

fig = plt.figure()
ax = fig.add_subplot(111, aspect=1/20)
#ax = fig.add_subplot(111)
df.plot.line(ax=ax, marker=".")
#ax.plot(df.index.values, nlogn_rg)
#ax.plot(brutal.index.map(str), brutal_rg)
ax.set_xlabel("Number of Points")
ax.set_ylabel("Time (s)")
ax.set_yscale("log", basey=10)
#plt.show()
fig.savefig("../../figs/hw2/pairs-time.pdf", bbox_inches="tight")
