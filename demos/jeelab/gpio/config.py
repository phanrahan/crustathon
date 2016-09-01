from crust import *
from crust.parts.nxp.lpc8xx import LPC812

mcu = LPC812()

# led connected to pio0_2
mcu.pio0_2.output()
mcu.pio0_2.on()

mcu.systick.on()

mcu.application = 'blink'
