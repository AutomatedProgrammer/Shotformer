# Two objects: Enemy and Player
# Connect keys for movement, inherited from Parent to Child class
import pygame
import random
from Object import Object

PL_V = 5  # player velocity, had to include this here

class Player(Object):

    def init(self, name, width, height, x, y, image_path):
        super(Player, self).init(name, width, height, x,y, image_path)

        key = pygame.player_movement.get_pressed()

        if key[pygame.K_LEFT]:
            self.move_left(PL_V)

        elif key[pygame.K_RIGHT]:
            self.move_right(PL_V)

# jumping can be added here, but for now, this will be for movements left and right.
