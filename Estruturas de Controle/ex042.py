#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes

r1 = float(input('Comprimento da primeira reta: '))
r2 = float(input('Comprimento da segunda reta: '))
r3 = float(input('Comprimento da terceira reta: '))

if r1 == r2 == r3:
    print('Seu triângulo é do tipo EQUILÁTERO.')
elif r1 != r2 != r3 != r1:
    print('Seu triângulo é do tipo ESCALENO.')
else:
    print('Seu triãngulo é do tipo ISÓSCELES.')

