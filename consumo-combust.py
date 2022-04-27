print('{:=^60}'.format(' Cálculo de consumo de combustível '))

print('---- Digite os valores de compra dos combustíveis:')
pg = float(input('Gasolina: R$ '))
pa = float(input('Álcool  : R$ '))
print('{}'.format('---- Digite o consumo médio em km/L: '))
cg = float(input('Gasolina : '))
kg = pg / cg
print('\tR$ {:.2f}/Km rodado'.format(kg))
ca = float(input('Álcool   : '))
ka = pa / ca
print('\tR$ {:.2f}/km rodado'.format(ka))
print('{:.^60}'.format(' Resultado '))
if kg > ka:
    me = 'Etanol'
else:
    me = 'Gasolina'
print('Nesse caso a melhor escolha é {}'.format(me))

