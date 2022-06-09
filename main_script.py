import numpy
import sys
import Player_menu

#variables
array_size = 0
game_speed = 0
gameboard = 0
#gameboard = numpy.array(array_size*[array_size*['OO']])
menu = Player_menu.Menu()
menu.display_menu_and_get_data()
game_speed = menu.get_game_speed()
array_size = menu.get_array_size()
#numpy.savetxt(sys.stdout, gameboard, fmt="%.2s")

