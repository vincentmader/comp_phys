import numpy as np
from numpy import sqrt

from .integrate import main as integrate
from .display import main as display


M, G = 1, 1


def kepler_velocity(r):
    return np.sqrt(G * M / r)


y0 = [
    M,    1,   0, 0, 0,   0, 0, 0,  # mass, radius, 3 pos. & 3 vel. values
    1e-6, 1,   0.25, 0, 0,   0, kepler_velocity(0.25), 0,
    1e-6, 1,   1, 0, 0,   0, 1, 0,
    1e-6, 1,   1.25, 0, 0,   0, kepler_velocity(1.25), 0,
    1e-6, 1,   1.5, 0, 0,   0, kepler_velocity(1.5), 0,
    1e-6, 1,   1.75, 0, 0,   0, kepler_velocity(1.75), 0,
    1e-6, 1,   2, 0, 0,   0, kepler_velocity(2), 0,
    1e-6, 1,   2, 1, 0,   0, kepler_velocity(4), 0,

    # 1e-5, 1,   sqrt(2), 0, 0,   0, kepler_velocity(10), 0,
    # 1e-5, 1,   -sqrt(2), 0, 0,   0, -kepler_velocity(10), 0,
    # 1e-5, 1,   0, sqrt(2), 0,   -kepler_velocity(10), 0, 0,
    # 1e-5, 1,   0, -sqrt(2), 0,   kepler_velocity(10), 0, 0,

    # 1e-5, 1,   1, 1, 0,   0,  kepler_velocity(10), 0,
    # 1e-5, 1,   -1, 1, 0,   0,  -kepler_velocity(10), 0,
    # 1e-5, 1,   1, -1, 0,    kepler_velocity(10), 0, 0,
    # 1e-5, 1,   -1, -1, 0,     kepler_velocity(10), 0, 0,
]


def main(nr_of_steps=1000, run_integrator=True):

    if run_integrator:
        ys = integrate(y0, nr_of_steps)
        np.savetxt('./n_body/out/ys.txt', ys)
    else:
        ys = np.loadtxt('./n_body/out/ys.txt')

    display(ys)
