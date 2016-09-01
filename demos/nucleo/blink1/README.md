# README

    /* technical reference manual says to
       1. program reload value
       2. clear counter value
       3. program control and status registers
    */
    /*
    //uint32_t usecs_per_tick =  clock_get_frequency() / 1000000;
    uint32_t usecs_per_tick =  CLOCK_FREQUENCY / 1000000;
    systick_set_reload(1000*usecs_per_tick);
    systick_set(0); // clear counter value
    // set_clocksource seems to be necessary
    systick_set_clocksource(SYSTICK_CLOCKSOURCE_INTERNAL);
    systick_enable_interrupt();
    systick_enable_counter();
    */

void tick(void)
{
    while(1)
        if( systick_get_overflow() ) break;
}

void delay(unsigned ticks)
{
    while( ticks-- ) 
        tick();

}

void setup(void) {
}

void loop(void) {
    gpio_write(LED, true);
    systick_delay(800);
    //delay(800);

    gpio_write(LED, false);
    systick_delay(200);
    //delay(200);
}



