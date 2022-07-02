import this
import operacao

this.opcao = -1

def menudeADM():

    print('1. Consultar Produtos\n'        +
          '2. Inserir Produtos\n'          +
          '3. Excluir Cliente\n'           +
          '4. Excluir Produto\n'           +
          '5. Atualizar Preço\n'           +
          '6. Atualizar Nome do Produto\n' +
          '0. Sair\n')
    this.opcao = int(input('Escolha uma opção: '))

def op():
    while (this.opcao != 0):
        menudeADM()
        if this.opcao == 0:
            print('Obrigado, volte sempre!')

        elif this.opcao == 1:
            operacao.consultarprodutos()

        elif this.opcao == 2:
            print('Insira o nome do produto: ')
            itens = input()
            print('Insira o preço do produto: ')
            preco = input()
            operacao.produtos(itens, preco)

        elif this.opcao == 3:
            print('Insira o CPF do Cliente: ')
            cpf = input()
            operacao.excluirPessoa(cpf)

        elif this.opcao == 4:
            print('Insira o Codigo do Produto a ser removido: ')
            codigo = input()
            operacao.excluirProduto(codigo)

        elif this.opcao == 5:
            print('Insira o codigo do produto a ser atualizado preço: ')
            this.codigo = input()
            print('Insira o novo preço do produto: ')
            this.campo = input()
            operacao.atualizarPreco('preco', this.campo, this.codigo)

        elif this.opcao == 6:
            print('Insira o codigo do produto a ser atualizado nome: ')
            this.codigo = input()
            print('Insira o novo nome: ')
            this.campo = input()
            operacao.atualizarPreco('itens', this.campo, this.codigo)






