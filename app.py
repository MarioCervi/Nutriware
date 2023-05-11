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
<<<<<<< Updated upstream
        for a in alimentos2:
            if a["nombre"] == alimento:
                nutriscore = a["nutriscore"]
                return nutriscore
=======
        dict = similitudes.mostrar_similitudes(alimento) # aqui pasarle el argumento "alimento"
        #for a in alimentos:
            #if a["nombre"] == alimento:
                #nutriscore = a["nutriscore"]
                #return nutriscore
        return dict
    #return jsonify()
>>>>>>> Stashed changes
    return render_template("buscador.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)



#prueba