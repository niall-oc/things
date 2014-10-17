import game_of_life
import pygame

screen = pygame.display.set_mode((600, 480))
state = set([(y+90, 100) for y in xrange(201)]+[(100, y+90) for y in xrange(300)])
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
    clock.tick(240)

