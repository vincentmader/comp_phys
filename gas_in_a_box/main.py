import numpy as np

from .integrate import main as integrate
from .display import main as display
from .initialize import main as initialize


DISPLAY_SIZE = 900, 900
PARTICLE_RADIUS = 8


def main(
    steps=5000,
    nr_of_particles=200,
    temperature=5,  # Kelvin (that's pretty cool!)
    run_integrator=True,
    dt=1e-2,
    collision_distance=(2 * PARTICLE_RADIUS / DISPLAY_SIZE[0])
):

    y0 = initialize(nr_of_particles, temperature)

    if run_integrator:
        ys = integrate(nr_of_particles, y0, steps, dt, collision_distance)
        np.savetxt('./gas_in_a_box/out/ys.txt', ys)
    else:
        ys = np.loadtxt('./gas_in_a_box/out/ys.txt')

    display(ys, nr_of_particles, DISPLAY_SIZE, PARTICLE_RADIUS)
