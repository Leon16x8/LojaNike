import this
import operacao
import time

# Tentar importar cv2 (OpenCV). Se não estiver instalado, deixamos um fallback
try:
    import cv2
    _HAS_CV2 = True
except Exception:
    cv2 = None
    _HAS_CV2 = False
import menu

this.opcao = -1
this.opcao1 = -1
this.opcao2 = -1

class bcolors:
    BLUE = '\033[1;94m' #Azul Claro
    WHITE = '\033[1;97m' #Branco
    BLACK = '\033[1;30m' #Preto
    GREEN = '\033[92m' #Verde
    YELLOW = '\033[93m' # Amarelo
    RED = '\033[91m' #Vermelho
    RESET = '\033[0m' #Resetar a Cor


def menuCliente():
    print(f"{bcolors.YELLOW}|------------------------------------------------------------------------|\n{bcolors.RESET}" +
          f"{bcolors.YELLOW}|--------------------------------PRODUTOS--------------------------------|\n{bcolors.RESET}" +
          f"{bcolors.YELLOW}|------------------------------------------------------------------------|\n{bcolors.RESET}")
    print(operacao.consultarprodutos())
    print(f"{bcolors.RED}0. Sair\n{bcolors.RESET}")

    this.opcao = int(input('Digite o codigo do produto que deseja: '))
    print('\n')


def show_payment_qr():
    """Mostra o QR code usando OpenCV se disponível; caso contrário mostra uma mensagem.

    Mantemos a função resiliente a erros (arquivo ausente ou falha no OpenCV).
    """
    if not _HAS_CV2:
        print(f"{bcolors.YELLOW}Biblioteca 'cv2' não está instalada. Instale 'opencv-python' para visualizar o QR.{bcolors.RESET}")
        return

    try:
        img = cv2.imread("qrcodepagamento.png")
        if img is None:
            print(f"{bcolors.YELLOW}Arquivo 'qrcodepagamento.png' não encontrado ou inválido.{bcolors.RESET}")
            return
        img = cv2.resize(img, (270, 270))
        cv2.imshow("Pagamento", img)
        cv2.waitKey(0)
    except Exception as e:
        print(f"{bcolors.RED}Erro ao mostrar QR: {e}{bcolors.RESET}")

def opera():
    while (this.opcao != 0):
        menuCliente()
        if this.opcao == 0:
            print(f"{bcolors.GREEN}Obrigado, volte sempre!{bcolors.RESET}")
            exit()

        elif this.opcao == 1:
            print(f"{bcolors.BLUE}Qual forma de pagamento deseja?\n {bcolors.RESET}")
            print(f"{bcolors.WHITE}1. PIX\n"     +
                  '2. Cartão\n'  +
                  f'0. Voltar\n{bcolors.RESET}')
            while (this.opcao2 != 0):
                this.opcao2 = int(input(f"{bcolors.WHITE}Digite o numero da opção de pagamento: {bcolors.RESET}"))
                if this.opcao2 == 0:
                    opera()

                elif this.opcao2 == 1: #PIX
                    time.sleep(1)
                    show_payment_qr()
                    time.sleep(1)
                    print(f"{bcolors.YELLOW}Iremos verificar o pagamento e te avisaremos via e-mail{bcolors.RESET}")
                    print(f"{bcolors.GREEN}Obrigado Volte Sempre !\n{bcolors.RESET}")
                    time.sleep(5)
                    opera()

                elif this.opcao2 == 2: #Cartão
                    print('Em Construção\n')

        elif this.opcao == 2:
            print(f"{bcolors.BLUE}Qual forma de pagamento deseja?\n {bcolors.RESET}")
            print(f"{bcolors.WHITE}1. PIX\n" +
                  '2. Cartão\n' +
                  f'0. Voltar\n{bcolors.RESET}')
            while (this.opcao2 != 0):
                this.opcao2 = int(input(f"{bcolors.WHITE}Digite o numero da opção de pagamento: {bcolors.RESET}"))
                if this.opcao2 == 0:
                    opera()
                elif this.opcao2 == 1:  # PIX
                    time.sleep(1)
                    show_payment_qr()
                    time.sleep(1)
                    print(f"{bcolors.YELLOW}Iremos verificar o pagamento e te avisaremos via e-mail{bcolors.RESET}")
                    print(f"{bcolors.GREEN}Obrigado Volte Sempre !\n{bcolors.RESET}")
                    time.sleep(5)
                    opera()

                elif this.opcao2 == 2:  # Cartão
                    print('Em Construção\n')

        elif this.opcao == 3:
            print(f"{bcolors.BLUE}Qual forma de pagamento deseja?\n {bcolors.RESET}")
            print(f"{bcolors.WHITE}1. PIX\n" +
                  '2. Cartão\n' +
                  f'0. Voltar\n{bcolors.RESET}')
            while (this.opcao2 != 0):
                this.opcao2 = int(input(f"{bcolors.WHITE}Digite o numero da opção de pagamento: {bcolors.RESET}"))
                if this.opcao2 == 0:
                    opera()
                elif this.opcao2 == 1:  # PIX
                    time.sleep(1)
                    show_payment_qr()
                    time.sleep(1)
                    print(f"{bcolors.YELLOW}Iremos verificar o pagamento e te avisaremos via e-mail{bcolors.RESET}")
                    print(f"{bcolors.GREEN}Obrigado Volte Sempre !\n{bcolors.RESET}")
                    time.sleep(5)
                    opera()

                elif this.opcao2 == 2:  # Cartão
                    print('Em Construção\n')











