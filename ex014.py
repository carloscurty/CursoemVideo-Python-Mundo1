# Desafio 014: Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

print('Desafio 014: Conversão de temperaturas - ºC para ºF')

c = float(input('Digite a temperatura em ºC: '))
f = ((9 * c)/5) + 32
print(' {:.1f}ºC correspondem a {:.1f}ºF'.format(c, f))
