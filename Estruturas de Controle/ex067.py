#Faça um programa que mostre a tabuada de vários números,
#um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.

while True:
    num = int(input('Deseja ver a tabuada de qual número? '))
    if num < 0:
        break
    for n in range(1, 11):
        print(f'{num} x {n} = {n * num}')
print('Tabuada encerrada!!')