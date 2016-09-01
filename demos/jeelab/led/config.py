from crust import *
from crust.parts.nxp.lpc8xx import LPC812
from crust.parts.generic.led import LED

mcu = LPC812()
led = LED('LED')

wire( mcu.pio0_2.O, led.I )
led.on()

mcu.systick.on()

mcu.application = 'blink'
