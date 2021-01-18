import numpy as np


def main(nr_of_particles, temperature):

    mean_velocity = np.sqrt(temperature / nr_of_particles)  # with k_B = 1
    velocity_distribution = np.random.normal  # TODO: change to Boltzmann dist.

    y0 = []
    for i in range(nr_of_particles):

        mass = 1  # TODO: randomize (discretely? -> nr. of nucleons in atom)
        radius = 1e-2 if i else 1e-2

        valid_position_found = False
        while not valid_position_found:
            x = np.random.uniform(0, 1)  # box edges are set to 0 and 1
            y = np.random.uniform(0, 1)
            valid_position_found = True
            for j in range(0, len(y0), 6):
                distance = ((y0[j+2]-x)**2 + (y0[j+3]-y)**2)**.5
                if distance < radius + y0[j+1]:
                    valid_position_found = False

        vx = velocity_distribution(mean_velocity, np.sqrt(mean_velocity))
        vy = velocity_distribution(mean_velocity, np.sqrt(mean_velocity))

        for i in [mass, radius, x, y, vx, vy]:
            y0.append(i)

    return y0
