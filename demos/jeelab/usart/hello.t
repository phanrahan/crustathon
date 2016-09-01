${mcu.setup()}

void setup(void) 
{
}

void loop (void) 
{
    serial_puts(CONSOLE, "hello, world\n\r");
    systick_delay(1000);
}

