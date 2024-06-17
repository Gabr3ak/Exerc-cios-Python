#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
#O programa encerrará quando ele disser que quer mostrar 0 termos.

primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
termo = primeiro
contador = 1
usuário = 10
total = 0

while usuário != 0:
    total = total + usuário
    while contador <= total:
        print(f'{termo} -> ', end='')
        termo = termo + razão
        contador = contador + 1
    print('PAROU')
    usuário = int(input('Você gostaria de colocar quantos termos nessa PA? '))
print('Acabou!')








