import numpy as np

G = 1


def kepler_velocity(r, M=1):
    return np.sqrt(G * M / abs(r))
