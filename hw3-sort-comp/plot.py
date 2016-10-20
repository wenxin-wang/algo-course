import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import pandas as pd
import os


def read_csvs(*files):
    return pd.concat([pd.read_csv(
        os.path.join("instance", f), index_col=0) for f in files]).sort_index()


def plot_radix(r, ax, name):
    df = read_csvs("radix-to-%s.csv" % r)
    df.plot.line(ax=ax)
    ax.legend(loc="upper left", ncol=2, prop={'size': 6})
    ax.set_xlabel("n")
    ax.set_ylabel("Time (ms)")
    fig.savefig("../../figs/hw3/%s.pdf" % name, bbox_inches="tight")
    #plt.show()


def plot_comp(ax, name, **kwargs):
    df = read_csvs("all.csv")
    df.plot.line(ax=ax, **kwargs)
    ax.set_xlabel("n")
    ax.set_ylabel("Time (ms)")
    fig.savefig("../../figs/hw3/%s.pdf" % name, bbox_inches="tight")
    #plt.show()

#read_csvs("short-time.csv", "med-time.csv", "long-time.csv", "insertion-long.csv", "supper-time.csv").to_csv("instance/all.csv")
fig = plt.figure()
fig.set_size_inches(6 * 1.3, 6)
ax = fig.add_subplot(111)

#plot_comp(ax, "sorting-log", logx=True, logy=True)
#plot_comp(ax, "sorting")
plot_radix(20, ax, "radix-20")
#plot_radix(7, ax, "radix-7")
