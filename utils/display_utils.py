import pygame


def draw_frame(display, color, display_size):

    display_width = display_size[0]
    display_height = display_size[1]

    pygame.draw.line(
        display, color, (0, 0), (0, display_height), 5
    )
    pygame.draw.line(
        display, color,
        (0, display_height), (display_width, display_height), 5
    )
    pygame.draw.line(
        display, color,
        (display_width, display_height), (display_width, 0), 5
    )
    pygame.draw.line(
        display, color, (display_width, 0), (0, 0), 5
    )
