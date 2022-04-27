print('Desafio 010: Conversão de reais em dólares')

real = float(input('Digite o valor em R$: '))
dolar = float(input('Digite o valor do dólar: '))
conv = float(real) / float(dolar)

print('Com R$ {:.2f} você pode comprar US$ {:.2f} no câmbio de R$ {:.2f}'.format(real, conv, dolar))