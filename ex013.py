# Desafio 013: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('Desafio 013: Aplicando aumento % em salário')

s = float(input('Digite o seu salário: R$ '))
a = float(input('Qual o aumento %? '))

aum = s * (a/100)
ns = s + aum

print('Com o aumento de {:.2f}%, seu salário passará de R$ {:.2f} para R$ {:.2f}'.format(a, s, ns))