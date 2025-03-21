from machine import Pin, ADC
import os
class ConversorAD(object):
    def __init__(self, pino=0):
        self.__adc = ADC( Pin(pino) )
        self.__adc.atten(ADC.ATTN_11DB)
        self._ADC_MAX = 4096
    def valor(self):
        return self.__adc.read()