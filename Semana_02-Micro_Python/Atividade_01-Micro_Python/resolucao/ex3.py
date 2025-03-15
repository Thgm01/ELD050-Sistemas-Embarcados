# Funcao que calcula o salario
def calculaSalario(salario):
    # Salario aumentado em 25%
    return salario*1.25

# recebendo do usuario o salario base para calculo
salario = float(input('Digite o salario: R$'))
print(f'O salario de R$ {salario:.2f} aumentado em 25% fica {calculaSalario(salario)}')