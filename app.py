'''
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime.
As perguntas são:
    "Telefonou para a vítima?"
    "Esteve no local do crime?"
    "Mora perto da vítima?"
    "Devia para a vítima?"
    "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação
da pessoa no crime.

Se a pessoa responder positivamente a 2 questões ela deve ser classificada
como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".

'''

from flask import Flask, render_template, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string' 


@app.route("/", methods=['GET','POST'])
def index():
    positivos = 0
    if request.method == "POST":
        nome = request.form['nome']
        telefonou = request.form['telefonou']
        if telefonou == 'S':
            positivos += 1
        esteve = request.form['esteve']
        if esteve == 'S':
            positivos += 1
        mora = request.form['mora']
        if mora == 'S':
            positivos += 1
        devia = request.form['devia']
        if devia == 'S':
            positivos += 1
        trabalhou = request.form['trabalhou']
        if trabalhou == 'S':
            positivos += 1
        
        if positivos < 2:
            flash(f'{nome} é inocente!')
            return render_template("resultado.html", resultado = 'Inocente', nome=nome)
        elif positivos == 2:
            flash(f'{nome} é culpado!')
            return render_template("resultado.html", resultado = 'Suspeito', nome=nome)
        elif positivos < 5:
            flash(f'{nome} é cúmplice!')
            return render_template("resultado.html", resultado = 'Cúmplice', nome=nome)
        else:
            flash(f'{nome} é ASSASSINO!')
            return render_template("resultado.html", resultado = 'ASSASSINO!', nome=nome)

            
         
    return render_template("index.html")


app.run(host='0.0.0.0', debug=True)