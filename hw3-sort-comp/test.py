# Test your PY!
import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt
plt.style.use('ggplot')
import pandas as pd
from subprocess import check_output
import filecmp
import sys
import os


def gen(N, name):
    x = np.random.randint(2**31, size=N, dtype="int32")
    np.savetxt(name, x, fmt="%d")


def run(sorts, N, times, out=False):
    infile =  "i.txt"
    results = []
    for _ in range(0, times):
        gen(N, infile)
        res = [N]
        for s in sorts:
            cmd = ["../" + s, str(N), infile]
            if out:
                cmd.append(s + ".txt")
            res.append(int(check_output(cmd)))
        results.append(res)
        if out and len(sorts) > 1:
            for s in sorts[1:]:
                if not filecmp.cmp(sorts[0] + ".txt", s + ".txt"):
                    print("%d: %s != %s" % (N, sorts[0], s))
                    sys.exit()
    #return np.vstack(results) if times > 1 else np.array(results)
    return np.vstack(results)


os.chdir("instance")

#sorts = ["stl-sort", "insertion"]
sorts = ["stl-sort", "insertion", "quick-sort", "merge-sort"]
times = pd.DataFrame(np.vstack([
    run(sorts, n, 5, True) for n in
    [10]
    #[10, 10**2, 10**3]
    #[10, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 2*10**8]:
]), columns=(["N"] + sorts))

print(times)

