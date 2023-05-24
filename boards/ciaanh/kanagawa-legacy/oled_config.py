import board

from kmk.extensions.peg_oled_Display import (
    Oled,
    OledData,
    OledDisplayMode,
    OledReactionType,
)


class Oled_Config:
    def __init__(self):
        self.SCL=board.GP1
        self.SDA=board.GP0
        self.oled_config = Oled(
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
    def ConfigureKeyboard(self, keyboard):
        keyboard.SCL = board.GP1
        keyboard.SDA = board.GP0
        keyboard.extensions.append(self.oled_config)

        return keyboard
