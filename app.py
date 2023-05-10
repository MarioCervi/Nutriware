from flask import Flask, render_template, jsonify, request
from alimentos import alimentos2

app = Flask(__name__)

@app.route("/main")
def main():
    return render_template("index.html")

@app.route("/buscador/", methods=["GET", "POST"])
def buscador():
    if request.method == "POST":
        alimento = request.form["buscador"]
        for a in alimentos2:
            if a["nombre"] == alimento:
                nutriscore = a["nutriscore"]
                return nutriscore
    return render_template("buscador.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)



#prueba