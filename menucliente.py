import this
import operacao

this.opcao = -1

def menuCliente():
    operacao.consultarprodutos()
    print('0. Sair\n')

    this.opcao = int(input('Digite o numero do produto que deseja: '))

def opera():
    while (this.opcao != 0):
        menuCliente()
        if this.opcao == 0:
            print('Obrigado, volte sempre!')







