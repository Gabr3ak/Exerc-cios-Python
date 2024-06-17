#Escreva um programa em Python que leia um número inteiro qualquer e
#peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um número qualquer: '))
print('Você gostaria de converter esse número para qual base?')
print('Digite 1 para binário.')
print('Digite 2 para octal.')
print('Digite 3 para hexadecimal.')
base = int((input('Qual base você escolheu? ')))

if base == 1:
    print(f'{num} convertido para binário é {bin(num)[2:]}.')
elif base == 2:
    print(f'{num} convertido para octal é {oct(num)[2:]}.')
else:
    print(f'{num} convertido para hexadecimal é {hex(num)[2:]}.')



