from __future__ import print_function
import sys


def ins(i, l, L, prev):
    n = l[i]
    lo = 0
    hi = len(L)
    while lo < hi:
        mid = (lo + hi) // 2
        if l[L[mid]] > n:
            hi = mid
        else:
            lo = mid + 1
    if lo == len(L):
        L.append(i)
    else:
        L[lo] = i
    prev.append(L[lo - 1] if lo > 0 else -1)


def backtrack(l, L, prev):
    res = []
    if not L:
        return res
    i = L[-1]
    while i != -1:
        res.append(l[i])
        i = prev[i]
    res.reverse()
    return res


def longest_mon_inc_seq(l):
    L = []
    prev = []
    for i in range(0, len(l)):
        ins(i, l, L, prev)
    return len(L), backtrack(l, L, prev)


def usage():
    print("usage: %s n1 [n2 ...]" % sys.argv[0], file=sys.stderr)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit()
    length, seq = longest_mon_inc_seq([int(i) for i in sys.argv[1:]])
    print(length)
    print(" ".join([str(i) for i in seq]))
