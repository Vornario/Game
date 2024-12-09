import pygame

WIDTH = 500
HEIGHT = 500

window_size = (500, 500)

FPS = 60
pygame.display.set_mode(window_size)
pygame.display.init()
clock = pygame.time.Clock()
root_scene = pygame.display.set_mode((500, 500))
class Hero:
    def __init__(self, w, h):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.speed = 10
        self.w = w
        self.h = h
    
    def move_down(self):
        self.y += self.speed

    def move_up(self):
        self.y -= self.speed

    def move_left(self):
        self.x -= self.speed

    def move_right(self):
        self.x += self.speed
    
while 1 == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()



        if (event.type == pygame.KEYDOWN):
            if event.key == pygame.K_DOWN:
                Hero.move_down()
            if event.key == pygame.K_UP:
                Hero.move_up()
            if event.key == pygame.K_LEFT:
                Hero.move_left()
            if event.key == pygame.K_RIGHT:
                Hero.move_right()
            else:
                print(event.key)
    root_scene.fill((255, 0, 0))
    pygame.draw.circle(root_scene, color= (0, 255, 0), center=(hero.x, hero.y))
    pygame.display.update()
    clock.tick(FPS)