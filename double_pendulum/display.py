import time

import numpy as np
from numpy import cos, sin, pi
import pygame
from pygame.locals import *

from utils import display_utils


# define colors for displaying with pygame
BLACK, WHITE = (0, 0, 0), (255, 255, 255)
RED, GREEN, BLUE = (255, 0, 0), (0, 128, 0), (0, 0, 255)

TAIL_LENGTH = 200


def main(ys, L, in_christmas_mode=False, fading_tails=True):

    pygame.init()
    # define display
    DISPLAY_WIDTH, DISPLAY_HEIGHT = 900, 900
    DISPLAY = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), 0, 32)
    ORIGIN = (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2)
    # define fonts
    pygame.font.init()
    myfont = pygame.font.SysFont('Hack Nerd', 60)
    title_font = pygame.font.SysFont('Hack Nerd', 200)

    def shift_coordinates(x_1, y_1, x_2, y_2):

        x_1 = (0.24 * x_1 + .5) * DISPLAY_WIDTH
        y_1 = (-0.24 * y_1 + .5) * DISPLAY_HEIGHT
        x_2 = (0.24 * x_2 + .5) * DISPLAY_WIDTH
        y_2 = (-0.24 * y_2 + .5) * DISPLAY_HEIGHT

        return x_1, y_1, x_2, y_2

    def make_transparent(color, alpha):
        r, g, b = color[0], color[1], color[2]
        return (int(alpha * r), int(alpha * g), int(alpha * b))

    def draw_tail(ys, frame_num, tail_length=150, fading_tails=True):

        frames_back = min(frame_num - 1, tail_length)
        for idx in range(frame_num - frames_back, frame_num):
            y_previous = ys[idx - 1]
            y_current = ys[idx]

            th_1, th_2 = y_current[0], y_current[1]
            x_1c, y_1c = L * sin(th_1), -L * cos(th_1)
            x_2c, y_2c = x_1c + L * sin(th_2), y_1c - L * cos(th_2)
            x_1c, y_1c, x_2c, y_2c = shift_coordinates(x_1c, y_1c, x_2c, y_2c)

            th_1, th_2 = y_previous[0], y_previous[1]
            x_1p, y_1p = L * sin(th_1), -L * cos(th_1)
            x_2p, y_2p = x_1p + L * sin(th_2), y_1p - L * cos(th_2)
            x_1p, y_1p, x_2p, y_2p = shift_coordinates(x_1p, y_1p, x_2p, y_2p)

            if fading_tails:
                tail_idx = frame_num - idx
                alpha = 1 - tail_idx / tail_length
            else:
                alpha = 1
            red = make_transparent(RED, alpha)
            green = make_transparent(GREEN, alpha)

            pygame.draw.line(DISPLAY, red, (x_2p, y_2p), (x_2c, y_2c), 5)
            if not in_christmas_mode:
                pygame.draw.line(DISPLAY, green, (x_1p, y_1p), (x_1c, y_1c), 5)

    frame_num = 0
    while True:
        # handle events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        # display christmas message
        if in_christmas_mode and frame_num == 375:
            text = f'Merry Christmas!'
            textsurface = title_font.render(f'{text}', False, (255, 0, 0))
            DISPLAY.blit(textsurface, (.08*DISPLAY_WIDTH, .14*DISPLAY_HEIGHT))
            pygame.display.update()
            input()
        # stop animation after last entry in simulation output data
        try:
            y = ys[frame_num]
        except IndexError:
            continue
        # clear screen & draw frame
        DISPLAY.fill(BLACK)
        display_utils.draw_frame(DISPLAY, WHITE, display_size)
        # get pendulum coordinates for given frame
        th_1, th_2 = y[0], y[1]
        x_1, y_1 = L * sin(th_1), -L * cos(th_1)
        x_2, y_2 = x_1 + L * sin(th_2), y_1 - L * cos(th_2)
        x_1, y_1, x_2, y_2 = shift_coordinates(x_1, y_1, x_2, y_2)
        # draw tails, pendulum bodies, and pendulum rods
        tail_length = TAIL_LENGTH if not in_christmas_mode else 150
        fading_tails = False if in_christmas_mode else True
        draw_tail(
            ys, frame_num, tail_length=tail_length, fading_tails=fading_tails
        )
        pygame.draw.circle(DISPLAY, WHITE, ORIGIN, 10, 15)
        pygame.draw.circle(DISPLAY, WHITE, (x_1, y_1), 10, 45)
        pygame.draw.circle(DISPLAY, WHITE, (x_2, y_2), 10, 45)
        pygame.draw.line(DISPLAY, WHITE, ORIGIN, (x_1, y_1), 3)
        pygame.draw.line(DISPLAY, WHITE, (x_1, y_1), (x_2, y_2), 3)
        # show frame number in top left
        if not in_christmas_mode:
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
