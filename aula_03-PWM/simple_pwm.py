from time import sleep
from machine import Pin, PWM

led = PWM(Pin(2), freq=2000, duty=0)

for valor in range(1024):
    led.duty(valor)
    sleep(0.01)
led.duty(0)