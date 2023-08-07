# Two objects: Enemy and Player
# Connect keys for movement, inherited from Parent to Child class
import pygame
import random
from Object import Object

PL_V = 5  # player velocity, had to include this here

class Player(Object):

    def keytracker(self):
        super().__init__()

        character = pygame.player_movement.get_pressed()

        character.x_vel = 0;

        if character[pygame.K_LEFT]:
            character.move_left(PL_V)

        if character[pygame.K_RIGHT]:
            character.move_right(PL_V)

# jumping can be added here, but for now, this will be for movements left and right.
