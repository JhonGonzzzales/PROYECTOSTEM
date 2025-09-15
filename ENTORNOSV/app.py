#IMPORTACIONES
from flask import Flask

#CREAR LA APLICACIÓN
app = Flask(__name__)

#CREAR RUTAS
@app.route("/")
def index():
    return "Hola mundo desde Flask!"

#
@app.route("/contacto")
def contacto():
    return "<h1>Pagina de contactos</h1>"


#EJECUTAR LA APLICACIÓN
if __name__ == "__main__":
    app.run(debug=True)
