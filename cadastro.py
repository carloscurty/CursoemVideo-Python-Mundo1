# Script de cadastro, gravação e leitura

#======>>>>>> Resolver saída com '0' não processada

def inclui():
    nome = input('Nome: ')
    arq = open('cadastro.txt', 'a')
    arq.seek(2)
    arq.write(nome + '\n')
    arq.close()
    print('{} {}'.format(nome, 'cadastrado com sucesso!'))

def lista():
    arq = open('cadastro.txt', 'r')
    linha = list(arq)
    linha.sort()
    t = len(linha)
    print('{:=^50}'.format(' Foram encontrados {} nomes cadastrados: '.format(t)))
    for x in range(0, len(linha)):
        print('{}: {}'.format(x + 1, linha[x]), end='')
    print('{:=^50}'.format(' Fim do arquivo '))
    arq.close()

while True:
    print('1. Incluir | 2. Listar | 0. Sair')
    opcao = int(input('Sua opção: '))
    if opcao == 1:
        inclui()
    elif opcao == 2:
        lista()
    elif opcao == 0:
        break
print('Obrigado!')

