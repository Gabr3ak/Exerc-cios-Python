#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal
#e condição de pagamento:
#- à vista dinheiro/cheque: 10% de desconto
#- à vista no cartão: 5% de desconto
#- em até 2x no cartão: preço formal
#- 3x ou mais no cartão: 20% de juros

valor = float(input('Qual o valor do produto? '))
print('FORMAS DE PAGAMENTO!!!')
print('Digite 1 se quiser à vista dinheiro/cheque')
print('Digite 2 se quiser à vista no cartão')
print('Digite 3 se quiser em até 2x no cartão')
print('Digite 4 se quiser 3x ou mais no cartão')
forma = int(input('Qual será sua forma de pagamento? '))

if forma == 1:
    print(f'Sendo à vista/cheque, o valor de seu produto será de R${valor - (valor*10/100):.2f}')
elif forma == 2:
    print(f'Sendo à vista no cartão, o valor será de R${valor - (valor*5/100):.2f} ')
elif forma == 3:
    vezes = int(input('Quantas parcelas? '))
    print(f'Sendo {vezes}x, o valor será de R${valor / vezes:.2f} por parcela. ')
elif forma == 4:
    juros = valor + (valor * 20/100)
    vezes = int(input('Quantas parcelas? '))
    print(f'Sendo {vezes}x no cartão, o valor será de R${juros / vezes:.2f} com juros por parcela. ')
else:
    forma = 0
    print('Opção inválida de pagamento, tente novamente...')




