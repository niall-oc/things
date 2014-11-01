import game_of_life
import pygame
import random
from math import cos, sin


    
screen = pygame.display.set_mode((600, 480))
#state = set([(x+150, 200) for x in xrange(201)]+[(250, y+100) for y in xrange(201)])
# Randomise the generation
#state = set([])
#for i in xrange(10000):
#    state.add((random.randint(200, 300), random.randint(200, 300),))
def wave(x_array, y_offset):
    return [(x, int((round(sin(x))*3)+y_offset),) for x in x_array]
    
def circle(x, y, r):
    points = [
        (
            int(round(r*sin(angle)))+x, 
            int(round(r*cos(angle)))+y,
        ) 
        for angle in range(361)
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
    state = set(circle(200, 200, 50)+circle(200, 200, 52))
    run(state)
