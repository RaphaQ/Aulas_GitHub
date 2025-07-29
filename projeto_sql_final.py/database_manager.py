import mysql.connector
from mysql.connector import Error

def criar_conexao ():
    try:
        conexao = mysql.connector.connect(
            host = "localhost:3306",
            database = "gerenciador_estoque",
            user = "root",
            password = "Infinity"
        )
        if conexao.is_connected():
            return conexao
    except Error as e:
        print(f"Erro ao conectar ao MySQL: {e}")
        return None