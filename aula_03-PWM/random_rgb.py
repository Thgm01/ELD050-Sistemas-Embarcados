from time import sleep
from machine import Pin, PWM
from random import getrandbits

tipo = 'ANODO_COMUM'
if tipo == 'CATODO"COMUM':
    MIN = 0
    MAX = 1023
else:
    MIN = 1023
    MAX = 0
    
r = PWM(Pin(5), freq=20000, duty=MIN)
g = PWM(Pin(4), freq=20000, duty=MIN)
b = PWM(Pin(15), freq=20000, duty=MIN)

try:
    while True:
        r.duty(getrandbits(10))
        g.duty(getrandbits(10))
        b.duty(getrandbits(10))
        
        sleep(1)
except KeyboardInterrupt:
    r.duty(MIN)
    g.duty(MIN)
    b.duty(MIN)
        
