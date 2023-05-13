# import os
# os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

from flask import Flask, render_template, jsonify, request, url_for, redirect
# from flask_dance.contrib.google import make_google_blueprint, google
from alimentos import alimentos
import similitudes

app = Flask(__name__)

# Configuración para inicio de sesión con google:
# app.secret_key = "nutriware-secret-key"
# blueprint = make_google_blueprint(
#     client_id="534885315451-nlatqmtcrsvboq3jjjntgik1u71364g9.apps.googleusercontent.com",
#     client_secret="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",
#     scope=["openid", "https://www.googleapis.com/auth/userinfo.email", "https://www.googleapis.com/auth/userinfo.profile"]
# )
# app.register_blueprint(blueprint, url_prefix="/login")

# @app.route("/")
# def index():
#     if not google.authorized:
#         return render_template("index.html")
#     else:
#         resp = google.get("/oauth2/v2/userinfo")
#         if resp.ok =="true":
#             return "bien"
#     return render_template("buscador.html")

@app.route("/buscador/", methods=["GET", "POST"])
def buscador():
    if request.method == "POST":
        alimento = request.form["buscador"]
        dict = similitudes.mostrar_similitudes(alimento) 
        for a in alimentos:
            if a["nombre"] == alimento:
                nutriscore = a["nutriscore"]
                alergenos = a["alergenos"]
                return render_template("resultados.html", nutriscore=nutriscore, alergenos=alergenos, a=alimento, dict=dict)
      
        
        return render_template("relacionados.html", dict2=dict)
    return render_template("buscador.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)