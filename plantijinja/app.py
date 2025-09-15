from flask import Flask, render_template

app = Flask("__name__")

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/quienes")
def quienes():
    return render_template('quienes.html')

@app.route("/servicios")
def servicios():
    lista = ["Entrega a domicilio",
             "Reserva vía online",
             "Pago contra entrega"]
    return render_template('servicios.html', lista=lista)

@app.route("/contacto")
def contacto():
    return render_template('contacto.html')

if __name__ == "__main__":
    app.run(debug=True, port = 8000)