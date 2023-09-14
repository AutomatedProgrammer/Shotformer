from App import App
from Object import Object
from Level import Level
#from Player import Player

App = App("Shotformer", 640, 480)

Level1 = Level()
Level1.load_level("Test.json")

App.app_add_level(Level1)

App.app_running()

#TODO
#Have the camera follow the player while never letting the player pass the middle of the screen. Like in super mario bros.