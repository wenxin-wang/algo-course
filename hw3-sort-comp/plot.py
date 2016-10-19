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


print(read_csvs("short-time.csv", "2.csv"))
