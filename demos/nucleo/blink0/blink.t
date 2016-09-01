${mcu.setup()}

void dummy(unsigned int);

void setup(void) {
}

void loop(void) {
    gpio_write(LED, true);
    for(int ra=0;ra<800000;ra++) dummy(ra);

    gpio_write(LED, false);
    for(int ra=0;ra<200000;ra++) dummy(ra);
}



