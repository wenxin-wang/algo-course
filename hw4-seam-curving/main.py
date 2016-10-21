import numpy as np
from PIL import Image
import sys
import random
import time

import numpy as np
import matplotlib as mpl
mpl.use('TkAgg')
import matplotlib.pyplot as plt


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


def rand_least(r, i, j):
    idx = [0]
    small = r[i]
    for t in range(i+1, j+1):
        if r[t] < small:
            small = r[t]
            idx = [t-i]
        elif r[t] == small:
            idx.append(t-i)
    return random.choice(idx)


def least_cost_r(r, b):
    n = len(r)
    if n <= 1:
        return r[0]
    b[0] = rand_least(r, 0, 1)
    b[1] = rand_least(r, 0, 2) - 1
    for i in range(2, n - 1):
        b[i] = rand_least(r, i - 1, i + 1) - 1
    b[n - 1] = rand_least(r, n - 2, n - 1) - 1


def curve_r(img, best):
    c = cost(img)
    #plt.imshow(c, cmap="binary")
    #plt.show()
    m, n = c.shape
    #_s = time.clock()
    for i in range(1, m):
        least_cost_r(c[i - 1, :], best[i, :])
        for j in range(0, n):
            c[i, j] += c[i - 1, j + best[i, j]]
    #print("DP", time.clock() - _s)
    keep = np.ones(img.shape, dtype=bool)
    idx = c[-1, :].argmin()
    keep[-1, idx, :] = False
    for i in range(m - 1, 0, -1):
        idx += best[i, idx]
        keep[i - 1, idx, :] = False
    return img[keep].reshape(m, n-1, 3)


def seam_curing(img):
    m, n, _ = img.shape
    best = np.zeros((max(m, n), max(m, n)), dtype='int8')
    for _ in range(0, n // 2):
        img = curve_r(img, best)
    img = img.transpose(1, 0, 2)
    for _ in range(0, m // 2):
        img = curve_r(img, best)
    img = img.transpose(1, 0, 2)
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
