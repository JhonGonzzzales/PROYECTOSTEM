from flask import Flask

app  = Flask(__name__)

@app.route("/")
def inicio():
    return "<h1>Pagina de Inicio</h1>"

@app.route("/acerca-de")
def acerca_de():
    return "<h1>Información sobre nosotros</h1>"

@app.route("/contacto")
def contacto():
    return "<h1>Página de contacto</h1>"

@app.route("/info")
@app.route("/informacion")
@app.route("/about")
def informacion():
    return "<h1>Página de Información</h1>"

if __name__ == "__main__":
    app.run(debug = True)