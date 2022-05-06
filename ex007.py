# Desafio 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('Desafio 007: Mostrando a média de duas notas de um aluno')

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
md = (n1 + n2) / 2

print('Sua média é: {:.2f}'.format(md))
