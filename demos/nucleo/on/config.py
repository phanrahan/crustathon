from crust import *
from crust.parts.stm.stm32f0 import STM32F030R8
from crust.boards.nucleo import Nucleo

board = Nucleo(STM32F030R8)

board.led.on()

mcu = board.mcu
mcu.application = 'on'
mcu.objects = []

