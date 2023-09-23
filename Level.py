import pygame
import json
from Object import Object
from Player import Player
from Enemy import Enemy
from Bullet import Bullet

scroll_speed = 3

class Level:
    
    def __init__(self):
        self.Objects = pygame.sprite.Group()
        self.Enemies = pygame.sprite.Group()
        self.Bullets = pygame.sprite.Group()
        #self.Player = Player

    def load_level(self, image_path):
        json_file = json.load(open('Test.json', 'r', encoding="utf-8"))
        for object in json_file["objects"]:
            temp_object = Object(object.get("object_name"),object.get("object_width"), object.get("object_height"), object.get("object_x"), object.get("object_y"), object.get("image_path"))
            if (temp_object.name == "player"):
                self.player_object = Player(object.get("object_name"),object.get("object_width"), object.get("object_height"), object.get("object_x"), object.get("object_y"), object.get("image_path"))
                self.Objects.add(self.player_object)
                #the commented out sections are for when the player class gets implemented. It's supposed to follow the same format as the object class since it inherits from it.
                #pass
            elif ("enemy" in temp_object.name):
                self.enemy_object = Enemy(object.get("object_name"),object.get("object_width"), object.get("object_height"), object.get("object_x"), object.get("object_y"), object.get("image_path"))
                self.Enemies.add(self.enemy_object)
            else:
                self.Objects.add(temp_object)
       
    def add_obj(self, object):
        self.Objects.add(object)
    
    def draw(self, screen):
        self.Objects.draw(screen)
        self.Enemies.draw(screen)
        self.Bullets.draw(screen)
        for object in self.Objects:
            if object.name != "player" and self.player_object.in_middle == True:
                object.move_x(-scroll_speed)
            if object.name == "player" and self.player_object.gun_fired == True:
                self.bullet_object = Bullet("bullet", 20, 20, self.player_object.x, self.player_object.y, "red_square.jpg")
                if self.player_object.direction == "right":
                    self.bullet_object.direction = "right"
                elif self.player_object.direction == "left":
                    self.bullet_object.direction = "left"
                self.Bullets.add(self.bullet_object)
                self.player_object.gun_fired = False
        
        for enemy in self.Enemies:
            if self.player_object.in_middle == True:
                enemy.move_x(-scroll_speed)
            if pygame.sprite.spritecollideany(enemy, self.Bullets):
                enemy.die()

        for bullet in self.Bullets:
            if self.bullet_object.air_time == 50:
                self.bullet_object.die()
#            if object.name == "bullet" and pygame.sprite.collide_rect(self.bullet_object, self.enemy_object):
#                self.bullet_object.die()
#                self.enemy_object.shot = True
#                print("COLLISION")
#
#            if object.name == "bullet" and self.bullet_object.air_time == 50:
#                self.bullet_object.die()
#
#            if "enemy" in object.name and self.enemy_object.shot == True:
#                self.enemy_object.die()
#                self.enemy_object.shot = False
        self.Objects.update()
        self.Enemies.update()
        self.Bullets.update()