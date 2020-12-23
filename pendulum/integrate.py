from tqdm import tqdm

import numpy as np
from numpy import cos, sin, pi
from scipy.integrate import RK45


# set parameters for 4th order Runge-Kutta integration scheme
g = .5
t0, t_bound = 0, 10000
first_step, max_step = .05, .05


def main(y0, m, L, steps):

    def f(t, y):

        th_1, th_2, p_1, p_2 = y[0], y[1], y[2], y[3]
        dth = th_1 - th_2

        dth_1 = 6/(m*L**2) * (2*p_1 - 3*cos(dth) * p_2) / (16 - 9*cos(dth)**2)
        dth_2 = 6/(m*L**2) * (8*p_2 - 3*cos(dth) * p_1) / (16 - 9*cos(dth)**2)
        dp_1 = -m * L**2 / 2 * (dth_1 * dth_2 * sin(dth) + 3*g/L*sin(th_1))
        dp_2 = -m * L**2 / 2 * (-dth_1 * dth_2 * sin(dth) + g/L*sin(th_2))

        return [dth_1, dth_2, dp_1, dp_2]

    integrator = RK45(
        f, t0, y0, t_bound, first_step=first_step, max_step=max_step
    )

    ys = []
    for _ in tqdm(range(steps)):
        y = integrator.step()
        ys.append(integrator.y)

    return ys
