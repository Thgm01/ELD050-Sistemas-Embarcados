from time import sleep
from machine import Pin, PWM

led_r = PWM(Pin(15), freq=2000, duty=0)
led_g = PWM(Pin(4), freq=2000, duty=0)
led_b = PWM(Pin(5), freq=2000, duty=0)

try:
    while True:
        led_r.duty(0)
        sleep(1)
        led_g.duty(0)
        sleep(1)
        led_b.duty(0)
        sleep(1)
        
        led_r.duty(1023)
        led_g.duty(1023)
        led_b.duty(1023)
        
        #for valor in range(1024):
        #    led.duty(valor)
        #    sleep(0.001)
        #led.duty(0)
except KeyboardInterrupt:
    pass