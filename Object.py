import pygame
import os

class Object(pygame.sprite.Sprite):
    
    def __init__(self, name , width, height, x, y, image_path):
        super().__init__()
        self.name = name
        self.image = pygame.image.load(os.path.join(image_path)).convert()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = [self.x, self.y]

    def load_texture_from_sheet(self, sheet_path, sprite_x, sprite_y):
        pass #More optimized texture loading function for loading from a spritesheet
            #Will bother with optimizations once we actually get a game running

    def move_x(self, x_move):
        self.x += x_move

    def move_y(self, y_move):
        self.y += y_move

    def update(self):
        self.rect.centerx = self.x
        self.rect.centery = self.y

    