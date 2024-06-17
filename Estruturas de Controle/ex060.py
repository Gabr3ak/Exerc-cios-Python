#Faça um programa que leia um número qualquer e mostre o seu fatorial.

num = int(input('Digite um número para calcular seu fatorial: '))
contador = num
multi = 1
print(f'Calculando {num}! = ', end='')

while contador > 0:
    print(f'{contador}', end='')
    print(' x ' if contador > 1 else ' = ', end='')
    multi = multi * contador
    contador = contador - 1

print(f'{multi} ')
print(f'Ou seja, o fatorial de {num} é {multi}.')
