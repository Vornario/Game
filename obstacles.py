import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, filename, hero):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(
            pygame.image.load(filename).convert_alpha(), (30, 30)
        )
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = hero.image.get_rect(center=(hero.rect.x, hero.rect.y))
        self.speed = 30

    def update(self):
        self.rect.x += self.speed

class Wall:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (0, 0, 255)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)
