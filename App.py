import pygame
from Level import Level
from Player import Player

class App:
    
    def __init__(self, window_name, screen_width, screen_height):
        pygame.init()
        pygame.display.set_caption(window_name)
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.running = True

        self.Levels = []

    def app_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False

    def app_add_level(self, level):
        self.Levels.append(level)

    def app_draw(self):
        self.screen.fill("white")
        for Level in self.Levels:
            Level.draw(self.screen)
            if Level.finished == True:
                self.running = False
        pygame.display.flip()

    def app_running(self):
        while self.running:
            self.app_events()
            self.app_draw()
            self.clock.tick(60)
        else:
            pygame.time.wait(1000)
            pygame.quit()
