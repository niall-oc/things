# -*- coding: utf-8 -*-
import random
from math import cos, sin, radians
import pygame
import game_of_life
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


def wave_start_state(x, y, r, length):
    """
    Start the game with a wave
    """
    points = []
    angle = 0
    max_x = x
    end = x + length
    while max_x < end:
        # when returning to the lower half of the circle we need
        # to move the center point along the x access.
        if angle in (91, 270):
            x = x + 2 * r
        # need to record the max x position so we don't go longer than the length
        max_x = int(round(r*sin(radians(angle))))+x
        points.append(
            (
                max_x,
                int(round(r*cos(radians(angle))))+y,
            )
        )
        angle += 1
        if angle > 361:
            angle = 0
    return points


def circle_start_state(x, y, r):
    """
    Start the game with a circle
    """
    points = [
        (
            int(round(r*sin(radians(angle))))+x,
            int(round(r*cos(radians(angle))))+y,
        )
        for angle in range(360)
    ]
    return points


def init_screen(width, height):
    """
    Initialize pygame hardware
    """
    display_options = pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE | pygame.FULLSCREEN
    screen = pygame.display.set_mode((width, height), display_options)
    surface = pygame.Surface(screen.get_size())
    return screen, surface


def run(game_state, width, height, percent):
    """
    Main loop
    """
    clock = pygame.time.Clock()
    running = True
    black = (0, 0, 0)
    white = (255, 255, 255)
    origin = (0, 0)
    start = origin
    end = width, height
    screen, surface = init_screen(width, height)

    pygame.font.init()
    myfont = pygame.font.SysFont('Comic Sans MS', 30)
    screen_stats = "start: {0}, end: {1}"
    textsurface = myfont.render(screen_stats.format(0, 0), False, (255, 255, 0))
    while running:
        surface.fill(black)
        for cell in game_state:
            surface.set_at(cell, white)

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN or event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                start = pygame.mouse.get_pos()
            if event.type == pygame.MOUSEBUTTONUP:
                end = pygame.mouse.get_pos()
                textsurface = myfont.render(screen_stats.format(start, end), False, (255, 255, 0))
                game_state = game_state.union(game_of_life.create_cells(start, end, percent))


        screen.blit(surface.convert(), origin)
        screen.blit(textsurface.convert(), origin)
        pygame.display.flip()
        game_state = game_of_life.step(game_state)
        clock.tick(24)


if __name__ == "__main__":
    run(game_state=set([]), width=640, height=480, percent=10)
