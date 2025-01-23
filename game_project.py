import pygame
import heroes
import obstacles
import sys

pygame.init()
pygame.display.set_caption("Fecalis revenge")
pygame.display.set_icon(pygame.image.load("logo.bmp"))

BLACK = (0, 0, 0)


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 800
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Fecalis Revenge")
clock = pygame.time.Clock()


hero = heroes.Hero(30, 30, "hero.jpg")

bulls = []


walls = [
    obstacles.Wall(0, 0, SCREEN_WIDTH, 20),  # Верхняя стена
    obstacles.Wall(0, SCREEN_HEIGHT - 20, SCREEN_WIDTH, 20),  # Нижняя стена
    obstacles.Wall(0, 0, 20, SCREEN_HEIGHT),  # Левая стена
    obstacles.Wall(SCREEN_WIDTH - 20, 0, 20, SCREEN_HEIGHT),  # Правая стена
    obstacles.Wall(200, 200, 100, 20),  # Пример внутренней стены
]


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Обработка нажатий клавиш
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero.move_left()
    if keys[pygame.K_RIGHT]:
        hero.move_right()
    if keys[pygame.K_UP]:
        hero.move_up()
    if keys[pygame.K_DOWN]:
        hero.move_down()
        
    # Очистка экрана
    screen.fill(BLACK)

    # Отрисовка стен
    for wall in walls:
        wall.draw(screen)

    # Отрисовка персонажа
    hero.draw(screen)

    # Обновление экрана
    
    pygame.display.flip()
    clock.tick(60)
    