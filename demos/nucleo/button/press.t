${mcu.setup()}

void setup(void) {
}

void loop(void) {
    led_write( LED, button_read(USER) );
}

