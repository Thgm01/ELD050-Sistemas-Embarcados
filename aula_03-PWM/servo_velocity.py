from time import sleep
from machine import Pin, PWM
from random import getrandbits

servo = PWM(Pin(2), freq=400, duty=0)
servo.duty(0)
velocidade='rapido'


try:
    while True:
        if velocidade == 'rapido':
            for valor in range(0,1024):
                servo.duty(valor)
                sleep(0.001)
            for valor in range(0,1024):
                servo.duty(1023 - valor)
                sleep(0.001)
            velocidade = 'lento'
            
        elif velocidade == 'lento':
            for valor in range(0,1024):
                servo.duty(valor)
                sleep(0.01)
            for valor in range(0,1024):
                servo.duty(1023 - valor)
                sleep(0.01)
            velocidade = 'rapido'
        
except KeyboardInterrupt:
    servo.duty(0)

