import pygame
from Object import Object

class Enemy(Object):

    def __init__(self, name, width, height, x, y, image_path):
        super(Enemy, self).__init__(name, width, height, x, y, image_path)
        self.gravity = 5
        self.move_ticks = 250
        self.timer = 0
        self.movement_speed = 1
        self.direction = "right"
            
    def update(self):
        if self.rect.centery < 340:
            self.move_y(self.gravity)
        
        if self.direction == "right":
            self.move_x(self.movement_speed)
        elif self.direction == "left":
            self.move_x(-self.movement_speed)

        self.timer += 1
        if self.timer > self.move_ticks:
            if self.direction == "right":
                self.direction = "left"
            elif self.direction == "left":
                self.direction = "right"
            self.timer = 0
            
        #self.move_y(gravity)
        #self.rect.centery = self.y
        self.rect.centerx = self.x
        self.rect.centery = self.y
# There is probably a much better way of doing this