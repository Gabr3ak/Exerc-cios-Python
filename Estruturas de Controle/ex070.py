#Crie um programa que leia o nome e o preço de vários produtos.
#O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato.

contador = contador2 = 0
soma = p1000 = menor = 0
barato = ' '

while True:
    nome = str(input('Nome do produto: ')).strip().upper()
    preço = float(input('Preço: R$'))
    soma = soma + preço
    contador = contador + 1
    if preço > 1000:
        contador2 = contador2 + 1
        p1000 = contador2
    if contador == 1:
        menor = preço
        barato = nome
    else:
        if preço < menor:
            menor = preço
            barato = nome
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
    if pergunta == 'N':
        break
print(f'O total gasto nesses produtos foi de R${soma:.2f}!')
print(f'{p1000} custam mais de R$1000 reais!')
print(f'O nome do produto com menor preço é {barato}, que custa R${menor:.2f}!')


