import numpy as np
from tqdm import tqdm


def main(nr_of_particles, y0, steps, dt, collision_distance):

    system_states = []
    current_system_state = y0

    for step_idx in tqdm(range(steps)):

        particle_states = []
        for idx in range(nr_of_particles):

            # get mass, position & velocity
            m = current_system_state[5*idx]
            x = current_system_state[5*idx + 1]
            y = current_system_state[5*idx + 2]
            vx = current_system_state[5*idx + 3]
            vy = current_system_state[5*idx + 4]

            # collisions with other particles
            for jdx in range(nr_of_particles):

                # no collisions with one-self
                if idx == jdx:
                    continue

                # get distance
                x2 = current_system_state[5*jdx + 1]
                y2 = current_system_state[5*jdx + 2]
                distance = np.sqrt((x2-x)**2 + (y2-y)**2)
                # skip if it's larger than collision distance (particle radius)
                if distance > collision_distance:
                    continue
                # get mass, location & velocity of other particle
                m2 = current_system_state[5*jdx]
                vx2 = current_system_state[5*jdx + 3]
                vy2 = current_system_state[5*jdx + 4]
                M = m + m2
                # apply momentum transfer according to elastic collision
                vx = (m-m2)/M * vx + 2*m2/M * vx2
                vy = 2*m/M * vy + (m2-m)/M * vy2

            # collisions with box edges
            if x + vx*dt <= 0 or x + vx*dt >= 1:
                vx *= -1
            if y + vy*dt <= 0 or y + vy*dt >= 1:
                vy *= -1

            # update positions
            x += vx * dt
            y += vy * dt

            for i in [m, x, y, vx, vy]:
                particle_states.append(i)

        system_states.append(particle_states)
        current_system_state = system_states[-1]

    return system_states
