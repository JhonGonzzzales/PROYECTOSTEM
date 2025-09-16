from flask import Flask, render_template

app = Flask (__name__)

@app.route("/saludo/<nombre>")
def index(nombre):
    return render_template(f"index.html", nombre=nombre)
    
@app.route("/usuarios")
def list_users():
    users = ["Bernardo", "Tiburcio", "Anacleto"]
    return render_template(f"users.html", users=users)

@app.route("/status")
def status():
    logueado = True
    return render_template(f"status.html", logueado=logueado)

@app.route("/home")
def home():
    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True, port=8000)