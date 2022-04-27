# Define as variáveis de linha
lin1 = 'Primeira linha do arquivo'
lin2 = 'Segunda linha do arquivo'
linex = 'Linha Extra'

# Abre o arquivo para gravação e grava a linha 1
arq = open('texto.txt', 'a')
for x in lin1:
        arq.write(x)
arq.write('\n')
arq.close()

# Abre o arquivo para gravação e grava a linha 2
arq = open('texto.txt', 'a')
lin2 = 'Segunda linha do arquivo'
arq.seek(0, 1)
for x in lin2:
        arq.write(x)
arq.write('\n')
arq.close()

# Abre o arquivo para 'APPEND' e grava a linha extra
arq = open('texto.txt', 'a')
linex = 'Linha extra'
arq.seek(2)
for x in linex:
        arq.write(x)
arq.write('\n')
arq.close()