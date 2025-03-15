# Funcao para converter fahrenheit para celcius
def fahrenheitParaCelcius(temperaturaFahrenheit):
    temperaturaCelcius = 5 * (temperaturaFahrenheit - 32) / 9
    return temperaturaCelcius

# Recebendo do usuario a temperatura em fahrenheit para conversao
temperaturaFahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
print(f'A temperatura de {temperaturaFahrenheit:.2f} °F equivale a {fahrenheitParaCelcius(temperaturaFahrenheit):.2f}')