import pygame
import obstacles

class Hero:
    def __init__(self, x, y, image_path):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 5

    def move_left(self):
        self.rect.x -= self.speed

    def move_right(self):
        self.rect.x += self.speed

    def move_up(self):
        self.rect.y -= self.speed

    def move_down(self):
        self.rect.y += self.speed

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def check_collision(self, walls):
        for wall in walls:
            if self.rect.colliderect(wall.rect):
                print(f"Коллизия с стеной на x={wall.rect.x}, y={wall.rect.y}")
                return True
        return False