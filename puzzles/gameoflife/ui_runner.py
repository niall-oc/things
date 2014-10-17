import game_of_life
import pygame
import random

screen = pygame.display.set_mode((600, 480))
#state = set([(x+150, 200) for x in xrange(201)]+[(250, y+100) for y in xrange(201)])
# Randomise the generation
state = set([])
for i in xrange(10000):
    state.add((random.randint(100, 400), random.randint(100, 400),))
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

