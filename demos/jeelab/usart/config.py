from crust import *
from crust.boards.jeelabs import JeeLabs
from crust.parts.nxp.lpc8xx import LPC810, LPC812

#board = JeeLabs(LPC810)
board = JeeLabs(LPC812)
mcu = board.mcu

board.console.on()
mcu.systick.on()

mcu.application = 'hello'
