# Funcao para calcular a area de um triangulo
def areaTriangulo(base, altura):
    area = base*altura/2
    return area
    
# Recebendo do usuario qual a base do triangulo a ser calculado
base = float(input('Digite a base do traingulo: '))

# Recebendo do usuario qual a altura do triangulo a ser calculado
altura = float(input('Digite a altura do traingulo: '))
print(f'A area do triangulo de base {base:.2f} e altura de {altura:.2f} equivale a {areaTriangulo(base, altura):.2f}')