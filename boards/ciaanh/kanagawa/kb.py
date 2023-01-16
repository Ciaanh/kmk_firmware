import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.scanners.encoder import RotaryioEncoder
from kmk.scanners.keypad import MatrixScanner


class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = [
            MatrixScanner(
                # required arguments:
                column_pins = self.col_pins,
                row_pins = self.row_pins,
                # optional arguments with defaults:
                columns_to_anodes=DiodeOrientation.COL2ROW,
                interval=0.02,
                max_events=64
            )
        ]
    col_pins = ( board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP15, board.GP16, board.GP17, board.GP18 )
    row_pins = ( board.GP28, board.GP27, board.GP26, board.GP22, board.GP21, board.GP20)
    diode_orientation = DiodeOrientation.COLUMNS
    rgb_pixel_pin = board.GP4
    brightness_limit = 0.3
    num_pixels = 83
    SCL=board.GP1
    SDA=board.GP0
    led_key_pos = [ 12,  11, 10,  9,  8,  7,  6,  5,  4,  3,  2,  1,  0, 
                    26,  25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13,    66,
                    40,  39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27,    67,
                    53,  52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41,        68,
                    65,  64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54,        70,
                    82,  81, 80,     79, 78, 77, 76,    75, 74, 73,     72, 71, 69 
    ]
    coord_mapping = [
         0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,         13,

        14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,     55,
        28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,     69,
        42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,         83,
        56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,        68,   
        70, 71, 72,     73, 74, 75, 76,     77, 78, 79,    80, 81, 82
    ]
