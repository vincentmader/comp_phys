from tqdm import tqdm

import numpy as np
from numpy import cos, sin, pi, sqrt
from scipy.integrate import RK45

from .euler import main as euler
from .leapfrog import main as leapfrog
from .runge_kutta import main as runge_kutta
from utils.math_utils import l2_norm as norm


G = 1


def main(y0, nr_of_steps):

    # set parameters for 4th order Runge-Kutta integration scheme
    first_step, max_step = 1e-2, 1e-2
    t0, t_bound = 0, max_step * nr_of_steps
    EPSILON = 0  # 1e-2  # "softer" potentials near singularity

    nr_of_bodies = int(len(y0) / 8)  # 8 <- mass, radius, 3 pos/ & 3 vel

    def f(t, y):  # = dy/dt, y ^= state vector

        ydot = []
        for i in range(nr_of_bodies):

            m_i, r_i = y[8*i], y[8*i+1]
            pos_i = np.array([y[8*i+2], y[8*i+3], y[8*i+4]])
            vel_i = np.array([y[8*i+5], y[8*i+6], y[8*i+7]])

            acc_i = 0
            for j in range(nr_of_bodies):
                if i == j:  # no self-interaction
                    continue

                m_j, r_j = y[8*j], y[8*j+1]
                pos_j = np.array([y[8*j+2], y[8*j+3], y[8*j+4]])
                vel_j = np.array([y[8*j+5], y[8*j+6], y[8*j+7]])

                dr = pos_j-pos_i
                acc_i += G * m_j * dr / norm(dr + EPSILON)**3

            ydot += [0, 0] + list(vel_i) + list(acc_i)
        return ydot

    integrator = RK45(
        f, t0, y0, t_bound,
        first_step=first_step, max_step=max_step
    )

    ys = [y0]
    for _ in tqdm(range(nr_of_steps)):
        integrator.step()
        ys.append(integrator.y)

    return np.array(ys)
