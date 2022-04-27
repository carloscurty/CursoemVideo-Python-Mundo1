print('Desafio 008: Convertendo uma medida em metros para centímetros e milímetros')

med = input('Digite a medida em metros: ')
cent = float(med) * 100
mil = float(med) * 1000

print('{} m equivalem a {} centímetros e {} milímetros'.format(med, cent, mil))