import supervisor
import board

from kb import KMKKeyboard
from rgb_matrix_config import RGB_Matrix_Config
from oled_config import Oled_Config
from kmk.keys import KC

from kmk.hid import HIDModes
from kmk.hid import BLEUART_Config

from kmk.modules.layers import Layers
# from kmk.modules.modtap import ModTap
from kmk.modules.encoder import EncoderHandler
from kmk.extensions.media_keys import MediaKeys

rgbConf = RGB_Matrix_Config()
oledConf = Oled_Config()

keyboard = KMKKeyboard()
keyboard.debug_enabled = False

keyboard = rgbConf.ConfigureKeyboard(keyboard)
keyboard = oledConf.ConfigureKeyboard(keyboard)

layers = Layers()
keyboard.modules.append(layers)

# modtap = ModTap()
# keyboard.modules.append(modtap)

media=MediaKeys()
keyboard.extensions.append (media)

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

CUSTOMKEY = KC.LCTL(KC.LSFT)
ENCODER = KC.MPLY

encoder_handler = EncoderHandler()
encoder_handler.pins = ((board.GP3, board.GP2, None, False),)
encoder_handler.map = [ ((KC.VOLU, KC.VOLD, XXXXXXX),), # Layer 1
                        ((KC.MNXT, KC.MPRV, XXXXXXX),), # Layer 2
                        ((XXXXXXX, XXXXXXX, XXXXXXX),), # Layer 3
                        ((XXXXXXX, XXXXXXX, XXXXXXX),), # Layer 4
                      ]
keyboard.modules.append(encoder_handler)


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