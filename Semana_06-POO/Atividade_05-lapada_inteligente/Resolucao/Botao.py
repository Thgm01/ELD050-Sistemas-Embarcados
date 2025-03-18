from machine import Pin
from time import sleep

class Botao(object):
    def __init__(self, pino):
        self.__botao = Pin(pino, Pin.IN)
        self.__estado = 0
        self.__anterior = 0
    
    def pressionado(self):
        return self.__botao.value()
    
    def estado(self, quantidade=2):
        if self.pressionado() and self.__anterior == 0:
            self.__estado = self.__estado + 1
        if self.__estado >= quantidade:
            self.__estado = 0
        self.__anterior = self.pressionado()
        sleep(0.1)
        return self.__estado
        
        