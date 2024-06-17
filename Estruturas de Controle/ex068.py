#Faça um programa que jogue par ou ímpar com o computador.
#O jogo só será interrompido quando o jogador perder,
#mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
contador = 0
print('Vamos brincar de par ou ímpar!')

while True:
    usuário = int(input('Digite um número qualquer:'))
    computador = randint(1,11)
    soma = computador + usuário
    escolha = ' '

    while escolha not in 'PI':
        escolha = str(input('Par ou ímpar?[P/I]')).strip().upper()[0]
    print(f'Você escolheu {usuário} e eu escolhi {computador}. A soma é {soma}!')

    if escolha == 'P':
        if soma % 2 == 0:
            print(f'VOCÊ VENCEU!')
            contador = contador + 1
        else:
            print(f'VOCÊ PERDEU!')
            break
    if escolha == 'I':
        if soma % 2 == 1:
            print(f'VOCÊ VENCEU!')
            contador = contador + 1
        else:
            print(f'VOCÊ PERDEU!')
            break
print(f'Você ganhou {contador} vezes!')
