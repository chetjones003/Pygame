import sys
import os
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

sky_surface = pygame.image.load(
        os.path.join('Graphics', 'Sky.png')
        )
ground_surface = pygame.image.load(
        os.path.join('Graphics', 'ground.png')
        )
text_surface = test_font.render('My Game', False, 'Green')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    # draw all elements and update everything
    pygame.display.update()
    clock.tick(60)
