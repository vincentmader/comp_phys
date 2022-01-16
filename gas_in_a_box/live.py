from datetime import datetime as dt
import time

import numpy as np
import pygame
from tqdm import tqdm

from .initialize import main as initialize
from .integrate.next_step import main as next_step
from utils import display_utils


# define colors for displaying with pygame
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
RED, GREEN, BLUE = (255, 0, 0), (0, 128, 0), (0, 0, 255)


def main(nr_of_particles=200, Dt=1e-2, display_size=(800, 800)):

    pygame.init()
    # define display
    DISPLAY_WIDTH, DISPLAY_HEIGHT = display_size[0], display_size[1]
    DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 0, 32)
    ORIGIN = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)

    # define fonts
    pygame.font.init()
    myfont = pygame.font.SysFont('Hack Nerd', 60)
    title_font = pygame.font.SysFont('Hack Nerd', 200)

    temperature = 3

    system_state = initialize(nr_of_particles, temperature)

    frame_num = 0
    while True:

        # dates for fps
        date_start = dt.now()

        # handle events
        for event in pygame.event.get():
            pass
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    temperature += 10
                if event.key == pygame.K_DOWN:
                    temperature -= 10
                # if event.key == pygame.K_LEFT:

                # if event.key == pygame.K_RIGHT:

        system_state = next_step(
            system_state, nr_of_particles, Dt, temperature)
        # stop animation after last entry in simulation output data
        # try:
        #     y = ys[frame_num]
        # except IndexError:
        #     continue

        # clear screen & draw frame
        DISPLAY.fill(BLACK)
        display_utils.draw_frame(DISPLAY, WHITE, display_size)

        # get particle coordinates for given frame num
        for particle_idx in range(nr_of_particles):

            r = system_state[6*particle_idx + 1]
            x = system_state[6*particle_idx + 2]
            y = system_state[6*particle_idx + 3]
            vx = system_state[6*particle_idx + 4]
            vy = system_state[6*particle_idx + 5]
            x *= DISPLAY_WIDTH
            y *= DISPLAY_HEIGHT

            # draw particles
            drawing_radius = r * DISPLAY_WIDTH
            # drawing_radius = 1
            color = RED if particle_idx < 10 else WHITE
            pygame.draw.circle(DISPLAY, color, (x, y), drawing_radius)

            # draw_velocity_vector
            # lol = 10000
            # color = 'red'
            # next_x = x + lol * vx * Dt
            # next_y = y + lol * vy * Dt
            # pygame.draw.line(DISPLAY, color, (x, y), (next_x, next_y), 2)

        try:
            text = f'{temperature} K     {int(fps)} fps'
            # text = f'{temperature}'
        except UnboundLocalError:
            text = f'{temperature}'
        textsurface = myfont.render(f'{text}', False, (255, 255, 255))
        DISPLAY.blit(textsurface, (60, 60))

        # update, wait shortly, update frame number
        pygame.display.update()
        # time.sleep(0.01)
        frame_num += 1

        # date for fps
        date_finish = dt.now()
        fps = 1e6 / ((date_finish - date_start)).microseconds

        # input()

    # def main(nr_of_particles, y0, steps, dt):  # , collision_distance):

    #     system_states = []
    #     current_system_state = y0

    #     for step_idx in tqdm(range(steps)):

    #         next_system_state = get_next_system_state_step(
    #             current_system_state, nr_of_particles, dt
    #         )

    #         system_states.append(next_system_state)
    #         current_system_state = system_states[-1]

    #     return system_states

    # DISPLAY_SIZE = 900, 900

    # def main(
    #     steps=500,
    #     nr_of_particles=100,
    #     temperature=3,  # Kelvin (that's pretty cool!)
    #     run_integrator=True,
    #     dt=1e-3,
    # ):

    #     y0 = initialize(nr_of_particles, temperature)

    #     if run_integrator:
    #         ys = integrate(nr_of_particles, y0, steps, dt)
    #         np.savetxt('./gas_in_a_box/out/ys.txt', ys)
    #     else:
    #         ys = np.loadtxt('./gas_in_a_box/out/ys.txt')

    #     display(ys, nr_of_particles, DISPLAY_SIZE)
