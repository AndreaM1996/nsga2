import math
import numpy as np


def g1(x):
    n = len(x)
    x = np.array(x)
    return 1 + 9 / (n - 1) * (x.sum() - x[0])


def f_values(x):
    f1 = x[0]

    g = g1(x)
    f2 = g * (1 - math.sqrt(f1 / g))

    return f1, f2

