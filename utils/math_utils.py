import numpy as np


def l2_norm(vec):
    return np.sqrt(sum([i**2 for i in vec]))
