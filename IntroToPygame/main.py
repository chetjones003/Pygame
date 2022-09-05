"""
pygame is a free and open-source cross-platform library for the development
of multimedia applications like video games using Python
"""
import sys
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # draw all elements and update everything
    pygame.display.update()
    clock.tick(60)
