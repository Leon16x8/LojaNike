import mysql.connector
import conexaoSQL
import menucliente
import menuADM

db_connection = conexaoSQL.conectar()
con = db_connection.cursor()

def cadastro(cpf, nome, login, senha, email):
    try:
        sql = "insert into cadastro(cpf, nome, login, senha, email) values('{}', '{}', '{}', '{}', '{}')".format(cpf, nome, login, senha, email)
        con.execute(sql)
        db_connection.commit()  # Inserção de dados no BD
        print("{} Linha Inserida !\n".format(con.rowcount))#rowcount = Contar quantas linhas foram afetadas

    except Exception as erro:
        return erro

def produtos(itens, preco):
    try:
        sql = "insert into produtos(itens, preco) values ('{}', '{}')".format(itens, preco)
        con.execute(sql)
        db_connection.commit() #Inserção de dados no BD
        print("{} Produto inserido com Sucesso!\n".format(con.rowcount))#rowcount = Contar quantas linhas foram afetadas

    except Exception as erro:
        return erro

def consultarprodutos():
    try:
        sql = 'select * from produtos'
        con.execute(sql)

        msg = ""
        for(codigo, itens, preco) in con:
            msg += "{} {} {} ".format(codigo,itens,preco)
        return msg
    except Exception as erro:
        return erro

def consultarLoginSenha(loginn, senhaa):
    try:
        sql = 'select * from cadastro'
        con.execute(sql)

        for(cpf, nome, login, senha, email) in con:
            if login == loginn and senha == senhaa:
                return True
        return False
    except Exception as erro:
        print(erro)


def login(loginn, senhaa):
    try:
        if consultarLoginSenha(loginn, senhaa) == True:
            print('Logado com Sucesso !')
            menucliente.opera()
        else:
            print('Login e Senha incorretos!')
            print('\n')
    except Exception as erro:
        print(erro)

def consultaloginADM(loginADMM, senhaADMM):
    try:
        sql = 'select loginADM, senhaADM from ADM'
        con.execute(sql)
        for(loginADM, senhaADM) in con:
            if loginADM == loginADMM and senhaADM == senhaADMM:
                print('Logado com Sucesso')
                menuADM.op()
            else:
                print('Login e Senha incorretos !')
                print('\n')
    except Exception as erro:
        print(erro)

def excluirPessoa(cpf):
    try:
        sql = "delete from cadastro where cpf = '{}'".format(cpf)
        con.execute(sql)
        db_connection.commit()
        print('{} Cliente excluido com sucesso !\n'.format(con.rowcount))
    except Exception as erro:
        print(erro)

def excluirProduto(codigo):
    try:
        sql = "delete from produtos where codigo = '{}'".format(codigo)
        con.execute(sql)
        db_connection.commit()
        print('{} Codigo Nº{} Excluido com Sucesso !\n'.format(con.rowcount, codigo))
    except Exception as erro:
        print(erro)

def atualizarPreco(campo, novoDado, codigo):
    try:
        sql = "update produtos set {} = '{}' where codigo = '{}'".format(campo, novoDado, codigo)
        con.execute(sql)
        db_connection.commit()
        print('Preço atualizado com sucesso !\n')
    except Exception as erro:
        print(erro)

