#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

n = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

menor = n
if n2 < n and n2 < n3:
    menor = n2
if n3 < n and n3 < n2:
    menor = n3

maior = n
if n2 > n and n2 > n3:
    maior = n2
if n3 > n and n3 > n2:
    maior = n3
print(f'O maior número é {maior}.')
print(f'O menor número é {menor}.')



