#Crie um programa que leia vários números inteiros pelo teclado.
#No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
#O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

usuário = 'S'
juntar = 0
contador = 0
média = 0
maior = 0
menor = 0

while usuário == 'S':
    num = int(input('Digite um número: '))
    contador = contador + 1
    juntar = juntar + num
    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        else:
            menor = num
    usuário = str(input('Quer continuar? ')).upper().strip()


print(f'A média dos números digitados é {juntar / contador}!')
print(f'O maior número digitado foi {maior} e o menor foi {menor}!')
