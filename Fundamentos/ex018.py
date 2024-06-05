#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
ang = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print(f'O ângulo digitado foi {ang}, sendo seu SENO {sen:.2f}, COSSENO é {cos:.2f} e TANGENTE é {tan:.2f}')
