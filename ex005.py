# Exercício 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

print('Desafio 005: Mostrando o antecessor e o sucessor de um número')

num = int(input('Digite um número inteiro: '))
ant = num - 1
suc = num + 1
print("O antecessor de {} é {} e o seu sucessor é {}".format(num, ant, suc))