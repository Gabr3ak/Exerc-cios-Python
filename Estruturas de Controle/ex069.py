#Crie um programa que leia a idade e o sexo de várias pessoas.
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#A) quantas pessoas tem mais de 18 anos.
#B) quantos homens foram cadastrados.
#C) quantas mulheres tem menos de 20 anos

contador = contador2 = contador3 = 0
homem = pessoas = mulheridade = 0
while True:
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo[M/F]: ')).strip().upper()[0]
    idade = int(input('Idade: '))
    if idade > 18:
        contador = contador + 1
        pessoas = contador
    if sexo == 'M':
        contador2 = contador2 + 1
        homem = contador2
    if sexo == 'F':
        if idade < 20:
            contador3 = contador + 1
            mulheridade = contador3
    pergunta = ' '
    while pergunta not in 'SN':
        pergunta = str(input('Quer continuar[S/N]? ')).strip().upper()[0]
    if pergunta == 'N':
        break
print(f'Nesse grupo, {pessoas} pessoas tem mais de 18 anos, sendo {homem} homens e {mulheridade} mulheres menores de idade.')


