# Test your PY!
import numpy as np
import pandas as pd
from subprocess import check_output
import filecmp
import sys
import os
from collections import OrderedDict


def gen(N, name):
    x = np.random.randint(2**31, size=N, dtype="int32")
    np.savetxt(name, x, fmt="%d")


def test(sorts, N, times, generate=False, out=False):
    if generate:
        infile = os.path.join("instance", "i.txt")
    else:
        out = False
    results = []
    for _ in range(0, times):
        if generate:
            gen(N, infile)
        res = [N]
        for s in sorts:
            cmd = ["./" + s, str(N)]
            if generate:
                cmd.append(infile)
            if out:
                cmd.append(os.path.join("instance", s + ".txt"))
            res.append(int(check_output(cmd)))
        results.append(res)
        if out and len(sorts) > 1:
            for s in sorts[1:]:
                if not filecmp.cmp(
                        os.path.join("instance", sorts[0] + ".txt"),
                        os.path.join("instance", s + ".txt")):
                    print("%d: %s != %s" % (N, sorts[0], s))
                    sys.exit()
    #return np.vstack(results) if times > 1 else np.array(results)
    return np.vstack(results)

#sorts = ["stl-sort", "radix-sort"]
#sorts = ["stl-sort", "radix-sort", "radix-sort-msbf"]
#sorts = ["stl-sort", "insertion", "quick-sort", "merge-sort", "shell-sort",
#         "radix-sort"]
#times = pd.DataFrame(
#    np.vstack([
#        test(sorts, n, 10)
#        for n in [10, 10**2, 10**3]
#        #[10, 10**2, 10**3, 10**4, 10**5, 10**6, 10**7, 10**8, 2*10**8]:
#    ]),
#    columns=(["N"] + sorts))
#
#print(times)


def run(sort, runs):
    results = []
    print(sort)
    for N, times in runs:
        for _ in range(0, times):
            res = [N, int(check_output(["./" + sort, str(N)]))]
            print(res)
            results.append(res)
    return pd.DataFrame(results, columns=(["N", sort])).groupby(["N"]).mean()


def run_all(sorts, name):
    results = [run(sort, runs) for sort, runs in sorts.items()]
    df = pd.concat(results, axis=1)
    df.to_csv(os.path.join("instance", name))
    print(df)
    return df


long_runs = [(10, 10), (100, 10)]
short_runs = [(10, 10), (100, 10)]
#middle_runs = [(10, 10), (100, 10)]
ts = ["stl-sort", "insertion", "quick-sort", "merge-sort", "shell-sort",
      "radix-sort"]
sorts = [
    ("stl-sort", long_runs),
    ("insertion", short_runs),
    ("quick-sort", long_runs),
    ("merge-sort", long_runs),
    ("radix-sort", long_runs)]
res = run_all(OrderedDict(sorts), "short-time.csv")
