# Desafio: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

print('Desafio 009: Mostrando a tabuada de um número')

num = int(input('Digite um número inteiro: '))
print('Tabuada de {}:'.format(num))
for x in range(1, 11):
    if (num * x) < 9: m = ' ' + str(num * x)
    else: m = num * x
    if x == 10:
        print('{}  X {}  = \t{}'.format(num, x, m))
    else:
        print('{}  X  {}  = \t{}'.format(num, x, m))
