import numpy as np
from PIL import Image
import sys
import random
from collections import deque
import time


def usage():
    print("%s infile outfile" % sys.argv[0])


def cost(img):
    m, n, _ = img.shape
    t = np.absolute(img[:-1, :, :] - img[1:, :, :]).sum(axis=2, dtype='uint32')
    c = np.concatenate(
        (t, np.zeros((1, n), dtype='uint32')), axis=0) + np.concatenate(
            (np.zeros((1, n), dtype='uint32'), t), axis=0)
    t = np.absolute(img[:, :-1, :] - img[:, 1:, :]).sum(axis=2, dtype='uint32')
    c += np.concatenate(
        (t, np.zeros((m, 1), dtype='uint32')), axis=1) + np.concatenate(
            (np.zeros((m, 1), dtype='uint32'), t), axis=1)
    div = np.full(c.shape, 4, dtype='uint32')
    div[0, :] = 3
    div[-1, :] = 3
    div[:, 0] = 3
    div[:, 1] = 3
    div[0, 0] = 2
    div[-1, 0] = 2
    div[0, -1] = 2
    div[-1, -1] = 2
    return c // div


def rand_least(l):
    idx = [0]
    small = l[0]
    for i in range(1, len(l)):
        if l[i] < small:
            small = l[i]
            idx = [i]
        elif l[i] == small:
            idx.append(i)
    return random.choice(idx)


def least_cost_r(r, b):
    n = len(r)
    if n <= 1:
        return r[0]
    small = r[0]
    idx = 0
    l = deque(r[0:2])
    b[0] = rand_least(l)
    l.append(r[2])
    b[1] = rand_least(l) - 1
    for i in range(2, n-1):
        l.popleft()
        l.append(r[i+1])
        b[i] = rand_least(l) - 1
    l.popleft()
    b[n-1] = rand_least(l) - 1


def curve_r(img, best):
    _s = time.clock()
    c = cost(img)
    print("Cost", time.clock() - _s)
    m, n = c.shape
    _s = time.clock()
    for i in range(1, m):
        least_cost_r(c[i - 1, :], best[i, :])
        for j in range(1, n):
            c[i, j] += c[i - 1, j + best[i, j]]
    print("DP", time.clock() - _s)
    _s = time.clock()
    keep = np.ones(img.shape, dtype=bool)
    idx = c[-1, :].argmin()
    keep[-1, idx, :] = False
    for i in range(m - 1, 0, -1):
        idx += best[i, idx]
        keep[i - 1, idx, :] = False
    print("backtrack", time.clock() - _s)
    return img[keep].reshape(m, n-1, 3)


def seam_curing(img):
    m, n, _ = img.shape
    if m > n:
        mi = m // n
        ni = 1
        run = n // 2
    else:
        mi = 1
        ni = n // m
        run = m // 2
    best = np.zeros((max(m, n), max(m, n)), dtype='int8')
    run = 10
    ni = 1
    mi = 1
    for _ in range(0, run):
        for _ in range(0, ni):
            _s = time.clock()
            img = curve_r(img, best)
            print("n", time.clock() - _s)
        _s = time.clock()
        img = img.transpose(1, 0, 2)
        print("T", time.clock() - _s)
        for _ in range(0, mi):
            _s = time.clock()
            img = curve_r(img, best)
            print("m", time.clock() - _s)
        _s = time.clock()
        img = img.transpose(1, 0, 2)
        print("T", time.clock() - _s)
    return img


def main():
    if len(sys.argv) != 3:
        usage()
        sys.exit()
    img = np.array(Image.open(sys.argv[1]))
    img = seam_curing(img)
    Image.fromarray(img, "RGB").save(sys.argv[2])


if __name__ == "__main__":
    main()
