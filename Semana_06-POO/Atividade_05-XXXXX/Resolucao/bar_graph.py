from machine import Pin, ADC, PWM
from time import sleep

# Definição dos leds do Bar Graph
led_vd_1 = PWM(Pin(15), freq=20000, duty = 0)
led_vd_2 = PWM(Pin(4), freq=20000, duty = 0)
led_am_1 = PWM(Pin(5), freq=20000, duty = 0)
led_am_2 = PWM(Pin(19), freq=20000, duty = 0)
led_vm_1 = PWM(Pin(22), freq=20000, duty = 0)
led_vm_2 = PWM(Pin(23), freq=20000, duty = 0)

# Criando uma lista dos leds
led_list = [led_vd_1, led_vd_2, led_am_1, led_am_2, led_vm_1, led_vm_2]

# instanciando o pino do LDR
ldr = ADC(Pin(35))
ldr.atten(ADC.ATTN_11DB)

# Função para mapear um intervalo para o intervalo do pwm
def mapear_pwm(x, in_min, in_max, out_min=0, out_max=1023):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Função para atualizar o Bar Graph
def bar_graph(x, in_min, in_max, qtd_leds):
    
    # Cria uma lista de valores iniciados em zero
    led_values = list()
    for i in range(0, qtd_leds):
        led_values.append(0)
    
    # Define qual o intervalo entre cada led ficar completamente aceso
    interval = (in_max - in_min+1) / qtd_leds
    
    # Quantos leds estarão completamente aceso
    led_acionado = int(x // interval)
    
    # Mapeando o valor do led que não ficara completamente aceso
    value_pwm = int(mapear_pwm(x%interval, 0, interval))
    
    # atribui os valores dos leds que ficarão acesos completamente
    for i in range(0, led_acionado):
        led_values[i] = 1023
    
    # atribui o valor do led que ficara acionado parcialmente
    led_values[led_acionado] = int(value_pwm)
    
    #retorna a lista de valores dos leds
    return led_values
    
    
    

try:
    while True:
        # Le o valor do ldr
        valor_ldr = ldr.read()
        
        # Recebe a lista de valores de cada led
        led_values = bar_graph(valor_ldr, 0, 4095, len(led_list))
        
        # Define os valores de cada led
        led_list[0].duty(led_values[0])
        led_list[1].duty(led_values[1])
        led_list[2].duty(led_values[2])
        led_list[3].duty(led_values[3])
        led_list[4].duty(led_values[4])
        led_list[5].duty(led_values[5])
        sleep(0.1)

except KeyboardInterrupt:
    # Desliga tudo quando encerra o programa
    led_vd_1.duty(0) 
    led_vd_2.duty(0) 
    led_am_1.duty(0) 
    led_am_2.duty(0) 
    led_vm_1.duty(0) 
    led_vm_2.duty(0) 