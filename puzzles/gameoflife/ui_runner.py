# -*- coding: utf-8 -*-
import random
from math import cos, sin, radians
import pygame
import game_of_life


DISPLAY_OPTIONS = pygame.DOUBLEBUF | pygame.HWSURFACE | pygame.RESIZABLE
SCREEN = pygame.display.set_mode((800, 600), DISPLAY_OPTIONS)
SURFACE = pygame.Surface(SCREEN.get_size())


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


def run(state):
    """
    Main loop
    """
    clock = pygame.time.Clock()
    running = True
    black = (0, 0, 0)
    white = (255, 255, 255)
    origin = (0,0)
    while running:
        SURFACE.fill(black)
        for cell in state:
            SURFACE.set_at(cell, white)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        SCREEN.blit(SURFACE.convert(), origin)
        pygame.display.flip()
        state = game_of_life.step(state)
        clock.tick(24)


if __name__ == "__main__":
    game_state = set([])
    for i in range(1000):
        game_state.add((random.randint(0, 800), random.randint(0, 600),))
    # state = set(wave_start_state(0, 20, 50, 80) + wave_start_state(0, 20, 52, 180))
    run(game_state)
