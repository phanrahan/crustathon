#include "clock.h"
${mcu.setup()}

void setup(void) {
}

void loop(void) {
    gpio_write(LED, true);
    systick_delay(800);

    gpio_write(LED, false);
    systick_delay(200);
}



