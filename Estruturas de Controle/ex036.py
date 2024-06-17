#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: '))
salário = float(input('Salário do comprador: '))
anos = int(input('Quantos anos: '))
prestação = casa / (anos*12)
porcentagem = salário*30/100

if prestação <= porcentagem:
    print('Seu empréstimo foi APROVADO.')
else:
    print('Seu empréstimo foi NEGADO.')
