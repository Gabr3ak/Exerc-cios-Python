#Desenvolva um programa que leia o comprimento de três retas e
#diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print(f'Através dessas medidas, suas retas podem formar um triângulo.')
else:
    print(f'Através dessas medidas Suas retas não podem formar um triângulo.')
