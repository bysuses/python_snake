import numpy
import sys
from Player_menu_class import Menu
import clear_screen_module as cls
import Snake_class as sn
import time

#variables
array_size = 0
game_speed = 0
gameboard = 0
game_over = False

#menu interaction
menu = Menu()
menu.display_menu_and_get_data()
game_speed = menu.get_game_speed()
array_size = menu.get_array_size()

#defining the gameboard
gameboard = numpy.array(array_size*[array_size*['OO']])
snake = sn.Snake(array_size, 0 , 0)
segments = snake.get_elements()
stop = 3.0/game_speed

while(not game_over):
    cls.clear_screen()
    numpy.savetxt(sys.stdout, gameboard, fmt="%.2s")
    time.sleep(stop)
