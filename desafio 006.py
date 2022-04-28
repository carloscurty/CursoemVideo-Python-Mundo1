# Desafio 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

print('Desafio 006: Mostrando o dobro, o triplo e a raiz quadrada de um número')

num = input('Digite um número: ')
dob = float(num) * 2
tri = float(num) * 3
rq = pow(float(num), (1/2))
print('O dobro de {} é {}, o triplo é {} e a raiz quadrada é {:.3f}'.format(num, dob, tri, rq))