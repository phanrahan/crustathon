${mcu.setup()}

void setup(void) {
}

void loop (void) {
    const char *cp;
    const char *hello = "hello, world\n\r";

    for( cp = hello; *cp != 0; )
        serial_putc(CONSOLE, *cp++);

    systick_delay(1000);
}
