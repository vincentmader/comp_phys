import time

import matplotlib.pyplot as plt
import numpy as np
from numpy import cos, sin, pi
import pygame
from pygame.locals import *
from utils import display_utils


# define colors for displaying with pygame
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
RED, GREEN, BLUE = (255, 0, 0), (0, 128, 0), (0, 0, 255)

TAIL_LENGTH = 200


def main(ys):

    nr_of_bodies = int(len(ys[0]) / 8)

    # make plot
    # for i in range(nr_of_bodies):
    #     x = [j[8*i+2] for j in ys]
    #     y = [j[8*i+3] for j in ys]
    #     # print(x)
    #     # print(y)
    #     # input()

    #     plt.plot(x, y, label=i)
    # plt.legend()
    # plt.savefig('test.pdf')

    # =================

    # define display
    DISPLAY_WIDTH, DISPLAY_HEIGHT = 900, 900
    DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT
    DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 0, 32)
    ORIGIN = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)

    def shift_coordinates(x, y):
        x = (.2*x + .5) * DISPLAY_WIDTH
        y = (-.2*y + .5) * DISPLAY_HEIGHT
        return x, y

    def make_transparent(color, alpha):
        r, g, b = color[0], color[1], color[2]
        return (int(alpha * r), int(alpha * g), int(alpha * b))

    def draw_tail(ys, frame_num, i, tail_length=150, fading_tails=True):

        frames_back = min(frame_num - 1, tail_length)
        for idx in range(frame_num - frames_back, frame_num):
            y_previous = ys[idx - 1]
            y_current = ys[idx]

            r_xp, r_yp, r_zp = y_previous[8*i +
                                          2], y_previous[8*i+3], y_previous[8*i+4]
            r_xc, r_yc, r_zc = y_current[8*i +
                                         2], y_current[8*i+3], y_current[8*i+4]

            if fading_tails:
                tail_idx = frame_num - idx
                alpha = 1 - tail_idx / tail_length
            else:
                alpha = 1
            white = make_transparent(WHITE, alpha)

            r_xp, r_yp = shift_coordinates(r_xp, r_yp)
            r_xc, r_yc = shift_coordinates(r_xc, r_yc)

            pygame.draw.line(
                DISPLAY, white, (r_xp, r_yp), (r_xc, r_yc), 5
            )

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
        display_utils.draw_frame(DISPLAY, WHITE, DISPLAY_SIZE)

        # get body coordinates for given frame
        for i in range(nr_of_bodies):
            r_x, r_y, r_z = y[8*i+2], y[8*i+3], y[8*i+4]
            r_x, r_y = shift_coordinates(r_x, r_y)

            draw_tail(
                ys, frame_num, i,
                tail_length=TAIL_LENGTH, fading_tails=True
            )
            pygame.draw.circle(DISPLAY, WHITE, (r_x, r_y), 10, 45)

        # update, wait shortly, update frame number
        pygame.display.update()
        # time.sleep(0.01)
        frame_num += 1
        # break
