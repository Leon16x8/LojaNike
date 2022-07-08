import operacao
import this
from gtts import gTTS
from playsound import playsound
this.loginn = ""
this.senhaa = ""
this.opcao = -1

##som = ('speech.mp3')
##playsound(som)

class bcolors:
    WHITE = '\033[1;97m' #Branco
    BLACK = '\033[1;30m' #Preto
    GREEN = '\033[92m' #Verde
    YELLOW = '\033[93m' # Amarelo
    RED = '\033[91m' #Vermelho
    RESET = '\033[0m' #Resetar a Cor

def menu():
    print(f"{bcolors.BLACK}|------------------------|{bcolors.RESET}")
    print(f"{bcolors.WHITE}|          NIKE          |{bcolors.RESET}\n" +
          f"{bcolors.BLACK}|------------------------|{bcolors.RESET}\n" +
          f"{bcolors.WHITE}Escolha uma das opções abaixo: {bcolors.RESET}\n\n" +
          f"{bcolors.WHITE}1. Login\n{bcolors.RESET}"             +
          f"{bcolors.WHITE}2. Cadastro\n{bcolors.RESET}"          +
          f"{bcolors.RED}0. Sair\n{bcolors.RESET}")
    this.opcao = int(input(f"{bcolors.GREEN}Escolha uma opção: {bcolors.RESET}"))

def operar():
    while (this.opcao != 0):
        menu()
        if this.opcao == 0:
            print('\n')
            print(f"{bcolors.RED}FLW MENOR{bcolors.RESET}")
            ##son = ('speech1.mp3')
            ##playsound(son)

        elif this.opcao == 1:
            print(f"{bcolors.WHITE}Digite seu Login: ")
            this.loginn = input()
            print('Digite sua Senha: ')
            this.senhaa = input()
            operacao.login(this.loginn, this.senhaa)

        elif this.opcao == 2:
            print(f"{bcolors.WHITE}Informe seu CPF: ")
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


