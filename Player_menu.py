from os import system, name

class Menu:
    def __init__(self):
        self._array_size = 20
        self._game_speed = 1

    def get_array_size(self):
        return int(self._array_size)
    
    def get_game_speed(self):
        return int(self._game_speed)

    @staticmethod
    def clear_screen():
         # for windows
        if name == 'nt':
            _ = system('cls')
        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear') 
        return

    def display_menu_and_get_data(self): 
        self.clear_screen()
        print("hello")
        return 0