#Escreva um programa que leia um número N inteiro qualquer
#e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.

n = int(input('Quantos termos você quer na sequência de Fibonacci? '))

a = 0
b = 1
contador = 3

print(f'{a} -> {b} ', end='')
while contador <= n:
    c = a + b
    print(f'-> {c} ', end='')
    a = b
    b = c
    contador = contador + 1
print('-> Acabou!')

