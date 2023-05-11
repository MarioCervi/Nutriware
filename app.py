from flask import Flask, render_template, jsonify, request
from alimentos import alimentos

app = Flask(__name__)

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/buscador/", methods=["GET", "POST"])
def buscador():
    if request.method == "POST":
        alimento = request.form["buscador"]
        for a in alimentos:
            if a["nombre"] == alimento:
                nutriscore = a["nutriscore"]
                alergenos = a["alergenos"]
                return nutriscore, alergenos
            
    return render_template("buscador.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)