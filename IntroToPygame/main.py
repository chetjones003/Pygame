import sys
import os
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()

# first surface
sky_image = pygame.image.load(os.path.join('IntroToPygame', 'graphics', 'Sky.png'))
ground_image = pygame.image.load(os.path.join('IntrotoPygame', 'graphics', 'ground.png'))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sky_image, (0, 0))
    screen.blit(ground_image, (0, 250))

    # draw all elements and update everything
    pygame.display.update()
    clock.tick(60)
