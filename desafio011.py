print('Desafio 011: Calcular a quantidade de tinta necessária para pintar uma parede baseado na sua área')

l = float(input('Qual a largura da parede? '))
h = float(input('Qual a altura da parede? '))
a = l * h
lt = a / 2

print('Levando em conta que cada litro de tinta pinta 2m², \nvocê irá precisar de {} litro(s) de tinta para pintar a sua parede de {} m² de área'.format(lt, a))