import pygame

class Hero(pygame.sprite.Sprite):

    def __init__(self, x, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(
            pygame.image.load(filename).convert_alpha(), (50, 50)
        )
        self.rect = self.image.get_rect(center=(x, 0))
        self.speed = 10

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

    def jump(self, h=100):
        for i in range(0, 10):
            self.rect.y -= h / 10