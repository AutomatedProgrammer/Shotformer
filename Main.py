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
#Program end condition