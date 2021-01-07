import time

import numpy as np
from numpy import cos, sin, pi
import pygame
from pygame.locals import *

from utils import display_utils


# define colors for displaying with pygame
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
RED, GREEN, BLUE = (255, 0, 0), (0, 128, 0), (0, 0, 255)


def main(ys, nr_of_particles, display_size, particle_radius):

    pygame.init()
    # define display
    DISPLAY_WIDTH, DISPLAY_HEIGHT = display_size[0], display_size[1]
    DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 0, 32)
    ORIGIN = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
    # define fonts
    pygame.font.init()
    myfont = pygame.font.SysFont('Hack Nerd', 60)
    title_font = pygame.font.SysFont('Hack Nerd', 200)

    frame_num = 0
    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # stop animation after last entry in simulation output data
        try:
            y = ys[frame_num]
        except IndexError:
            continue
        # clear screen & draw frame
        DISPLAY.fill(BLACK)
        display_utils.draw_frame(DISPLAY, WHITE, display_size)
        # get particle coordinates for given frame num
        for particle_idx in range(nr_of_particles):

            x = ys[frame_num][5*particle_idx + 1]
            y = ys[frame_num][5*particle_idx + 2]
            x *= DISPLAY_WIDTH
            y *= DISPLAY_HEIGHT

            color = RED if particle_idx < 20 else WHITE
            pygame.draw.circle(DISPLAY, color, (x, y), particle_radius)

        formatted_frame_num = frame_num
        if frame_num < 10000:
            formatted_frame_num = f'0{frame_num}'
            if frame_num < 1000:
                formatted_frame_num = f'0{formatted_frame_num}'
                if frame_num < 100:
                    formatted_frame_num = f'0{formatted_frame_num}'
                    if frame_num < 10:
                        formatted_frame_num = f'0{formatted_frame_num}'
        text = f'{formatted_frame_num}'
        textsurface = myfont.render(f'{text}', False, (255, 255, 255))
        DISPLAY.blit(textsurface, (20, 20))
        text = f' /  {len(ys)}'
        textsurface = myfont.render(f'{text}', False, (255, 255, 255))
        DISPLAY.blit(textsurface, (150, 20))
        # update, wait shortly, update frame number
        pygame.display.update()
        time.sleep(0.01)
        frame_num += 1
