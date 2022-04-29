# Desafio 008: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

print('Desafio 008: Convertendo uma medida em metros para centímetros e milímetros')

med = float(input('Digite a medida em metros: '))
cm = med * 100
mm = med * 1000

print('{} m equivalem a {} centímetros e {} milímetros'.format(med, cm, mm))
