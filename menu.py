import operacao
import this
from gtts import gTTS
from pygame import mixer
from playsound import playsound
this.loginn = ""
this.senhaa = ""
this.opcao = -1

som = ('speech.mp3')
playsound(som)

class bcolors:
    GREEN = '\033[92m' #Verde
    YELLOW = '\033[93m' # Amarelo
    RED = '\033[91m' #Vermelho
    RESET = '\033[0m' #Resetar a Cor

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
            print('\n')
            print(f"{bcolors.RED}FLW MENOR{bcolors.RESET}")
            son = ('speech1.mp3')
            playsound(son)

        elif this.opcao == 1:
            print('Digite seu Login: ')
            this.loginn = input()
            print('Digite sua Senha: ')
            this.senhaa = input()
            operacao.login(this.loginn, this.senhaa)

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


