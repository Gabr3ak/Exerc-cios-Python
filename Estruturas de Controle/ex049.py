#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher,
#só que agora utilizando um laço for.

num = int(input('Escolha de qual número você deseja ver a tabuada: '))
for n in range(1, 11):
    print(f'{n} x {num} = {n*num}')
