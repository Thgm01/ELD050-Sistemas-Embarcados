# from time import sleep
# 
# from Potenciometro import Potenciometro
# 
# pot = Potenciometro(pino=XX)
#     
# try:
#     while True:
#         print(f"Potenciometro {pot.getValue()}")
#         sleep(0.01)
# except KeyboardInterrupt:
#     print("acabou")
    
######################################################    
# from time import sleep
# 
# from Botao import Botao
# 
# bot = Botao(pino=XX)
#     
# try:
#     while True:
#         print(f"Potenciometro {bot.pressionado()}")
#         sleep(0.01)
# except KeyboardInterrupt:
#     print("acabou")

#######################################################
# from time import sleep
# 
# from LedRGB import LedRGB
# 
# rgb = LedRGB(pinoR=XX, pinoR=XX,, pinoR=XX, catodoComum=True)
#     
# try:
#     while True:
#         print(f"Potenciometro {rgb.pressionado()}")
#         sleep(0.01)
# except KeyboardInterrupt:
#     print("acabou")

###################################
# from time import sleep
# 
# from Potenciometro import Potenciometro
# from Botao import Botao  
# from LedRGB import LedRGB
# 
# pot = Potenciometro(pino=XX)
# bot = Botao(pino=XX)
# rgb = LedRGB(pinoR=XX, pinoR=XX,, pinoR=XX, catodoComum=True)
#     
# try:
#     while True:
#         estado = bot.estado(4)
#         brilho = pot.toPWM()
#         rgb.estado(estado, brilho)
#         
#             
# except KeyboardInterrupt:
#     print("acabou")