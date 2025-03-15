# Funcao para calcular a area de uma circunferencia
def areaCircunferencia(raio):
    PI = 3.14159
    area = PI*raio**2 
    return area

# Recebendo do usuario qual o raio a ser calculado
raio = float(input('Digite o raio da circinferencia: '))

# Imprimindo a resposta
print(f'A area da circunferencia de raio {raio:.2f} e {areaCircunferencia(raio):.2f}')