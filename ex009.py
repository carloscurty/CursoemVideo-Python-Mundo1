# Desafio: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

print('Desafio 009: Mostrando a tabuada de um número')

num = int(input('Digite um número <1 - 10>: '))

print('=' * 13)
print('Tabuada de {}:'.format(num))
print('-' * 13)
for x in range(1, 11):
    m = num * x
    print('{} X  {:2} = {:2}'.format(num, x, m))
print('=' * 13)
