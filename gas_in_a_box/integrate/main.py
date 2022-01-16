import numpy as np
from tqdm import tqdm

from .next_step import main as next_step


def main(nr_of_particles, y0, steps, dt):  # , collision_distance):

    system_states = []
    current_system_state = y0

    for step_idx in tqdm(range(steps)):

        next_system_state = next_step(
            current_system_state, nr_of_particles, dt
        )

        system_states.append(next_system_state)
        current_system_state = system_states[-1]

    return system_states
