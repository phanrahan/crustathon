${mcu.setup()}

void setup(void) {
}

void loop(void) {
    gpio_toggle(PIO0_2);
    systick_delay(500);
}

