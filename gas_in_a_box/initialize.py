import numpy as np


def main(nr_of_particles, temperature):

    mean_velocity = np.sqrt(temperature / nr_of_particles)  # with k_B = 1
    velocity_distribution = np.random.normal  # TODO: change to Boltzmann dist.

    y0 = []
    for i in range(nr_of_particles):

        mass = 1  # TODO: randomize (discretely? -> nr. of nucleons in atom)

        x = np.random.uniform(0, 1)  # box edges are set to 0 and 1
        vx = velocity_distribution(mean_velocity, np.sqrt(mean_velocity))

        y = np.random.uniform(0, 1)
        vy = velocity_distribution(mean_velocity, np.sqrt(mean_velocity))

        for i in [mass, x, y, vx, vy]:
            y0.append(i)

    return y0
