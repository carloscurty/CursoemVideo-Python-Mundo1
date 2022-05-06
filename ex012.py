print('Desafio 012: Mostrando preço de um produto com desconto')

preco = float(input('Qual o preço do produto? R$ '))
desco = float(input('Quanto é o desconto em %? '))
desc = preco * (desco/100)
pd = preco * (1-(desco/100))


print('Com o desconto de {:.1f}% (R$ {:.2f}), o produto que custava R$ {:.2f}, passará a custar R$ {:.2f}'.format(desc, desco, preco, pd))