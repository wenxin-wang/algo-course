# Test your PY!
import numpy as np
import pandas as pd
from subprocess import check_output
import filecmp
import sys
import os


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
        print(N, times)
        for _ in range(0, times):
            res = [N, int(check_output(["./" + sort, str(N)]))]
            results.append(res)
    return pd.DataFrame(results, columns=(["N", sort])).groupby(["N"]).mean()


def run_all(sorts, name):
    results = [run(sort, runs) for sort, runs in sorts]
    df = pd.concat(results, axis=1)
    df.to_csv(os.path.join("instance", name))
    print(df)
    return df


def range_2(k):
    res = []
    for i in range(1, k+1):
        gap = 2**(i-1) // i
        top = 2**i
        res += [2**i - (j-1) * gap for j in range(i, 0, -1)]
    return res


def comp_radix(r):
    sorts = [("radix-sort-1", zip(range_2(r), [1000] * (r*(r+1)//2)))] + [
        ("radix-sort-%d" % k, zip(range_2(k), [1000] * (k*(k+1)//2)))
        for k in range(2, r+1)
    ]
    run_all(sorts, "radix-to-%d.csv" % r)


def comp_sorts():
    #short_runs = [(10, 500), (10**2, 500), (10**3, 500), (10**4, 500), (10**5, 100)]
    short_runs = []
    #insertion_runs = short_runs + [(4*10**5, 3), (6*10**5, 3)]
    #med_runs = short_runs + [(10**6, 100), (10**7, 100)]
    med_runs = short_runs + [(4*10**5, 3), (6*10**5, 3)]
    #med_runs = [(10**8, 3), (2*10**8, 3)]
    #long_runs = med_runs + [(10**9, 3)]
    long_runs = med_runs + []
    sorts = [
        ("stl-sort", long_runs),
        #("insertion", insertion_runs),
        ("shell-sort", med_runs),
        ("quick-sort", long_runs),
        ("merge-sort", long_runs),
        ("radix-sort", long_runs)
    ]
    run_all(sorts, "supper-time.csv")

#comp_radix(10)
#print(run("shell-sort", [(2*10**8, 1)]))
comp_sorts()
