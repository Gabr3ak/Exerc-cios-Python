#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
computador = randint(0, 5)
print('Pensei em um número aqui entre 0 e 5...')
print('Tente adivinhar haha...')
usuario = int(input('Qual número eu pensei? '))
print('x'*35)
if usuario == computador:
    print('BOAA, você adivinhou, parabéns.')
else:
    print(f'haha EU ganhei, escolhi o número {computador}')

