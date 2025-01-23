import pygame
import heroes
import obstacles
import sys

pygame.init()
pygame.display.set_caption("Fecalis Revenge")
pygame.display.set_icon(pygame.image.load("logo.bmp"))

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((1000, 800))
clock = pygame.time.Clock()
FPS = 60

# Define the map as a 2D array
# 0 = walkable, 1 = wall
MAP = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

TILE_SIZE = 50
walls = []

# Parse the map to create wall rectangles
for row_idx, row in enumerate(MAP):
    for col_idx, tile in enumerate(row):
        if tile == 1:
            rect = pygame.Rect(
                col_idx * TILE_SIZE, row_idx * TILE_SIZE, TILE_SIZE, TILE_SIZE
            )
            walls.append(rect)

# Initialize the hero
hero = heroes.Hero(40, "hero.png")

bulls = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx = -5
    elif keys[pygame.K_RIGHT]:
        dx = 5
    elif keys[pygame.K_DOWN]:
        dy = 5
    elif keys[pygame.K_UP]:
        dy = -5

    # Move hero and check collisions
    hero.rect.x += dx
    hero.rect.y += dy

    for wall in walls:
        if hero.rect.colliderect(wall):
            # Undo the movement if collision detected
            hero.rect.x -= dx
            hero.rect.y -= dy
            break

    if keys[pygame.K_f]:
        bulls.append(obstacles.Bullet(hero.rect.x, hero.rect.y, "bullet.png", hero))

    # Draw everything
    screen.fill(BLACK)
    for wall in walls:
        pygame.draw.rect(screen, RED, wall)

    screen.blit(hero.image, hero.rect)
    for bull in bulls:
        screen.blit(bull.image, bull.rect)
        bull.update()

    pygame.display.flip()
    clock.tick(FPS)
