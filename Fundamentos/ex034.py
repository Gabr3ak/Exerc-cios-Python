#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual seu salário? '))
aumento = (salario*10)/100
aumento2 = (salario*15)/100
if salario <= 1250:
    print(f'Seu salário teve um aumento de 15%, ficando R${salario+aumento2:.2f} ')
else:
    print(f'Seu salário teve um aumento de 10%, ficando R${salario+aumento:.2f}')

