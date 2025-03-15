from time import sleep
from machine import Pin

# Variavel para guardar se o pedestre chamou
pedestre_chamou = False

# Definicao dos pinos dos leds do semaforo
sem_car_verm = Pin(2, Pin.OUT)
sem_car_ama  = Pin(4, Pin.OUT)
sem_car_verd = Pin(5, Pin.OUT)

sem_ped_verm = Pin(19, Pin.OUT)
sem_ped_verd = Pin(21, Pin.OUT)

# Definicao do pino do botao
bot_pedestre = Pin(23, Pin.IN)

# Definicao dos estados
states = ((0, 0, 0, 0, 0), (0, 0, 1, 1, 0), (0, 1, 0, 1, 0), (1, 0, 0, 1, 0), (1, 0, 0, 0, 1), (0, 0, 1, 1, 0), (0, 1, 0, 1, 0))
timers = (0, 10, 5, 7, 8, 5, 10)

# variavel para guardar o estado atual
atual_state = 1

# Funcao para atualizar todos os leds
def setSemaforo(values):
    sem_car_verm.value(values[0])
    sem_car_ama.value(values[1])
    sem_car_verd.value(values[2])
    sem_ped_verm.value(values[3])
    sem_ped_verd.value(values[4])

# Funcao para atualizacao dos estados da maquina de estados
def update_state_machine():
    global atual_state
    global pedestre_chamou
    
    if(atual_state == 1):
        atual_state = 2
    
    elif(atual_state == 2):
        if (pedestre_chamou):
            atual_state = 4
            pedestre_chamou = False        
        else:
            atual_state = 3
            
    elif(atual_state == 3):
        atual_state = 1
    
    
    elif(atual_state == 4):
        atual_state = 5
    
    elif(atual_state == 5):
        atual_state = 6
    
    elif(atual_state == 6):
        atual_state = 3
    
# Funcao para interrupcao do botao
def handle_interrupt(pin):
    global pedestre_chamou
    pedestre_chamou = True
    print("Pedestre pediu o semaforo")

# Conectar o evento do botao apertado com a interrupcao do sistema
bot_pedestre.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

# Codigo Main
try:
    while True:
        print(atual_state)
        setSemaforo(states[atual_state])
        sleep(timers[atual_state])
        update_state_machine()

except KeyboardInterrupt:
    setSemaforo(states[0])
