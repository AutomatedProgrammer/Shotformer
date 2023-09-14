import pygame 
from Object import Object

class Bullet(Object):

    def __init__(self, name, width, height, x, y, image_path):
        super(Player, self).__init__(name, width, height, x,y, image_path)
        self.bullet_speed = 5

    def update(self):
        self.move_x(self.bullet_speed)
        self.rect.centerx = self.x
        self.rect.centery = self.y
