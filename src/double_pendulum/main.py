import json
import sys

import numpy as np
from numpy import pi

from .integrate import main as integrate
from .display import main as display
import utils

DISPLAY_SIZE = 900, 900

CHRISTMAS_MODE = False
# NOTE I used this "mode" to generate the reddit Chistmas post 
#   -> to try out: set to True


# set initial conditions
if CHRISTMAS_MODE:
    y0 = [pi * .75, pi * .75, 0, 0]  
else:
    y0 = [pi, .8*pi, 0, 0]

# set parameters of physical system
L, m = 1, 1


def main(
    steps=50000, 
    run_integrator=False,
    screenshot_mode=False,
):
    # run integrator, or load from file
    if run_integrator:
        ys = integrate(y0, m, L, steps)
        np.savetxt('./double_pendulum/out/ys.txt', ys)
    else:
        if CHRISTMAS_MODE:
            ys = np.loadtxt('./double_pendulum/out/ys_christmas.txt')
        else:
            ys = np.loadtxt('./double_pendulum/out/ys.txt')

    # display simulation using pygame
    display(
        ys, L,
        fading_tails=True,
        display_size=DISPLAY_SIZE,
        christmas_mode=CHRISTMAS_MODE,
        screenshot_mode=screenshot_mode,
    )


if __name__ == "__main__":
    main()
