# Importa o conversor AD
from ConversorAD import ConversorAD

class Potenciometro(ConversorAD):
    def __init__(self, pino=0):
        super().__init__(pino)
    
    def __mapear(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    def escalonar(self, min=0, max=1):
        return int(self.__mapear(self.valor(), 0, self._ADC_MAX, min, max))
    
    # Convertendo para PWM
    def toPWM(self):
        valor_pwm = self.escalonar(min=0, max=1023)
        return valor_pwm