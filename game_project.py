import pygame
import heroes
import obstacles

pygame.init()
pygame.display.set_caption("Fecalis revenge")
pygame.display.set_icon(pygame.image.load("logo.bmp"))

BLACK = (0, 0, 0)
W, H = 1000, 570

sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
FPS = 60


hero = heroes.Hero(40, "hero.png")

bulls = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        hero.move_left()
    elif keys[pygame.K_RIGHT]:
        hero.move_right()
    elif keys[pygame.K_DOWN]:
        hero.move_down()
    elif keys[pygame.K_UP]:
        hero.move_up()

        if event.key == pygame.K_f:
            bulls.append(
                obstacles.Bullet(hero.rect.x, hero.rect.y, "bullet.png", hero)
            )

    sc.fill(BLACK)
    sc.blit(hero.image, hero.rect)
    for bull in bulls:
        sc.blit(bull.image, bull.rect)
        bull.update()
    pygame.display.update()
    clock.tick(FPS)
