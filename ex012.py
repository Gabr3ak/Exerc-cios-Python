#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preço = float(input('Qual o valor do seu produto? R$'))
reajuste = preço * 0.05
novo = preço - reajuste
print(f'O novo preço do seu produto com 5% de desconto é de R${novo}')

