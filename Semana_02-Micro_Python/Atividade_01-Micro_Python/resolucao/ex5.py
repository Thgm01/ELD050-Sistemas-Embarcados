def eVogal(caracter):
    # Se o caracter estiver dentro da string ele entra no if
    if caracter in 'aeiou':
        print(f'O caracter {caracter} e uma vogal')
    # Se nao for 'aeiou' ele verifica se e 'y'
    elif caracter == 'y':
        print(f'O caracter {caracter} pode ser uma vogal ou nao depedendo da sua lingua')
    # Caso contrario ele e vogal
    else:
        print(f'O caracter {caracter} e uma consoante')
        
caracter = input('Digite uma letra do alfabeto: ').lower()
eVogal(caracter)