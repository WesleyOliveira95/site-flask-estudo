from flask import Flask, render_template

app = Flask(__name__)

# criar a 1º pagina do site
# route -> hashtagdominio.com/contatos
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_usuario>")
def usuarios(nome_usuario):
    return render_template("usuarios.html", nome_usuario=nome_usuario)

@app.route("/gatinhos")
def gatinhos():
    return render_template("gatinhos.html")

# colocar o site no ar
if __name__== "__main__":
    app.run(debug=True)

    # servidor do heroku

