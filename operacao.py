import mysql.connector
import conexaoSQL

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


