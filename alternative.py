import pymysql.cursors



connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='gabriel',

)

class Nada:
    def __init__(self, senha):
        self. senha = senha
