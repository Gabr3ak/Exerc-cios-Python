#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
#e quantas mulheres têm menos de 20 anos.

soma = 0
Média = 0
maioridade = 0
nomevelho = ''
mulheridade = 0

for p in range(1, 5):
    print(f'----- {p}ª pessoa -----')
    nome = str(input(f'Nome: '))
    idade = int(input(f'Idade: '))
    sexo = str(input(f'Sexo[M/F]: ')).upper()
    soma = soma + idade
    if p == 1 and sexo == 'M':
        maioridade = idade
        nomevelho = nome
    if sexo in 'M' and idade > maioridade:
        maioridade = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        mulheridade = mulheridade + 1


média = soma / 4
print(f'A média das idades do grupo é {média}!')
print(f'O homem mais velho tem {maioridade} anos e se chama {nomevelho}!')
print(f'Tem {mulheridade} mulheres menores de 20 anos!')



