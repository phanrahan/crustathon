from crust import *
from crust.boards.nucleo import Nucleo
from crust.parts.stm.stm32f0 import STM32F030R8

board = Nucleo(STM32F030R8)

board.button.on()
board.led.on()

mcu = board.mcu
mcu.application = 'press'
mcu.objects = []

