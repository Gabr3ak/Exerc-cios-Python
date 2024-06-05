#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
percorrido = float(input('Digite a quantidade em KM percorrida com o carro alugado: '))
dia = int(input('Digite por quantos dias o carro foi alugado? '))
valor = (dia*60)+(percorrido*0.15)
print(f'O preço a ser pago com {percorrido}km percorridos, durante {dia} dias alugados é de R${valor}')

