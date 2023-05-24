import board

from kmk.extensions.peg_rgb_matrix import Rgb_matrix

# Colors https://htmlcolorcodes.com/fr/
    
# Green = [  0,255,  0]
# Red = [255,  0,  0]
# Yellow = [255,255,  0]
# Cyan = [  0,255,255]
# White = [255,255,255]
# Orange = [255,165,  0]     
# Teal = [  0,128,128]
# Gray = [128,128,128]
# Olive = [128,128,  0]
# DarkRed = [199,  0, 57]


Gold = [255,195,  0] 
Pink = [128,  0,128]
Purple = [ 85,  0,255]
Silver = [192,192,192]
Cyan = [  0,234,255]
Magenta = [255,  0,255]

class RGB_Matrix_Config:
    def __init__(self):
        self.rgb_pixel_pin = board.GP4
        self.brightness_limit = 0.3
        self.num_pixels = 83
        self.led_key_pos = [ 
            12,  11, 10,  9,  8,  7,  6,  5,  4,  3,  2,  1,  0, 
            26,  25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13,    66,
            40,  39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27,    67,
            53,  52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41,        68,
            65,  64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54,        70,
            82,  81, 80,     79, 78, 77, 76,    75, 74, 73,     72, 71, 69 
        ]
        self.rgb_values = [
            #  0,   1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 
            # 13,  14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,    27,
            # 28,  29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,    42,
            # 43,  44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,        56,
            # 57,  58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68,        69,
            # 70,  71, 72,     73, 74, 75, 76,    77, 78, 79,     80, 81, 82 
            
            # Row 1
            Silver,     # 0
            Purple,     # 1
            Purple,     # 2
            Purple,     # 3
            Purple,     # 4
            Purple,     # 5
            Purple,     # 6
            Purple,     # 7
            Purple,     # 8
            Purple,     # 9
            Purple,     # 10
            Purple,     # 11
            Purple,     # 12

            # Row 2
            Silver,     # 13
            Pink,     # 14
            Pink,     # 15
            Pink,     # 16
            Pink,     # 17
            Pink,     # 18
            Pink,     # 19
            Pink,     # 20
            Pink,     # 21
            Pink,     # 22
            Pink,     # 23
            Pink,     # 24
            Pink,     # 25
            Silver,     # 26
            Cyan,     # 27
            
            # Row 3
            Silver,     # 28
            Pink,     # 29
            Pink,     # 30
            Pink,     # 31
            Pink,     # 32
            Pink,     # 33
            Pink,     # 34
            Pink,     # 35
            Pink,     # 36
            Pink,     # 37
            Pink,     # 38
            Pink,     # 39
            Pink,     # 40
            Pink,     # 41
            Cyan,     # 42

            # Row 4
            Silver,     # 43
            Pink,     # 44
            Pink,     # 45
            Pink,     # 46
            Pink,     # 47
            Pink,     # 48
            Pink,     # 49
            Pink,     # 50
            Pink,     # 51
            Pink,     # 52
            Pink,     # 53
            Pink,     # 54
            Silver,     # 55
            Cyan,     # 56

            # Row 5
            Silver,     # 57
            Pink,     # 58
            Pink,     # 59
            Pink,     # 60
            Pink,     # 61
            Pink,     # 62
            Pink,     # 63
            Pink,     # 64
            Pink,     # 65
            Pink,     # 66
            Pink,     # 67
            Silver,     # 68
            Gold,     # 69

            # Row 6
            Silver,     # 70
            Silver,     # 71
            Silver,     # 72
            Magenta,     # 73
            Cyan,     # 74
            Cyan,     # 75
            Magenta,     # 76
            Silver,     # 77
            Silver,     # 78
            Silver,     # 79
            Gold,     # 80
            Gold,     # 81
            Gold,     # 82      
        ]
    def ConfigureKeyboard(self, keyboard):

        keyboard.rgb_pixel_pin = self.rgb_pixel_pin
        keyboard.brightness_limit = self.brightness_limit
        keyboard.num_pixels = self.num_pixels
        keyboard.led_key_pos = self.led_key_pos

        keyboard.extensions.append(
            Rgb_matrix(
                ledDisplay = self.rgb_values,
                disable_auto_write = True,
            )
        )


        return keyboard