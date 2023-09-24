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
        self.PL_V = 3 
        self.gravity = 5
        self.jump_height = 12
        self.direction = "right"
        self.collided = False
        self.hitboxtop = pygame.Rect(x, y, width/1, height/2)
        self.hitboxbottom = pygame.Rect(x, y, width/1, height/2)
        self.hitboxleft = pygame.Rect(x, y, width/2, height)
        self.hitboxright = pygame.Rect(x, y, width/2, height)

    def update(self):
        key = pygame.key.get_pressed()

        if key[pygame.K_SPACE] and self.gun_empty == False:
            print("BANG")
            self.gun_empty = True
            self.gun_fired = True
        
        if key[pygame.K_r] and self.gun_empty == True:
            print("RELOAD")
            self.gun_empty = False

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

        elif key[pygame.K_UP] and self.jumping == False:
            if self.air_time > 50:
                self.jumping = True
                self.air_time = 0
            self.move_y(-self.jump_height)
            self.air_time += 1

        if self.rect.centery < 340:
            self.move_y(self.gravity)
            self.rect.centery = self.y
            self.air_time += 1
            if self.rect.centery >= 340:
                self.jumping = False
                self.air_time = 0
                self.rect.centery = 340
                
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
        self.hitboxtop.centerx = self.x
        self.hitboxtop.centery = self.y-10
        self.hitboxbottom.centerx = self.x
        self.hitboxbottom.centery = self.y+10
        self.hitboxleft.centerx = self.x-10
        self.hitboxleft.centery = self.y
        self.hitboxright.centerx = self.x+10
        self.hitboxright.centery = self.y