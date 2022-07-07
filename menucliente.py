import this
import operacao
import time
import cv2
import menu

this.opcao = -1
this.opcao1 = -1
this.opcao2 = -1

class bcolors:
    GREEN = '\033[92m' #Verde
    YELLOW = '\033[93m' # Amarelo
    RED = '\033[91m' #Vermelho
    RESET = '\033[0m' #Resetar a Cor

def menuCliente():
    print(operacao.consultarprodutos())
    print('0. Sair\n')

    this.opcao = int(input('Digite o codigo do produto que deseja: '))
    print('\n')

def opera():
    while (this.opcao != 0):
        menuCliente()
        if this.opcao == 0:
            print(f"{bcolors.GREEN}Obrigado, volte sempre!{bcolors.RESET}")
            exit()

        elif this.opcao == 1:
            print('Qual forma de pagamento deseja?\n ')
            print('1. PIX\n'     +
                  '2. Cartão\n'  +
                  '0. Voltar\n')
            while (this.opcao1 != 0):
                this.opcao1 = int(input('Digite o numero da opção de pagamento: '))
                if this.opcao1 == 0:
                    opera()
                elif this.opcao1 == 1: #PIX
                    time.sleep(1)
                    img = cv2.imread("qrcodepagamento.png")
                    img = cv2.resize(img, (270, 270))
                    cv2.imshow("Pagamento", img)
                    cv2.waitKey(0)
                    time.sleep(1)
                    print(f"{bcolors.YELLOW}Iremos verificar o pagamento e te avisaremos via e-mail{bcolors.RESET}")
                    print(f"{bcolors.GREEN}Obrigado Volte Sempre !\n{bcolors.RESET}")
                    time.sleep(5)
                    opera()

                elif this.opcao1 == 2: #Cartão
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
                elif this.opcao1 == 1: #PIX
                    time.sleep(1)
                    img = cv2.imread("qrcodepagamento.png")
                    img = cv2.resize(img, (270, 270))
                    cv2.imshow("Pagamento", img)
                    cv2.waitKey(0)
                    time.sleep(1)
                    print(f"{bcolors.YELLOW}Iremos verificar o pagamento e te avisaremos via e-mail{bcolors.RESET}")
                    print(f"{bcolors.GREEN}Obrigado Volte Sempre !\n{bcolors.RESET}")
                    time.sleep(5)
                    opera()
                elif this.opcao1 == 2: #Cartão
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
                elif this.opcao1 == 1: #PIX
                    time.sleep(1)
                    img = cv2.imread("qrcodepagamento.png")
                    img = cv2.resize(img, (270, 270))
                    cv2.imshow("Pagamento", img)
                    cv2.waitKey(0)
                    time.sleep(1)
                    print(f"{bcolors.YELLOW}Iremos verificar o pagamento e te avisaremos via e-mail{bcolors.RESET}")
                    print(f"{bcolors.GREEN}Obrigado Volte Sempre !\n{bcolors.RESET}")
                    time.sleep(5)
                    opera()
                elif this.opcao1 == 2: #Cartão
                    print('Em Construção\n')











