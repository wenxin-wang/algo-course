import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt

class Solution:
    def __init__(self, points):
        self.points = points

    @staticmethod
    def dist2(a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
