# Two objects: Enemy and Player
# Connect keys for movement, inherited from Parent to Child class
import pygame
import random
from Object import Object

PL_V = 5  # player velocity, had to include this here

class Player(Object):
    def keytracker(self):

        character = pygame.player_movement.get_pressed()

        character.x_vel = 0;

        if character[pygame.K_LEFT]:
            character.move_left(PL_V)

            if character[pygame.K_RIGHT]:
                character.move_right(PL_V)

# jumping can be added here, but for now, this will be for movements left and right.
class Enemy(Object):
    def __init__(self, enemy):
        for i in range(1, 500):
            print(random())
            if random() % 2:
                enemy.move_left()
                if random() % 3:
                    enemy.move_right()
# There is probably a much better way of doing this
