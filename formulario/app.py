from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

#ruta para mostrar el formulario
@app.route("/")
def show_form():
    return render_template("form.html")

#ruta para procesar el formulario y mostrar el resultado
@app.route("/saludo", methods = ["POST"])
def greet_user():
    #obtener el nombre del formulario
    nombre_u = request.form.get("nombre")
    if not nombre_u:
        return redirect(url_for('show_form'))
    
    return render_template("result.html", nombre = nombre_u)

if __name__ == "__main__":
    app.run(debug = True, port = 8000)