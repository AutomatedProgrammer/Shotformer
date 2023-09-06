import pygame
from Object import Object

gravity = 5

class Enemy(Object):

    def __init__(self, name, width, height, x, y, image_path):
        super(Enemy, self).__init__(name, width, height, x, y, image_path)

    def update(self):
        if self.rect.centery < 340:
            self.move_y(gravity)
        #self.move_y(gravity)
        #self.rect.centery = self.y
        self.rect.centerx = self.x
        self.rect.centery = self.y

    
# There is probably a much better way of doing this