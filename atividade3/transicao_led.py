from time import sleep
from machine import Pin, PWM

# Definindo os valores maximos e minimos do PWM dos leds
MIN = 0
MAX = 1023

# Variavel global para o estado atual
atual_state = 0

# Iniciando os leds de forma apagada
led_b = PWM(Pin(2), freq=20000, duty=MIN)
led_g = PWM(Pin(4), freq=20000, duty=MIN)
led_r = PWM(Pin(5), freq=20000, duty=MIN)

# Instanciando o botao
bot = Pin(19, Pin.IN)

# Funcao para interrupcao do botao
def handle_interrupt(pin):
    print("mudando de estado")
    sleep(0.5)
    
# Conectar o evento do botao apertado com a interrupcao do sistema
bot.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

class StateMachine():
    def __init__(self, delay):
        self.states = ((MIN, MIN, MIN),(MAX, MIN, MIN), (MIN, MAX, MIN), (MIN, MIN, MAX), (MAX, MIN, MIN))
        self.delay = delay
        self.atual_dutty = [MIN, MIN, MIN]
    
    def run(self):
        global atual_state
        while True:
            while not self.finished_state():
                if self.atual_dutty[0] != self.states[atual_state-1][0]:
                    self.atual_dutty[0] += 1 * round((abs(self.states[atual_state-1][0] - self.atual_dutty[0])/(self.states[atual_state-1][0] - self.atual_dutty[0] - 1e-5)))
                if self.atual_dutty[1] != self.states[atual_state-1][1]:
                    self.atual_dutty[1] += 1 * round((abs(self.states[atual_state-1][1] - self.atual_dutty[1])/(self.states[atual_state-1][1] - self.atual_dutty[1] - 1e-5)))                
                if self.atual_dutty[2] != self.states[atual_state-1][2]:
                    self.atual_dutty[2] += 1 * round((abs(self.states[atual_state-1][2] - self.atual_dutty[2])/(self.states[atual_state-1][2] - self.atual_dutty[2] - 1e-5)))
                
                led_r.duty(self.atual_dutty[0])
                led_g.duty(self.atual_dutty[1])
                led_b.duty(self.atual_dutty[2])
                sleep(self.delay)
                
            self.update_state()                
                
                
            
    def finished_state(self):
        global atual_state
        for i in range(3):
            if self.atual_dutty[i] != self.states[atual_state-1][i]:

                
                return False
        return  True
    
    def update_state(self):
        global atual_state
        if(atual_state == 1):
            atual_state = 2
        elif(atual_state == 2):
            atual_state = 3
        elif(atual_state == 3):
            atual_state = 4
        elif(atual_state == 4):
            atual_state = 5
        elif(atual_state == 5):
            atual_state = 3
            
            
sm = StateMachine(0.01)

try:
    sm.run()
     
except KeyboardInterrupt:
    led_r.duty(MIN)
    led_g.duty(MIN)
    led_b.duty(MIN)