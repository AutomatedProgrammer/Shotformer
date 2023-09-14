# Two objects: Enemy and Player
# Connect keys for movement, inherited from Parent to Child class
import pygame
import random
from Object import Object

class Player(Object):

    def __init__(self, name, width, height, x, y, image_path):
        super(Player, self).__init__(name, width, height, x,y, image_path)
        self.in_middle = False
        self.jumping = False
        self.air_time = 0
        self.gun_fired = False
        self.gun_empty = False
        self.PL_V = 3  # player velocity, had to include this here
        self.gravity = 5
        self.jump_height = 12
        self.direction = "right"

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] and self.gun_empty == False:
            print("BANG")
            self.gun_empty = True
            self.gun_fired = True
        
        if key[pygame.K_r] and self.gun_empty == True:
            print("RELOAD")
            self.gun_empty = False

        #Jumping movement. I think to make it smoother we only set jumping to false after the key's been held down for a little bit.
        if key[pygame.K_UP] and key[pygame.K_RIGHT] and self.jumping == False:
            self.direction = "right"
            if self.air_time > 50:
                self.jumping = True
                self.air_time = 0
            self.move_y(-self.jump_height)
            self.air_time += 1
            if self.rect.centerx > 380:
                self.in_middle = True

            elif self.in_middle == False: 
                self.move_x(self.PL_V)
                
        elif key[pygame.K_UP] and key[pygame.K_LEFT] and self.jumping == False:
            self.direction = "left"
            if self.air_time > 50:
                self.jumping = True
                self.air_time = 0
            self.move_y(-self.jump_height)
            self.air_time += 1
            if self.rect.centerx > 0:
                self.move_x(-self.PL_V)
                self.in_middle = False

        #Jumping just up
        elif key[pygame.K_UP] and self.jumping == False:
            if self.air_time > 50:
                self.jumping = True
                self.air_time = 0
            self.move_y(-self.jump_height)
            self.air_time += 1

        #Gravity
        if self.rect.centery < 340:
            self.move_y(self.gravity)
            self.rect.centery = self.y
            self.air_time += 1
            if self.rect.centery >= 340:
                self.jumping = False
                self.air_time = 0
                self.rect.centery = 340
                

        #Regular movement
        if key[pygame.K_LEFT]:
            self.direction = "left"
            if self.rect.centerx > 0:
                self.move_x(-self.PL_V)
                self.in_middle = False
            
            
        elif key[pygame.K_RIGHT]:
            self.direction = "right"
            if self.rect.centerx > 380:
                self.in_middle = True

            elif self.in_middle == False: 
                self.move_x(self.PL_V)

        self.rect.centerx = self.x
        self.rect.centery = self.y

# jumping can be added here, but for now, this will be for movements left and right.
