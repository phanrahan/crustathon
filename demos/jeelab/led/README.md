# README

This is a simple program illustrating the use of `crust`
with the NXP LPC8xx family of Cortex M0+ processors.

`config.py` creates an LPC812 and a LED.
The LED is wired to pio0_2.
Finally, the LED and systick peripheral are turned on.

`blink.t` is the application that blinks the LED on pio0_2.

