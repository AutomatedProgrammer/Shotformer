import pygame
#from Object import Object
from Level import Level
from Player import Player

#This will be the app portion of the program. This is where the running loop will be
#and where it all comes together.
class App:
    
    def __init__(self, window_name, screen_width, screen_height):
        pygame.init()
        pygame.display.set_caption(window_name)
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.running = True
        #debug sprite group to test objects
        #self.Objects = pygame.sprite.Group()

        #Levels
        self.Levels = []
        #self.Player = Player("player", 10, 10, 50, 50, "blue_square.png")

    def app_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    #debug func to test objects
    #def app_add_obj(self, object):
        #self.Objects.add(object)

    #Add level function
    def app_add_level(self, level):
        self.Levels.append(level)

    def app_draw(self):
        self.screen.fill("white")
        #self.Objects.draw(self.screen)
        #self.Objects.update()
        for Level in self.Levels:
            Level.draw(self.screen)
        #self.screen.blit(self.Player.image, self.Player.rect)
        #self.Player.update()
        pygame.display.flip()

    def app_running(self):
        while self.running:
            self.app_events()
            self.app_draw()
            self.clock.tick(60)
        else:
            pygame.quit()
