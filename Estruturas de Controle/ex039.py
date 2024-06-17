#Faça um programa que leia o ano de nascimento de um jovem e informe,
#de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
#se é a hora exata de se alistar ou se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

ano = int(input('Em que ano você nasceu? '))
hoje = date.today().year
idade = hoje - ano
print(f'Se você nasceu em {ano}, então você tem {idade} anos em {hoje}.')

if idade == 18:
    print('Chegou o momento de você se alistar!')
elif idade < 18:
    print(f'Logo, ainda falta {18 - idade} anos para você se alistar!')
else:
    print(f'logo, você passou {idade - 18} anos do prazo de se alistar!')



