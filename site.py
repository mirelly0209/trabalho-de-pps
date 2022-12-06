from flask import Flask, render_template, request, redirect, url_for
from main import Funcionario
from main2 import Socio
import conexao
from random import choice
import string

secundario = conexao.secundario

connection = conexao.connection

gabriel = Flask(__name__)


# PÁGINA PRINCIPAL

############################################################################################

@gabriel.route("/", methods=["GET", "POST"])
def homepage():
    return render_template('homepage.html')


##############################################################################################

#LOGIN PARA LISTA

##############################################################################################

@gabriel.route("/loginlista.html", methods=["GET", "POST"])
def loginlista():
    mycursor = secundario.cursor()

    mycursor.execute("SELECT nome, email, senha  FROM socios")

    myresult = mycursor.fetchall()
    print(myresult)
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        senha = request.form.get('senha')
        print(nome, email, senha)
        for x in myresult:
            print(x)
            if nome and email and senha in x:
                return redirect(url_for('lista'))
            else:
                return redirect(url_for('erro_loginlista'))
    return render_template('loginlista.html')

##############################################################################################

# LOGIN PARA CADASTRO DE SÓCIO

##############################################################################################

@gabriel.route("/loginsocio.html", methods=["GET", "POST"])
def loginsocio():
    mycursor = secundario.cursor()

    mycursor.execute("SELECT senha FROM senhas")

    myresult = mycursor.fetchall()
    if request.method == 'POST':
        senha = request.form.get('senha')
        print(senha)
        for x in myresult:
            print(x)
            if senha in x:
                return redirect(url_for('socio'))
            else:
                return redirect(url_for('erro_loginsocio'))
    return render_template('loginsocio.html')


##############################################################################################

##############################################################################################

# ERRO LOGINLISTA

##############################################################################################

@gabriel.route("/erro_loginlista.html", methods=["GET", "POST"])
def erro_loginlista():
    return render_template('erro_loginlista.html')

##############################################################################################

# ERRO LOGINSOCIO

##############################################################################################

@gabriel.route("/erro_loginsocio.html", methods=["GET", "POST"])
def erro_loginsocio():
    return render_template('erro_loginsocio.html')
#############################################################################################

# LISTA DOS FUNCIONÁRIOS E SÓCIOS

##############################################################################################

@gabriel.route("/lista", methods=["GET", "POST"])
def lista():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM funcionario')
        funcionarios = cursor.fetchall()
        cursor.execute('SELECT * FROM socios')
        socios = cursor.fetchall()
    return render_template('lista.html', funcionarios=funcionarios, socios=socios)


##############################################################################################


# CADASTRO DOS FUNCIONÁRIOS E SÓCIOS

##############################################################################################

@gabriel.route("/funcionario.html", methods=["GET", "POST"])
def funcionario():
    if request.method == 'POST':
        nome = request.form.get('nome')
        email = request.form.get('email')
        numero = request.form.get('numero')
        cpf = request.form.get('cpf')
        cidade = request.form.get('cidade')
        funcionario = Funcionario(nome, email, numero, cpf, cidade)
        funcionario.criar_fun()
        return redirect(url_for('homepage'))
    return render_template('funcionario.html')


##############################################################################################

@gabriel.route("/socio.html", methods=["GET", "POST"])
def socio():
    if request.method == 'POST':
        tamanho_da_senha = 8
        caracteres = string.ascii_letters + string.digits
        senha = ''
        for i in range(tamanho_da_senha):
            senha += choice(caracteres)
        print(senha)
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        nivel = request.form.get('nivel')
        email = request.form.get('email')
        socio = Socio(nome, cpf, nivel, email, senha)
        socio.criar_socio()
        return redirect(url_for('identificar'))
    return render_template('socio.html')

##############################################################################################

#IDENTICAR

##############################################################################################
@gabriel.route("/identificar.html", methods=["GET", "POST"])
def identificar():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM socios')
        socios = cursor.fetchall()
    return render_template('identificar.html', socios=socios)


##############################################################################################

#SENHA

##############################################################################################

@gabriel.route("/<int:id>/senha.html", methods=["GET", "POST"])
def senha(id):
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM socios WHERE id = {id}')
        socio = cursor.fetchone()

        if request.method == 'POST':
            nome = request.form.get('nome')
            cpf = request.form.get('cpf')
            nivel = request.form.get('nivel')
            email = request.form.get('email')
            senha = request.form.get('senha')
            Socio.atualizar_senha(id, nome, cpf, nivel, email, senha)
            return redirect(url_for('lista'))
    return render_template('senha.html', socio=socio)
##############################################################################################

# ATUALIZAR FUNCIONÁRIO E SÓCIO

##############################################################################################

@gabriel.route('/<int:id>/atualizar_funcionario', methods=["GET", "POST"])
def atualizar_funcionario(id):
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM funcionario WHERE id = {id}')
        funcionario = cursor.fetchone()

        if request.method == 'POST':
            nome = request.form.get('nome')
            email = request.form.get('email')
            numero = request.form.get('numero')
            cpf = request.form.get('cpf')
            cidade = request.form.get('cidade')
            Funcionario.atualizar_fun(id, nome, email, numero, cpf, cidade)
            return redirect(url_for('lista'))
    return render_template('atualizar_funcionario.html', funcionario=funcionario)


##############################################################################################

@gabriel.route('/<int:id>/atualizar_socio', methods=["GET", "POST"])
def atualizar_socio(id):
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM socios WHERE id = {id}')
        socio = cursor.fetchone()

        if request.method == 'POST':
            nome = request.form.get('nome')
            cpf = request.form.get('cpf')
            nivel = request.form.get('nivel')
            email = request.form.get('email')
            Socio.atualizar_so(id, nome, cpf, nivel, email )
            return redirect(url_for('lista'))
    return render_template('atualizar_socio.html', socio=socio)



##############################################################################################

# REMOVER FUNCIONÁRIO E SÓCIO

##############################################################################################

@gabriel.route('/<int:id>/remover_funcionario')
def remover_funcionario(id):
    print(id)
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM funcionario WHERE id = {id}')
        funcionario = cursor.fetchone()

        print(funcionario)
        Funcionario.deletar_fun(id)
        return redirect(url_for('lista'))

    return redirect(url_for('remover_funcionario.html'))


##############################################################################################

@gabriel.route('/<int:id>/remover_socio')
def remover_socio(id):
    print(id)
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM socio WHERE id = {id}')
        socio = cursor.fetchone()

        print(socio)
        Socio.deletar_socio(id)
        return redirect(url_for('lista'))

    return redirect(url_for('remover_socio.html'))


##############################################################################################


if __name__ == "__main__":
    gabriel.run(debug=True)
