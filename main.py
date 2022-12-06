import conexao

connection = conexao.connection


class Funcionario:
    def __init__(self, nome, email, numero, cpf, cidade):
        self.nome = nome
        self.email = email
        self.numero = numero
        self.cpf = cpf
        self.cidade = cidade

    def criar_fun(self):
        with connection.cursor() as cursor:
            sql = "INSERT INTO `funcionario` (nome, email, numero, cpf, cidade) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (self.nome, self.email, self.numero, self.cpf, self.cidade))
            connection.commit()
            print('O aluno foi inserido com sucesso')

    @staticmethod
    def listar_fun():
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM funcionario')
            resultado = cursor.fetchall()
            for linha in resultado:
                print(linha)
        return linha.__str__()

    @staticmethod
    def deletar_fun(id):
        print(id)
        with connection.cursor() as cursor:
            sql = f'DELETE FROM funcionario WHERE id = {id}'
            cursor.execute(sql)
            connection.commit()

    @staticmethod
    def atualizar_fun(id, nome, email, numero, cpf, cidade):
        with connection.cursor() as cursor:
            sql = f'UPDATE funcionario SET nome="{nome}", email="{email}", numero="{numero}", cpf="{cpf}", cidade="{cidade}"  WHERE id="{id}"'
            cursor.execute(sql)
            connection.commit()

