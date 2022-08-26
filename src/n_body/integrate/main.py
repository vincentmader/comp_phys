from tqdm import tqdm

import numpy as np
from numpy import cos, sin, pi, sqrt
from scipy.integrate import RK45

from .euler import main as euler
from .leapfrog import main as leapfrog
from .runge_kutta import main as runge_kutta
from utils.math_utils import l2_norm as norm
from utils.math_utils import transform_coords_pol2cart


G = 1
EPSILON = 1e-7  # "softer" potentials near singularity


def f(t, y):  # = dy/dt, y ^= state vector

    nr_of_bodies = int(len(y) / 6)

    ydot = []
    for i in range(nr_of_bodies):

        m_i, r_i = y[6*i], y[6*i+1]
        pos_i = np.array([y[6*i+2], y[6*i+3]])
        vel_i = np.array([y[6*i+4], y[6*i+5]])

        acc_i = np.array([0., 0.])
        for j in range(nr_of_bodies):
            if i == j:  # no self-interaction
                continue

            m_j, r_j = y[6*j], y[6*j+1]
            pos_j = np.array([y[6*j+2], y[6*j+3]])
            vel_j = np.array([y[6*j+4], y[6*j+5]])

            dr = pos_j - pos_i
            acc_i += G * m_j * dr / norm(dr + EPSILON)**3

        ydot += [0, 0] + list(vel_i) + list(acc_i)
    return ydot


def main(y0, nr_of_steps, y0_is_in_polar_coords=True):

    # set parameters for 4th order Runge-Kutta integration scheme
    first_step, max_step = 1e-2, 1e-2
    t0, t_bound = 0, max_step * nr_of_steps
    # get information about system
    nr_of_bodies = int(len(y0) / 6)  # 6 <- mass, radius, 2 pos/ & 2 vel
    if y0_is_in_polar_coords:
        new_y0 = []
        for i in range(nr_of_bodies):
            x, y = transform_coords_pol2cart(y0[6*i+2], y0[6*i+3])
            u, v = transform_coords_pol2cart(y0[6*i+4], y0[6*i+5])
            for i in [y0[6*i], y0[6*i+1], x, y, u, v]:
                new_y0.append(i)
        y0 = new_y0
    # setup Runge-Kutta integrator
    integrator = RK45(
        f, t0, y0, t_bound, first_step=first_step, max_step=max_step
    )
    # integrate
    ys = [y0]
    for _ in tqdm(range(nr_of_steps)):
        integrator.step()
        ys.append(integrator.y)

    return np.array(ys)
