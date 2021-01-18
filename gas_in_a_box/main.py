import numpy as np

from .integrate import main as integrate
from .display import main as display
from .initialize import main as initialize


DISPLAY_SIZE = 900, 900


def main(
    steps=500,
    nr_of_particles=100,
    temperature=3,  # Kelvin (that's pretty cool!)
    run_integrator=True,
    dt=1e-3,
):

    y0 = initialize(nr_of_particles, temperature)

    if run_integrator:
        ys = integrate(nr_of_particles, y0, steps, dt)
        np.savetxt('./gas_in_a_box/out/ys.txt', ys)
    else:
        ys = np.loadtxt('./gas_in_a_box/out/ys.txt')

    display(ys, nr_of_particles, DISPLAY_SIZE)
