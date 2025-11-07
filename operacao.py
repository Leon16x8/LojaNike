import conexaoSQL
import menucliente
import menuADM

db_connection = conexaoSQL.conectar()
con = None


def _ensure_connection():
    """Garante que `db_connection` e `con` (cursor) estejam disponíveis.

    Se a conexão inicial falhar, tenta conectar novamente. Retorna True
    se a conexão (e cursor) estiverem prontos, False caso contrário.
    """
    global db_connection, con
    if db_connection is None:
        db_connection = conexaoSQL.conectar()
    if db_connection is None:
        print(f"{bcolors.RED}Erro: não foi possível conectar ao banco de dados. Operação cancelada.{bcolors.RESET}")
        con = None
        return False

    try:
        # cria cursor se ainda não existir
        if con is None:
            con = db_connection.cursor()
        return True
    except Exception as e:
        print(f"{bcolors.RED}Erro ao obter cursor do DB: {e}{bcolors.RESET}")
        con = None
        return False

class bcolors:
    WHITE = '\033[1;97m' #Branco
    BLACK = '\033[1;30m' #Preto
    GREEN = '\033[92m' #Verde
    YELLOW = '\033[93m' # Amarelo
    RED = '\033[91m' #Vermelho
    RESET = '\033[0m' #Resetar a Cor


def cadastro(cpf, nome, login, senha, email):
    try:
        if not _ensure_connection():
            return None
        sql = "insert into cadastro(cpf, nome, login, senha, email) values('{}', '{}', '{}', '{}', '{}')".format(cpf, nome, login, senha, email)
        con.execute(sql)
        db_connection.commit()  # Inserção de dados no BD
        print("{} Linha Inserida !\n".format(con.rowcount))#rowcount = Contar quantas linhas foram afetadas

    except Exception as erro:
        return erro

def produtos(itens, preco):
    try:
        if not _ensure_connection():
            return None
        sql = "insert into produtos(itens, preco) values ('{}', '{}')".format(itens, preco)
        con.execute(sql)
        db_connection.commit() #Inserção de dados no BD
        print("{} Produto inserido com Sucesso!\n".format(con.rowcount))#rowcount = Contar quantas linhas foram afetadas

    except Exception as erro:
        return erro

def consultarprodutos():
    try:
        if not _ensure_connection():
            return None
        sql = 'select * from produtos'
        con.execute(sql)
        for(codigo, itens, preco) in con:
            print(f"{bcolors.WHITE}")
            print('Produto: {} {}'.format(codigo, itens))
            print('R${}\n'.format(preco))
            print(f"{bcolors.RESET}")
    except Exception as erro:
        return erro

def consultarLoginSenha(loginn, senhaa):
    try:
        if not _ensure_connection():
            return False
        sql = 'select login, senha from cadastro'
        con.execute(sql)
        for(login, senha) in con:
            if login == loginn and senha == senhaa:
                return True
        return False
    except Exception as erro:
        print(erro)

def consultarLoginSenhaADM(loginADMM, senhaADMM):
    try:
        if not _ensure_connection():
            return False
        sql = 'select * from ADM'
        con.execute(sql)
        for(cpf, loginADM, senhaADM) in con:
            if loginADM == loginADMM and senhaADM == senhaADMM:
                return True
        return False
    except Exception as erro:
        print(erro)

def login(loginn, senhaa):
    try:
        if consultarLoginSenha(loginn, senhaa) == True:
            print('Logado com Sucesso !')
            print('\n')
            menucliente.opera()
        else:
            print('Login e Senha incorretos!')
            print('\n')
    except Exception as erro:
        print(erro)

def consultaloginADM(loginADMM, senhaADMM):
    try:
        if consultarLoginSenhaADM(loginADMM, senhaADMM) == True:
            print('Logado com Sucesso !')
            menuADM.op()
        else:
            print('Login e Senha incorretos!')
            print('\n')
    except Exception as erro:
        print(erro)

def excluirPessoa(cpf):
    try:
        if not _ensure_connection():
            return None
        sql = "delete from cadastro where cpf = '{}'".format(cpf)
        con.execute(sql)
        db_connection.commit()
        print('{} Cliente excluido com sucesso !\n'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def excluirProduto(codigo):
    try:
        if not _ensure_connection():
            return None
        sql = "delete from produtos where codigo = '{}'".format(codigo)
        con.execute(sql)
        db_connection.commit()
        print('{} Codigo Nº{} Excluido com Sucesso !\n'.format(con.rowcount, codigo))
    except Exception as erro:
        print(erro)

def atualizarPreco(campo, novoDado, codigo):
    try:
        if not _ensure_connection():
            return None
        sql = "update produtos set {} = '{}' where codigo = '{}'".format(campo, novoDado, codigo)
        con.execute(sql)
        db_connection.commit()
        print('Preço atualizado com sucesso !\n')
    except Exception as erro:
        print(erro)

def atualizarProduto(campo, novoDado, codigo):
    try:
        if not _ensure_connection():
            return None
        sql = "update produtos set {} = '{}' where codigo = '{}'".format(campo, novoDado, codigo)
        con.execute(sql)
        db_connection.commit()
        print('Produto atualizado com sucesso !\n')
    except Exception as erro:
        print(erro)


