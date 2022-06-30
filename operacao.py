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
        print("{} Linha Inserida!".format(con.rowcount))#rowcount = Contar quantas linhas foram afetadas

    except Exception as erro:
        return erro

def produtos(itens, preco):
    try:
        sql = "insert into produtos(itens, preco) values ('{}', '{}')".format(itens, preco)
        con.execute(sql)
        db_connection.commit() #Inserção de dados no BD
        print("{} Linha Inserida!".format(con.rowcount))#rowcount = Contar quantas linhas foram afetadas

    except Exception as erro:
        return erro

def consultarprodutos():
    try:
        sql= 'select codigo, itens, preco from produtos'
        con.execute(sql)
        for(codigo, itens, preco) in con:
            print('Produto {}: {}\n R${}'.format(codigo, itens, preco))
    except Exception as erro:
        print(erro)

def consultalogin(loginn, senhaa):
    try:
        sql = 'select login, senha from cadastro'
        con.execute(sql)
        for(login, senha) in con:
            if loginn == login and senhaa == senha:
                print('Logado com Sucesso')
                menucliente.opera()
            else:
                print('Login e Senha incorretos !')
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