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
        self.Player_Objects = pygame.sprite.Group()
        self.Background = pygame.sprite.Group()
        self.score = 0
        self.finished = False

    def load_level(self, image_path):
        json_file = json.load(open('Test.json', 'r', encoding="utf-8"))
        for object in json_file["objects"]:
            self.temp_object = Object(object.get("object_name"),object.get("object_width"), object.get("object_height"), object.get("object_x"), object.get("object_y"), object.get("image_path"))
            if (self.temp_object.name == "player"):
                self.player_object = Player(object.get("object_name"),object.get("object_width"), object.get("object_height"), object.get("object_x"), object.get("object_y"), object.get("image_path"))
                self.Player_Objects.add(self.player_object)
            elif ("enemy" in self.temp_object.name):
                self.enemy_object = Enemy(object.get("object_name"),object.get("object_width"), object.get("object_height"), object.get("object_x"), object.get("object_y"), object.get("image_path"))
                self.Enemies.add(self.enemy_object)
            elif (self.temp_object.name == "background"):
                self.Background.add(self.temp_object)
            elif (self.temp_object.name == "ground"):
                self.Background.add(self.temp_object)
            else:
                self.Objects.add(self.temp_object)
       
    def add_obj(self, object):
        self.Objects.add(object)
    
    def draw(self, screen):
        self.Background.draw(screen)
        self.Objects.draw(screen)
        self.Enemies.draw(screen)
        self.Bullets.draw(screen)
        self.Player_Objects.draw(screen)

        for object in self.Objects:
            if object.name == "flag" and pygame.sprite.spritecollideany(object, self.Player_Objects):
                print("Level finished.")
                print("You had " + str(self.score) + " points.")
                self.finished = True
            if self.player_object.in_middle == True:
                object.move_x(-scroll_speed) 
            if pygame.Rect.colliderect(object.rect, self.player_object.hitboxtop):
                self.player_object.move_y(self.player_object.jump_height)
                self.player_object.air_time = 50
            if pygame.Rect.colliderect(object.rect, self.player_object.hitboxbottom):
                self.player_object.move_y(-self.player_object.gravity)
                self.player_object.air_time = 0
                self.player_object.jumping = False
            if pygame.Rect.colliderect(object.rect, self.player_object.hitboxleft):
                self.player_object.move_x(self.player_object.PL_V)
            if pygame.Rect.colliderect(object.rect, self.player_object.hitboxright):
                self.player_object.move_x(-self.player_object.PL_V)
            if "question_" in object.name:
                if pygame.sprite.spritecollideany(object, self.Bullets):
                    object.die()
                    self.bullet_object.hit_something = True
                    self.score += 1
            
        for enemy in self.Enemies:
            if self.player_object.in_middle == True:
                enemy.move_x(-scroll_speed)
            if pygame.sprite.spritecollideany(enemy, self.Bullets):
                enemy.die()
                self.score += 1
            
        for background_object in self.Background:
            if self.player_object.in_middle == True:
                background_object.move_x(-scroll_speed)            

        for bullet in self.Bullets:
            if self.bullet_object.air_time == 50:
                self.bullet_object.die()
            if self.bullet_object.hit_something == True:
                self.bullet_object.die()
                self.bullet_object.hit_something = False

        if self.player_object.gun_fired == True:
            self.bullet_object = Bullet("bullet", 20, 20, self.player_object.x, self.player_object.y, "red_square.jpg")
            if self.player_object.direction == "right":
                self.bullet_object.direction = "right"
            elif self.player_object.direction == "left":
                self.bullet_object.direction = "left"
            self.Bullets.add(self.bullet_object)
            self.player_object.gun_fired = False

        for player in self.Player_Objects:
            if pygame.sprite.spritecollideany(player, self.Enemies):
                player.die()
                print("You died.")
                print("You had " + str(self.score) + " points.")
                self.finished = True
            
        
            
            
        self.Background.update()
        self.Objects.update()
        self.Enemies.update()
        self.Player_Objects.update()
        self.Bullets.update()