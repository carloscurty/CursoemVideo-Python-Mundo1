nome = input('Qual é seu nome? ')
print('Prazer em te conhecer, {}!'.format(nome))

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
rq = pow(n1, (1/n2))
print('A soma é {}, a multiplicação é {}, a divisão é {}'.format(s, m, d))
print('A divisão inteira é {}, {} elevado a {} é {}'.format(di, n1, n2, e))
print('A raiz {} de {} é {}'.format(n2, n1, rq))