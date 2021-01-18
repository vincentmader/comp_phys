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


def format_frame_number(frame_num, nr_of_leading_zeros):

    formatted_frame_num = frame_num
    for i in range(nr_of_leading_zeros):
        if frame_num < 10**i:
            formatted_frame_num = f'0{formatted_frame_num}'

    return formatted_frame_num

    # if frame_num < 1000:
    #     formatted_frame_num = f'0{formatted_frame_num}'
    #     if frame_num < 100:
    #         formatted_frame_num = f'0{formatted_frame_num}'
    #         if frame_num < 10:
    #             formatted_frame_num = f'0{formatted_frame_num}'
