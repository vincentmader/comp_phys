import json
import sys

import numpy as np
from numpy import pi

from .integrate import main as integrate
from .display import main as display
import utils


# set initial conditions
y0 = [pi, .8*pi, 0, 0]
# y0 = [pi * .75, pi * .75, 0, 0]  # used for "christmas mode"

# set parameters of physical system
L, m = 1, 1


def main(steps=50000, run_integrator=False, in_christmas_mode=False):

    # get simulation output data
    if run_integrator:
        ys = integrate(y0, m, L, steps)
        np.savetxt('.double_pendulum/out/ys.txt', ys)
    else:
        if in_christmas_mode:
            ys = np.loadtxt('./double_pendulum/out/ys_christmas.txt')
        else:
            ys = np.loadtxt('./double_pendulum/out/ys.txt')

    # display simulation using pygame
    display(
        ys, L,
        in_christmas_mode=in_christmas_mode,
        fading_tails=True,
    )


if __name__ == "__main__":
    main()
