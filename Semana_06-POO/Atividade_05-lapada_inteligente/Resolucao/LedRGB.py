# Importando as bibliotecas
from machine import Pin, PWM

class LedRGB(object):
    # Construtor da classe recebe qual o Pino R, G, B e se e catodoComum
    def __init__(self, pinoR, pinoG, pinoB, catodoComum=True):
        
        # Define os valores maximos e minimos dependendo se e cadoto ou anodo comum
        self.__min = 0 if catodoComum else 1023
        self.__max = 1023 if catodoComum else 0
        
        # Instancia os leds e seus atributos iniciando desligado
        self.__colorRed = PWM(Pin(pinoR), freq=20000, duty=self.__min)
        self.__colorGreen = PWM(Pin(pinoG),freq=20000, duty=self.__min)
        self.__colorBlue = PWM(Pin(pinoB), freq=20000, duty=self.__min)
        
    def setRed(self, value):
        # Verifica se está no range do PWM e define o duty do Led Red
        if(value > 1023):
            value = 1023
        elif (value < 0):
            value = 0
        self.__colorRed.duty(value)
    
    def setGreen(self, value):
        # Verifica se está no range do PWM e define o duty do Led Green
        if(value > 1023):
            value = 1023
        elif (value < 0):
            value = 0
        self.__colorGreen.duty(value)
    
    def setBlue(self, value):
        # Verifica se está no range do PWM e define o duty do Led Blue
        if(value > 1023):
            value = 1023
        elif (value < 0):
            value = 0
        self.__colorBlue.duty(value)
        
    def estado(self, estado, brilho):
        # Alterna entre os estados definindo os brilhos de cada um
        
        # Tudo desligado
        if estado == 0:
            self.setRed(self.__min)
            self.setGreen(self.__min)
            self.setBlue(self.__min)
        
        # Led Vermelho aceso
        if estado == 1:
            self.setRed(brilho)
            self.setGreen(self.__min)
            self.setBlue(self.__min)
            
        # Led Verde aceso
        if estado == 2:
            self.setRed(self.__min)
            self.setGreen(brilho)
            self.setBlue(self.__min)
        
        # Led Azul aceso
        if estado == 3:
            self.setRed(self.__min)
            self.setGreen(self.__min)
            self.setBlue(brilho)