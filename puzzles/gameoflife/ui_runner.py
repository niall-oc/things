import game_of_life
import pygame
import random
from math import cos, sin, radians

screen = pygame.display.set_mode((800, 600))

def wave(x, y, r, length):
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

def circle(x, y, r):
    points = [
        (
            int(round(r*sin(radians(angle))))+x, 
            int(round(r*cos(radians(angle))))+y,
        )
        for angle in range(360)
    ]
    return points

def run(state):
    clock = pygame.time.Clock()
    running = True
    while running:
        screen.fill((0,0,0,))
        for cell in state:
            screen.set_at(cell, (255,255,255))
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.flip()
        state = game_of_life.step(state)
        clock.tick(24)

if __name__ == "__main__":
    state = set([(x+150, 200) for x in xrange(201)]+[(250, y+100) for y in xrange(201)])
    # Randomise the generation
    #state = set([])
    #for i in xrange(10000):
    #    state.add((random.randint(200, 300), random.randint(200, 300),))
    #state = set(wave(0, 200, 50, 580)+wave(0, 200, 52, 580))
    run(state)
