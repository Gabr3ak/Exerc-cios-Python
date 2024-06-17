#crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase qualquer: ')).strip().lower()
inverter = frase[::-1].split()
juntar = ''.join(inverter)
print(f'Inverso de {frase} é: {juntar}')

if frase == juntar:
    print('É palíndromo.')
else:
    print('Não é palíndromo.')


