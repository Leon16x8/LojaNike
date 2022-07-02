import this
import operacao

this.opcao = -1
this.opcao1 = -1

def menuCliente():
    operacao.consultarprodutos()
    print('0. Sair\n')

    this.opcao = int(input('Digite o codigo do produto que deseja: '))
    print('\n')

def opera():
    while (this.opcao != 0):
        menuCliente()
        if this.opcao == 0:
            print('Obrigado, volte sempre!')

        elif this.opcao == 1:
            print('Qual forma de pagamento deseja?\n ')
            print('1. PIX\n'     +
                  '2. Cartão\n'  +
                  '0. Voltar\n')
            while (this.opcao1 != 0):
                this.opcao1 = int(input('Digite o numero da opção de pagamento: '))
                if this.opcao1 == 0:
                    opera()
                elif this.opcao1 == 1:
                    print('Em Construção\n')
                elif this.opcao1 == 2:
                    print('Em Construção\n')

        elif this.opcao == 2:
            print('Qual forma de pagamento deseja?\n ')
            print('1. PIX\n' +
                  '2. Cartão\n' +
                  '0. Voltar\n')
            while (this.opcao1 != 0):
                this.opcao1 = int(input('Digite o numero da opção de pagamento: '))
                if this.opcao1 == 0:
                    opera()
                elif this.opcao1 == 1:
                    print('Em Construção\n')
                elif this.opcao1 == 2:
                    print('Em Construção\n')

        elif this.opcao == 3:
            print('Qual forma de pagamento deseja?\n ')
            print('1. PIX\n' +
                  '2. Cartão\n' +
                  '0. Voltar\n')
            while (this.opcao1 != 0):
                this.opcao1 = int(input('Digite o numero da opção de pagamento: '))
                if this.opcao1 == 0:
                    opera()
                elif this.opcao1 == 1:
                    print('Em Construção\n')
                elif this.opcao1 == 2:
                    print('Em Construção\n')











