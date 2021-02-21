import pygame
from util import draw_planet

pygame.init()

game_display = pygame.display.set_mode((960, 540))
pygame.display.set_caption("Satellite shooter")

clock = pygame.time.Clock()

crashed = False

while not crashed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crashed = True
        print(event)
    draw_planet(game_display, 450, 300)
    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()