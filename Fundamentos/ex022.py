#Crie um programa que leia o nome completo de uma pessoa e mostre:
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.
nome = input('Digite seu nome completo: ')
dividido = nome.split()
print('Seu nome completo em minúsculas é', nome.lower())
print('Seu nome completo em maiúsculas  é', nome.upper())
print('Seu nome ao todo tem', len(nome.strip()) - nome.count(' '), 'letras')
print('Seu primeiro nome é', dividido[0], 'e tem', len(dividido[0]), 'letras')



