import numpy as np
from numpy import sqrt

from .integrate import main as integrate
from .display import main as display
from .display import pyplot as display_via_pyplot


M, G = 1, 1


def kepler_velocity(r, m=M):
    return np.sqrt(G * m / abs(r))


v_K = kepler_velocity


y0 = [
    M,    1,   0, 0, 0,   0, 0, 0,  # mass, radius, 3 pos. & 3 vel. values

    # 1e-3, 1,   2, 0, 0,   0, v_K(2), 0,

    # 1e-12, 1,
    # 2+2e-2, 0, 0,
    # 0, kepler_velocity(2) + kepler_velocity(2e-2, m=1e-3), 0,

    # 1e-6, 1,   0.25, 0, 0,   0, kepler_velocity(0.25), 0,
    # 1e-6, 1,   .2, 0, 0,   0, v_K(.2), 0,
    1e-6, 1,   -.4, 0, 0,   0, -v_K(.4), 0,
    1e-6, 1,   .7, 0, 0,   0, v_K(.7), 0,
    # 1e-6, 1,   -.6, 0, 0,   0, -v_K(.6), 0,
    1e-6, 1,   -1, 0, 0,   0, -v_K(1), 0,
    1e-6, 1,   -1.3, 0, 0,   0, -v_K(1.3), 0,
    1e-6, 1,   1.5, 0, 0,   0, v_K(1.4), 0,
    1e-6, 1,   -1.8, 0, 0,   0, -v_K(1.8), 0,
    # 1e-6, 1,   -1.25, 0, 0,   0, -kepler_velocity(3.25), 0,
    # 1e-6, 1,   1.25, 0, 0,   0, kepler_velocity(1.25), 0,
    # 1e-6, 1,   -1.6, 0, 0,   0, -kepler_velocity(1.5), 0,
    # 1e-6, 1,   -1.5, 0, 0,   0, -kepler_velocity(4), 0,
    # 1e-6, 1,   1.75, 0, 0,   0, kepler_velocity(5.75), 0,
    # 1e-6, 1,   2, 0, 0,   0, kepler_velocity(2), 0,
    # 1e-6, 1,   2, 1, 0,   0, kepler_velocity(4), 0,

    # 1e-5, 1,   sqrt(2), 0, 0,   0, kepler_velocity(10), 0,
    # 1e-5, 1,   -sqrt(2), 0, 0,   0, -kepler_velocity(10), 0,
    # 1e-5, 1,   0, sqrt(2), 0,   -kepler_velocity(10), 0, 0,
    # 1e-5, 1,   0, -sqrt(2), 0,   kepler_velocity(10), 0, 0,

    # 1e-5, 1,   1, 1, 0,   0,  kepler_velocity(10), 0,
    # 1e-5, 1,   -1, 1, 0,   0,  -kepler_velocity(10), 0,
    # 1e-5, 1,   1, -1, 0,    kepler_velocity(10), 0, 0,
    # 1e-5, 1,   -1, -1, 0,     kepler_velocity(10), 0, 0,
]


def main(nr_of_steps=2000, run_integrator=True, in_screenshot_mode=False):

    if run_integrator:
        ys = integrate(y0, nr_of_steps)
        np.savetxt('./n_body/out/ys.txt', ys)
    else:
        ys = np.loadtxt('./n_body/out/ys.txt')
        np.savetxt('./n_body/out/ys_2.txt', ys)

    display_via_pyplot(ys)
    display(ys, in_screenshot_mode=in_screenshot_mode)
