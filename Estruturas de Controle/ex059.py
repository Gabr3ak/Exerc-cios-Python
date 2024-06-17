#Crie um programa que leia dois valores e mostre um menu na tela:
#[ 1 ] somar
#[ 2 ] multiplicar
#[ 3 ] maior
#[ 4 ] novos números
#[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
usuário = 0
soma = n1 + n2
multi = n1 * n2

while usuário != 5:
    print('''Qual tipo de operação você deseja fazer com eles?'
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    usuário = int(input('Digite sua escolha: '))
    if usuário == 1:
        print(f'{n1} + {n2} = {soma}')
    elif usuário == 2:
        print(f'{n1} x {n2} = {multi}')
    elif usuário == 3:
        if n1 > n2:
            print(f'O maior número é o {n1}.')
        else:
            print(f'O maior número é o {n2}.')
    elif usuário == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif usuário == 5:
        print('Finalizando...')
    else:
        int(input('Número inválido, tente novamente: '))
print('Fim do programa!')

