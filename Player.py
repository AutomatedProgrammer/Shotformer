# Two objects: Enemy and Player
# Connect keys for movement, inherited from Parent to Child class
import pygame
import random
from Object import Object

PL_V = 3  # player velocity, had to include this here

class Player(Object):

    def __init__(self, name, width, height, x, y, image_path):
        super(Player, self).__init__(name, width, height, x,y, image_path)
        self.in_middle = False

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            self.move_x(-PL_V)
            self.in_middle = False
            
        elif key[pygame.K_RIGHT]:
            if self.rect.centerx > 380:
                self.in_middle = True

            elif self.in_middle == False: 
                self.move_x(PL_V)
                
        self.rect.centerx = self.x
        self.rect.centery = self.y

# jumping can be added here, but for now, this will be for movements left and right.
