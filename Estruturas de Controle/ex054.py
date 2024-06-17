#Crie um programa que leia o ano de nascimento de sete pessoas.
#No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import datetime

maior = 0
menor = 0

for p in range(1, 8):
    ano = int(input(f'Em que ano a {p}ª pessoa nasceu? '))
    hoje = datetime.today().year
    idade = hoje - ano
    if idade >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('='*35)
print(f'{maior} pessoas atingiram a maioridade.')
print(f'{menor} pessoas NÃO atingiram a maioridade.')


