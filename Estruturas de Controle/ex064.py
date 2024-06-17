#Crie um programa que leia vários números inteiros pelo teclado.
#O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

contador = 0
soma = 0

num = int(input('Digite um número: '))
while num != 999:
    contador = contador + 1
    soma = soma + num
    num = int(input('Digite um número: '))
print(f'Foram digitados {contador} números!')
print(f'A soma dos números digitados é {soma}!')
