import pymysql.cursors

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='gabriel',
    cursorclass=pymysql.cursors.DictCursor
)

secundario = pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='gabriel',

)


class Nada():
    @staticmethod
    def verificar():
        mycursor = secundario.cursor()

        mycursor.execute("SELECT senha FROM senha")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)
            if senha in x:
                print('sim')

