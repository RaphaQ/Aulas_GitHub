from database_manager import criar_conexao

class Produto:
    def __init__(self, id, nome, descricao, preco, quantidade_disponivel):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.quantidade_disponivel = quantidade_disponivel

    @staticmethod
    def cadastrar(nome, descricao, preco, quantidade):
        conexao = criar_conexao()
        if conexao:
            cursor = conexao.cursor()
            query = "INSERT INTO produtos (nome, descricao, preco, quantidade_disponivel) VALUES (%s %s %s %s)"
            valores = (nome, descricao, preco, quantidade)
            cursor.execute(query, valores)
            conexao.commit()
            cursor.close()
            conexao.close()
            print("Produto cadastrado com sucesso")
    @staticmethod
    def listar_todos():