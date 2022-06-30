import this
import operacao

this.opcao = -1

def menudeADM():
    print('1. Inserir Produtos\n' +
          '0. Sair\n')
    this.opcao = int(input('Escolha uma opção: '))

def op():
    while (this.opcao != 0):
        menudeADM()
        if this.opcao == 0:
            print('Obrigado, volte sempre!')

        elif this.opcao == 1:
            print('Insira o nome do produto: ')
            itens = input()
            print('Insira o preço do produto: ')
            preco = input()
            operacao.produtos(itens, preco)