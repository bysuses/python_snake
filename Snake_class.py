from enum import Enum

class Snake:

    def __init__(self, board_size, starting_point_x, starting_point_y):

        #segnent_types = ["head", "tail", "middle"]
        #directions = ["down","up","left","right"]

        class Segment_type(Enum):
            HEAD = 1
            MIDDLE = 2
            TAIL = 3

        class Direction(Enum):
            DOWN = 1
            UP = 2
            LEFT = 3
            RIGHT = 4

        self._elements = [[[starting_point_x,starting_point_y], Segment_type.HEAD]]
        self._max_coordinate = board_size

    def get_elements(self):
        return self._elements;