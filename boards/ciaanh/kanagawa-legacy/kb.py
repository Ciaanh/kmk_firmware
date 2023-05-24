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

    coord_mapping = [
         0,  1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12,         13,

        14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,     55,
        28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,     69,
        42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,         83,
        56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67,        68,   
        70, 71, 72,     73, 74, 75, 76,     77, 78, 79,    80, 81, 82
    ]
