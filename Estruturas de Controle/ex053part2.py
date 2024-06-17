#crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase qualquer: ')).strip().lower()
separar = frase.split()
juntar = ''.join(separar)
inverso = ''

for letra in range(len(juntar) - 1, -1, -1):
    inverso = inverso + juntar[letra]
print(f'O inverso de {juntar} é {inverso}.')

if juntar == inverso:
    print('É um palíndromo!')
else:
    print('Não é um palíndromo!')

