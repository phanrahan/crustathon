${mcu.setup()}

void setup(void) {
}

void loop(void) {
    led_write(LED, true);
    systick_delay(800);

    led_write(LED, false);
    systick_delay(200);
}



