from time import sleep

# Importando as classes criadas 
from Potenciometro import Potenciometro
from Botao import Botao  
from LedRGB import LedRGB

# Intanciando oque sera utilizado
pot = Potenciometro(pino=35)
bot = Botao(pino=19)
rgb = LedRGB(pinoR=5, pinoG=4, pinoB=15, catodoComum=True)
    
try:
    while True:
        # Atualiza qual o estado atual
        estado = bot.estado(4)
        
        # Atualiza qual o valor do potenciometro convertido pra PWM
        brilho = pot.toPWM()
        
        # Envia qual estado atual e qual brilho queremos atribuir ao Led RGB
        rgb.estado(estado, brilho)
        sleep(0.01)
        
            
except KeyboardInterrupt:
    rgb.setRed(0)
    rgb.setGreen(0)
    rgb.setBlue(0)
    
