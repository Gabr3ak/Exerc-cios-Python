#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
city = str(input('Em qual cidade você mora? ')).strip()
print(city[0:5].lower() == 'santo')
