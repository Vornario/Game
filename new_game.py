import pygame
import sys
import obstacles
import heroes

pygame.init()

screen = pygame.display.set_mode((1000, 800))
r = pygame.Rect(50, 50, 100, 200)
pygame.draw.rect(screen, (255, 0, 0), r, 0)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
