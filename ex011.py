#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = altura*largura
print(f'Sua parede tem {largura}m de largura, {altura}m de altura e {area}m² de área.')
tinta = area / 2
print(f'Sendo assim, a quantidade de tinta necessária para pintar sua parede é {tinta}l')

