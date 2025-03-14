from time import sleep
from machine import Pin, PWM
from random import getrandbits

servo = PWM(Pin(2), freq=400, duty=0)

try:
    while True:
        for valor in range(0,1024):
            servo.duty(valor)
            sleep(0.001)
        for valor in range(0,1024):
            servo.duty(1023 - valor)
            sleep(0.001)
            
        
except KeyboardInterrupt:
    servo.duty(0)
