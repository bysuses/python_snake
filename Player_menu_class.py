import sys
import clear_screen_module as cls

class Menu:
    def __init__(self):
        self._array_size = 20
        self._game_speed = 1

    def get_array_size(self):
        return int(self._array_size)
    
    def get_game_speed(self):
        return int(self._game_speed)

    def _acquire_size(self):
        cls.clear_screen()
        print("Enter the gameboard size (between 10 and 40) :")
        x = input()
        try: 
            x = int(x)
        except ValueError: 
            x = self._acquire_size()
        if(x < 10 or x > 40):
            x = self._acquire_size()
        return x

    def _acquire_speed(self):
        cls.clear_screen()
        print("Type the game speed (1 or 2 or 3) and press enter:")
        x = input()
        try: 
            x = int(x)
        except ValueError: 
            x = self._acquire_speed()
        if(x not in [1, 2, 3]):
            x = self._acquire_speed()
        return x

    def display_menu_and_get_data(self): 
        self._array_size = self._acquire_size()
        self._game_speed = self._acquire_speed()
        return 0