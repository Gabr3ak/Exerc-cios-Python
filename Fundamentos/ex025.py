#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = str(input('Qual seu nome? ')).strip().lower().split()
print(f'Seu nome tem silva? {'silva' in nome}')
