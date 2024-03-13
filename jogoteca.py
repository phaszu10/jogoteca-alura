from flask import Flask, render_template, request

class Jogos():
    def __init__(self, nome, cat, console) -> None:
        self.nome = nome
        self.cat = cat
        self.console = console

titulo = 'Jogos'
jogo1 = Jogos('zelda','rpg', 'nintendo 64')
jogo2 = Jogos('Pokemon','rpg','gameboy')
lista_de_jogos = [jogo1, jogo2]


app = Flask(__name__)
@app.route("/inicio")
def ola():
    return render_template('listas.html',titulo = titulo, jogos = lista_de_jogos )

@app.route("/novo")
def novo():
    titulo = 'Novo'
    return render_template('novo.html',titulo = titulo)

@app.route("/criar")
def criar():
    nome = request.form['nome']
    cat = request.form['categoria']
    console = request.form['console']
    jogo = Jogos(nome,cat,console)
    lista_de_jogos.append(jogo)
    return render_template('listas.html',titulo = titulo, jogos = lista_de_jogos )

app.run()