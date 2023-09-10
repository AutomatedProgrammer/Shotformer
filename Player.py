# Two objects: Enemy and Player
# Connect keys for movement, inherited from Parent to Child class
import pygame
import random
from Object import Object

PL_V = 3  # player velocity, had to include this here
gravity = 5
jump_height = 10

class Player(Object):

    def __init__(self, name, width, height, x, y, image_path):
        super(Player, self).__init__(name, width, height, x,y, image_path)
        self.in_middle = False
        self.jumping = False
        self.air_time = 0

    def update(self):
        key = pygame.key.get_pressed()

        #Jumping movement. I think to make it smoother we only set jumping to false after the key's been held down for a little bit.
        if key[pygame.K_UP] and key[pygame.K_RIGHT] and self.jumping == False:
            if self.air_time > 50:
                self.jumping = True
                self.air_time = 0
            self.move_y(-jump_height)
            self.air_time += 1
            if self.rect.centerx > 380:
                self.in_middle = True

            elif self.in_middle == False: 
                self.move_x(PL_V)
                
        elif key[pygame.K_UP] and key[pygame.K_LEFT] and self.jumping == False:
            if self.air_time > 50:
                self.jumping = True
                self.air_time = 0
            self.move_y(-jump_height)
            self.air_time += 1
            if self.rect.centerx > 0:
                self.move_x(-PL_V)
                self.in_middle = False

        #Jumping just up
        elif key[pygame.K_UP] and self.jumping == False:
            if self.air_time > 50:
                self.jumping = True
                self.air_time = 0
            self.move_y(-jump_height)
            self.air_time += 1

        #Gravity
        if self.rect.centery < 340:
            self.move_y(gravity)
            self.rect.centery = self.y
            self.air_time += 1
            if self.rect.centery == 340:
                self.jumping = False
                self.air_time = 0
                

        #Regular movement
        if key[pygame.K_LEFT]:
            if self.rect.centerx > 0:
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
