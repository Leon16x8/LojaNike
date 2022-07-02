import operacao
import this

this.opcao = -1


def menu():
    print('\n|----------NIKE----------|\n' +
          'Escolha uma das opções abaixo: \n\n' +
          '1. Login\n'             +
          '2. Cadastro\n'          +
          '0. Sair\n')
    this.opcao = int(input('Escolha uma opção: '))

def operar():
    while (this.opcao != 0):
        menu()
        if this.opcao == 0:
            print('Obrigado!')

        elif this.opcao == 1:
            print('Digite seu Login: ')
            this.loginn = input()
            print('Digite sua Senha: ')
            this.senhaa = input()
            operacao.consultalogin(this.loginn, this.senhaa)

        elif this.opcao == 2:
            print('Informe seu CPF: ')
            cpf = input()
            print('Informe seu Nome:')
            nome = input()
            print('Informe um Nome de Usuario: ')
            login = input()
            print('Informe uma Senha: ')
            senha = input()
            print('Informe seu E-mail: ')
            email = input()
            operacao.cadastro(cpf, nome, login, senha, email)

        elif this.opcao == 99:
            print('Digite seu Login de Funcionário: ')
            this.loginADMM = input()
            print ('Digite sua senha: ')
            this.senhaADMM = input()
            operacao.consultaloginADM(this.loginADMM, this.senhaADMM)


