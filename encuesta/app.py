from flask import Flask, render_template, request, redirect, url_for

resultados_encuesta = {
    "lenguaje_favorito": {},
    "experiencia": {}
}

app = Flask(__name__)

@app.route("/encuesta")
def mostrar_encuesta():
    return render_template("encuesta.html")

@app.route("/procesar-encuesta", methods=["POST"])
def procesar_encuesta():
    lenguaje = request.form.get("lenguaje")
    experiencia = request.form.get("experiencia")

    if not lenguaje or not experiencia:
        return redirect(url_for('mostrar_encuesta'))

    resultados_encuesta["lenguaje_favorito"][lenguaje] = resultados_encuesta["lenguaje_favorito"].get(lenguaje, 0) + 1
    resultados_encuesta["experiencia"][experiencia] = resultados_encuesta["experiencia"].get(experiencia, 0) + 1

    return redirect(url_for('mostrar_resultados'))

@app.route("/resultados")
def mostrar_resultados():
    return render_template("resultados.html", resultados=resultados_encuesta)

if __name__ == "__main__":
    app.run(debug=True, port=8000)