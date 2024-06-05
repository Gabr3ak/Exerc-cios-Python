#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Qual o salário do funcionário? R$'))
novo = salario + (salario * 15/100)
print(f'O funcionário ganhava R${salario}, com 15% de aumento, o salário foi para R${novo}')

