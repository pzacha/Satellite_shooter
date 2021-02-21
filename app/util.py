import pygame


def draw_planet(surface, xcor, ycor):
    pygame.draw.circle(surface, (255, 255, 255), (xcor, ycor), 10)
