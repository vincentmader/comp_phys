import numpy as np

kB = 1


def main(system_state, nr_of_particles, Dt, wall_temperature=None):

    next_system_state = []

    for idx in range(nr_of_particles):

        # get mass, position & velocity
        m = system_state[6*idx]
        r = system_state[6*idx + 1]
        x = system_state[6*idx + 2]
        y = system_state[6*idx + 3]
        vx = system_state[6*idx + 4]
        vy = system_state[6*idx + 5]

        # collisions with other particles
        for jdx in range(nr_of_particles):

            # no collisions with one-self
            if idx == jdx:
                continue

            # get distance
            r2 = system_state[6*jdx + 1]
            x2 = system_state[6*jdx + 2]
            y2 = system_state[6*jdx + 3]
            vx2 = system_state[6*jdx + 4]
            vy2 = system_state[6*jdx + 5]

            Dx = (x2 + vx * Dt - x)
            Dy = (y2 + vy * Dt - y)
            distance = np.sqrt(Dx**2 + Dy**2)
            # skip if it's larger than collision distance (particle radius)
            collision_distance = r + r2
            if distance > collision_distance:
                continue

            # get mass, location & velocity of other particle
            m2 = system_state[6*jdx]
            vx2 = system_state[6*jdx + 4]
            vy2 = system_state[6*jdx + 5]
            M = m + m2
            # apply momentum transfer according to elastic collision
            vx = (m-m2)/M * vx + 2*m2/M * vx2
            vy = 2*m/M * vy + (m2-m)/M * vy2
            # make sure they don't get stuck
            # d_s = r + r2
            # d_i < r + r2  ->  d += (d_s - d_i) / 2
            # x -= Dx - r
            # y -= Dy - r

        if wall_temperature:
            particle_temperature = m * (vx**2 + vy**2) / (3 * kB)
            new_temperature = (wall_temperature + particle_temperature) / 2
            new_velocity = np.sqrt(3 * kB * new_temperature / m)
            old_velocity = np.sqrt((vx**2 + vy**2))

        # collisions with box edges
        if x + vx*Dt <= 0 or x + vx*Dt >= 1:
            # if wall_temperature:
            #     vx *= -new_velocity / old_velocity
            # else:
            x += vx * Dt
            y += vy * Dt

            vx *= -1
        if y + vy*Dt <= 0 or y + vy*Dt >= 1:
            # if wall_temperature:
            #     vy *= -new_velocity / old_velocity
            # else:
            x += vx * Dt
            y += vy * Dt

            vy *= -1

        # update positions
        x += vx * Dt
        y += vy * Dt

        for i in [m, r, x, y, vx, vy]:
            next_system_state.append(i)

    return next_system_state
