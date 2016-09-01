from crust import *
from crust.boards.jeelabs import JeeLabs
from crust.parts.nxp.lpc8xx import LPC810, LPC812, LPC824
from crust.parts.generic.led import LED

#board = JeeLabs(LPC810)
board = JeeLabs(LPC812)
#board = JeeLabs(LPC824)
mcu = board.mcu

board.led.on()

mcu.application = 'on'

