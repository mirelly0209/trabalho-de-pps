import conexao

from random import choice
import string

connection = conexao.connection


class Socio:
    def __init__(self, nome, cpf, nivel, email, senha):
        self.nome = nome
        self.cpf = cpf
        self.nivel = nivel
        self.email = email
        self.senha = senha

    def criar_socio(self):
        with connection.cursor() as cursor:
            sql = "INSERT INTO `socios` (nome, cpf, nivel, email, senha) VALUES (%s, %s, %s, %s, %s)"
            cursor.execute(sql, (self.nome, self.cpf, self.nivel, self.email, self.senha))
            connection.commit()
            print('O socio foi inserido com sucesso')

    @staticmethod
    def listar_socio():
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM socios')
            resultado = cursor.fetchall()
            for linha in resultado:
                print(linha)
        return linha.__str__()

    @staticmethod
    def deletar_socio(id):
        print(id)
        with connection.cursor() as cursor:
            sql = f'DELETE FROM socios WHERE id = {id}'
            cursor.execute(sql)
            connection.commit()

    @staticmethod
    def atualizar_so(id, nome, cpf, nivel, email):
        with connection.cursor() as cursor:
            sql = f'UPDATE socios SET nome="{nome}", cpf="{cpf}", nivel="{nivel}", email="{email}" WHERE id="{id}"'
            cursor.execute(sql)
            connection.commit()

    @staticmethod
    def atualizar_senha(id, nome, cpf, nivel, email, senha):
        with connection.cursor() as cursor:
            sql = f'UPDATE socios SET nome="{nome}", cpf="{cpf}", nivel="{nivel}", email="{email}, senha="{senha}" WHERE id="{id}"'
            cursor.execute(sql)
            connection.commit()




