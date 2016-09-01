from crust import *
from crust.boards.nucleo import Nucleo
from crust.parts.stm.stm32f0 import STM32F030R8

board = Nucleo(STM32F030R8)
mcu = board.mcu

mcu.systick.on()
board.console.on()

mcu.application = 'hello'
mcu.objects = []


