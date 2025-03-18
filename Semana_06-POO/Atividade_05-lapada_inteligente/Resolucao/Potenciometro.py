from ConversorAD import ConversorAD

class Potenciometro(ConversorAD):
    def __init__(self, pino=0):
        super().__init__(pino)
    
    def __mapear(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min
    
    def escalonar(self, min=0, max=1):
        return int(self.__mapear(self.valor(), 0, self._ADC_MAX, min, max))
    
    def toPWM(self):
        valorADC = self.getValor()
        valorPWM = self.__mapear(valorADC, 0, self._ADC_MAX, 0, 1023)
        return valorPWM
