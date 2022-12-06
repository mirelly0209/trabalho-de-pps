import pymysql.cursors



connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='trabalho',
)


class Aluno:
    def __init__(self, nome, idade, matricula, genero):
        self.nome = nome
        self.idade = idade
        self.matricula = matricula
        self.genero = genero

    def criar_aluno(self):
        with connection.cursor() as cursor:
            sql = "INSERT INTO aluno (nome, idade, matricula, genero) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (self.nome, self.idade, self.matricula, self.genero))
            connection.commit()
            print('O aluno foi inserido com sucesso')


    def listar_aluno():
        print(connection.cursor())
        with connection.cursor() as cursor:
            cursor.execute('SELECT * FROM aluno')
            resultado = cursor.fetchall()
            for linha in resultado:
                print(linha)


    def atualizar_aluno(id, nome, idade):
        with connection.cursor() as cursor:
            print(id, nome)
            sql = 'UPDATE aluno SET nome=%s, idade=%s WHERE id=%s'
            cursor.execute(sql, (nome, idade, id))
            connection.commit()


    def deletar_aluno(id):
        with connection.cursor() as cursor:
            sql = 'DELETE FROM aluno WHERE id = %s'
            cursor.execute(sql, (id))
            connection.commit()


    def login():
        mycursor = connection.cursor()

        mycursor.execute("SELECT nome FROM aluno")

        myresult = mycursor.fetchmany(10000)

        for x in myresult:
            print(x)
        print("Teste")
        y = input()
        if y in x:
            print("Deu certo")
        else:
            print("Escreve Gabriel")

aluno = Aluno
print("nome")
a = input()
print("idade")
b = input()
print("matricula")
c = input()
print("genero")
d = input()
aluno = Aluno
#aluno.criar_aluno(a, b, c, d)
Aluno.login()