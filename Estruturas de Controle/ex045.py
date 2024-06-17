#Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint

jokenpo = ('PEDRA PAPEL TESOURA').split()
cpu = randint(0,2)
print('''Suas opções são:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
escolha = (int(input('PEDRA PAPEL OU TESOURA? ')))
print(f'Eu escolhi {jokenpo[cpu]} e você {jokenpo[escolha]}.')

if cpu == 0:
    if escolha == 0:
        print('Deu empate!')

    elif escolha == 1:
        print('Você ganhou!')

    elif escolha == 2:
        print('EU ganhei')

    else:
        print('Opção inválida')

elif cpu == 1:
    if escolha == 0:
        print('EU ganhei!')

    elif escolha == 1:
        print('Deu empate!')

    elif escolha == 2:
        print('Você ganhou!')

    else:
        print('Opção inválida')

elif cpu == 2:
    if escolha == 0:
        print('Você ganhou!')

    elif escolha == 1:
        print('EU ganhei!')

    elif escolha == 2:
        print('Deu empate')

    else:
        print('Opção inválida')


