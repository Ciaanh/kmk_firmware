import supervisor
import board

from kb import KMKKeyboard
from kmk.keys import KC

from kmk.hid import HIDModes
from kmk.hid import BLEUART_Config

from kmk.extensions.peg_oled_Display import (
    Oled,
    OledData,
    OledDisplayMode,
    OledReactionType,
)
from kmk.extensions.peg_rgb_matrix import Rgb_matrix

from kmk.modules.layers import Layers
# from kmk.modules.modtap import ModTap
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

keyboard = KMKKeyboard()
keyboard.debug_enabled = False



layers = Layers()
# modtap = ModTap()
encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP3, board.GP2, None, False),)

keyboard.modules = [layers, encoder_handler] # modtap

oled_ext = Oled(
    OledData(
        corner_one={0: OledReactionType.STATIC, 1: ['Base']},
        corner_two={
            0: OledReactionType.LAYER,
            1: ['1', '2', '3', '4', '5', '6', '7', '8'],
        },
        corner_three={
            0: OledReactionType.LAYER,
            1: ['base', 'lower', 'upper', 'function', '5', '6', '7', '8'],
        },
        corner_four={
            0: OledReactionType.LAYER,
            1: ['kanagawa', 'nums', 'shifted', 'leds', '5', '6', '7', '8'],
        },
    ),
    toDisplay=OledDisplayMode.TXT,
    flip=False,
)


# Colors https://htmlcolorcodes.com/fr/
#  85,  0,255     Purple
#   0,255,  0     Green
# 255,  0,  0     Red
# 255,255,  0     Yellow
#   0,255,255     Cyan
#   0,234,255     Cyan 2
# 255,  0,255     Magenta
# 255,255,255     White
# 255,165,  0     Orange
# 128,  0,128     Purple
#   0,128,128     Teal
# 128,128,128     Gray
# 192,192,192     Silver
# 128,128,  0     Olive
# 199,  0, 57     Dark Red
# 255,195,  0     Gold 


rgb_ext = Rgb_matrix(
    ledDisplay=[
        #  0,   1,  2,  3,  4,  5,  6,  7,  8,  9, 10, 11, 12, 
        # 13,  14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26,    27,
        # 28,  29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,    42,
        # 43,  44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55,        56,
        # 57,  58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68,        69,
        # 70,  71, 72,     73, 74, 75, 76,    77, 78, 79,     80, 81, 82 
        
        # Row 1
        [192,192,192],     # 0
        [ 85,  0,255],     # 1
        [ 85,  0,255],     # 2
        [ 85,  0,255],     # 3
        [ 85,  0,255],     # 4
        [ 85,  0,255],     # 5
        [ 85,  0,255],     # 6
        [ 85,  0,255],     # 7
        [ 85,  0,255],     # 8
        [ 85,  0,255],     # 9
        [ 85,  0,255],     # 10
        [ 85,  0,255],     # 11
        [ 85,  0,255],     # 12

        # Row 2
        [192,192,192],     # 13
        [128,  0,128],     # 14
        [128,  0,128],     # 15
        [128,  0,128],     # 16
        [128,  0,128],     # 17
        [128,  0,128],     # 18
        [128,  0,128],     # 19
        [128,  0,128],     # 20
        [128,  0,128],     # 21
        [128,  0,128],     # 22
        [128,  0,128],     # 23
        [128,  0,128],     # 24
        [128,  0,128],     # 25
        [192,192,192],     # 26
        [  0,234,255],     # 27
        
        # Row 3
        [192,192,192],     # 28
        [128,  0,128],     # 29
        [128,  0,128],     # 30
        [128,  0,128],     # 31
        [128,  0,128],     # 32
        [128,  0,128],     # 33
        [128,  0,128],     # 34
        [128,  0,128],     # 35
        [128,  0,128],     # 36
        [128,  0,128],     # 37
        [128,  0,128],     # 38
        [128,  0,128],     # 39
        [128,  0,128],     # 40
        [128,  0,128],     # 41
        [  0,234,255],     # 42

        # Row 4
        [192,192,192],     # 43
        [128,  0,128],     # 44
        [128,  0,128],     # 45
        [128,  0,128],     # 46
        [128,  0,128],     # 47
        [128,  0,128],     # 48
        [128,  0,128],     # 49
        [128,  0,128],     # 50
        [128,  0,128],     # 51
        [128,  0,128],     # 52
        [128,  0,128],     # 53
        [128,  0,128],     # 54
        [192,192,192],     # 55
        [  0,234,255],     # 56

        # Row 5
        [192,192,192],     # 57
        [128,  0,128],     # 58
        [128,  0,128],     # 59
        [128,  0,128],     # 60
        [128,  0,128],     # 61
        [128,  0,128],     # 62
        [128,  0,128],     # 63
        [128,  0,128],     # 64
        [128,  0,128],     # 65
        [128,  0,128],     # 66
        [128,  0,128],     # 67
        [192,192,192],     # 68
        [255,195,  0],     # 69

        # Row 6
        [192,192,192],     # 70
        [192,192,192],     # 71
        [192,192,192],     # 72
        [255,  0,255],     # 73
        [  0,234,255],     # 74
        [  0,234,255],     # 75
        [255,  0,255],     # 76
        [192,192,192],     # 77
        [192,192,192],     # 78
        [192,192,192],     # 79
        [255,195,  0],     # 80
        [255,195,  0],     # 81
        [255,195,  0],     # 82      
    ],
    disable_auto_write=True,
)
media=MediaKeys()
keyboard.extensions = [media, oled_ext, rgb_ext]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

CUSTOMKEY = KC.LCTL(KC.LSFT)
ENCODER = KC.MPLY

encoder_handler.map = [ ((KC.VOLU, KC.VOLD, XXXXXXX),), # Layer 1
                        ((KC.MNXT, KC.MPRV, XXXXXXX),), # Layer 2
                        ((XXXXXXX, XXXXXXX, XXXXXXX),), # Layer 3
                        ((XXXXXXX, XXXXXXX, XXXXXXX),), # Layer 4
                      ]

keyboard.keymap = [
    [   # BASE
        KC.ESC,   KC.F1,      KC.F2,      KC.F3,      KC.F4,   KC.F5,   KC.F6,   KC.F7,   KC.F8,   KC.F9,  KC.F10,  KC.F11,  KC.F12,              ENCODER,
       
         KC.GRV,   KC.N1,      KC.N2,      KC.N3,      KC.N4,   KC.N5,   KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0, KC.MINS,  KC.EQL, KC.BSPC,      KC.DEL,  
         KC.TAB,    KC.Q,       KC.W,       KC.E,       KC.R,    KC.T,    KC.Y,    KC.U,    KC.I,    KC.O,    KC.P, KC.LBRC, KC.RBRC, KC.BSLS,     KC.HOME,  
        KC.CAPS,    KC.A,       KC.S,       KC.D,       KC.F,    KC.G,    KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.QUOT,  KC.ENT,               KC.END,  
        KC.LSFT,    KC.Z,       KC.X,       KC.C,       KC.V,    KC.B,    KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.RSFT,                KC.UP,           
        KC.LCTL, KC.LGUI,    KC.LALT,         KC.MO(1),  KC.SPC,        KC.SPC,   KC.MO(2),       KC.RALT,KC.TG(3), KC.RCTL,     KC.LEFT, KC.DOWN, KC.RGHT, 
    ],

    [   # Lower
        _______, _______,    _______,    _______,    _______, _______, _______, _______, _______, _______, _______, _______, _______,              _______,
       
        _______, _______,    _______,    _______,    _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,     _______,  
        _______, _______,    _______,    _______,    _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,     _______,  
        _______, _______,    _______,    _______,    _______, _______, _______, _______, _______, _______, _______, _______, _______,              _______,  
        _______, _______,    _______,    _______,    _______, _______, _______, _______, _______, _______, _______, _______,              _______,           
        _______, _______,    _______,         KC.MO(1), _______,       _______,   KC.MO(2),       _______,KC.TG(3), _______,     _______, _______, _______, 
    ],

    [   # Upper
        _______, _______,    _______,    _______,    _______, _______, _______, _______, _______, _______, _______, _______, _______,              _______,
       
        _______, _______,    _______,    _______,    _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,     _______,  
        _______, _______,    _______,    _______,    _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,     _______,  
        _______, _______,    _______,    _______,    _______, _______, _______, _______, _______, _______, _______, _______, _______,              _______,  
        _______, _______,    _______,    _______,    _______, _______, _______, _______, _______, _______, _______, _______,              _______,           
        _______, _______,    _______,         KC.MO(1), _______,       _______,   KC.MO(2),       _______,KC.TG(3), _______,     _______, _______, _______, 
    ],

    [   # Code
        _______, _______,    _______,    _______,    _______, _______, _______, _______, _______, _______, _______, _______, _______,              _______,
       
        _______, _______,    _______,    _______,    _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,     _______,  
        _______, _______,    _______,    _______,    _______, _______, _______, _______, _______, _______, _______, _______, _______, _______,     _______,  
        _______, _______,    _______,    _______,    _______, _______, _______, _______, _______, _______, _______, _______, _______,              _______,  
        _______, _______,    _______,    _______,    _______, _______, _______, _______, _______, _______, _______, _______,              _______,           
        _______, _______,    _______,         KC.MO(1), _______,       _______,   KC.MO(2),       _______,KC.TG(3), _______,     _______, _______, _______, 
    ],
]




# uart = BLEUART_Config()
# uart.tx=board.GP0,
# uart.rx=board.GP1,
# uart.gpio0=board.GP9,
# uart.chip_select=board.GP13,
# uart.busy=board.GP14,
# uart.reset=board.GP15,
# if __name__ == '__main__':
#     keyboard.go(
#         hid_type=HIDModes.BLE,
#         ble_name='Antikythera',
#         uart_config=uart
#     )

if __name__ == '__main__':
    keyboard.go()