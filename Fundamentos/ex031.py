#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 para viagens mais longas.

dis = float(input('Qual a distância da sua viagem? '))
print(f'Você fará um viagem de {dis}km')
if dis <= 200:
    print(f'Logo, sua passagem custará R${dis*0.50:.2f}')
else:
    print(f'Logo, sua passagem custará R${dis*0.45:.2f}')


