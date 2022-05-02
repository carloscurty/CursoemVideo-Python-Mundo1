print('Desafio 011: Calcular a quantidade de tinta necessária para pintar uma parede baseado na sua área')

l = float(input('Qual a largura da parede? '))
h = float(input('Qual a altura da parede? '))
a = l * h
lt = a / 2
print('-'*51)
print('Levando em conta que cada litro de tinta pinta 2m², \nvocê irá precisar de {:.1f} litro(s) de tinta\npara pintar a sua parede de {:.1f} m² de área'.format(lt, a))