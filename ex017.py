# Exercício Python 17: Faça um programa que leia o comprimento
# do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
import math
from math import hypot
print('Exercício 017: Cálculo da hipotenusa de um triângulo retângulo')

cop = float(input('Cateto oposto: '))
cad = float(input('Cateto adjacente: '))
# hip = ((cop ** 2) + (cad ** 2)) ** (1/2) # Solução utilizando cálculo matemático
hip = math.hypot(cop, cad)  # Solução com importação de módulo

print('A hipotenusa vai medir {:.2f}'.format(hip))
