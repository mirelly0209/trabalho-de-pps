import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='gabriel',

)

class Senha:
    def __init__(self, senha):
        self.senha = senha

    def criar_senha(self):
        with connection.cursor() as cursor:
            sql = "INSERT INTO senhas (senha) VALUES (%s)"
            cursor.execute(sql, (self.senha))
            connection.commit()
            print('O perfil foi inserido com sucesso')


a = "B4nz3fkd"
senha = Senha(a)
#senha.criar_senha()