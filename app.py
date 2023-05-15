import os
import re
import funciones
from flask import Flask, render_template, request, url_for, redirect, session
from authlib.integrations.flask_client import OAuth

app = Flask(__name__)
app.secret_key = os.urandom(12)
oauth = OAuth(app)

@app.route('/')
def index():
    # Si el usuario ya ha iniciado sesion, se le redirige al buscador
    if 'name' in session:
        return redirect('/buscador/')
    return render_template('index.html')

@app.route('/google/')
def google():
    GOOGLE_CLIENT_ID = "534885315451-nlatqmtcrsvboq3jjjntgik1u71364g9.apps.googleusercontent.com"
    GOOGLE_CLIENT_SECRET = "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"

    CONF_URL = 'https://accounts.google.com/.well-known/openid-configuration'
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url=CONF_URL,
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    # Redirect to google_auth function
    redirect_uri = url_for('google_auth', _external=True)
    print(redirect_uri)
    return oauth.google.authorize_redirect(redirect_uri)

@app.route('/google/auth')
def google_auth():
    #recuperar token y toda la sesión
    token = oauth.google.authorize_access_token()
    user_info = token
    user_email = token['userinfo']['email']
    user_name = token['userinfo']['name']
    #guardar en sesion
    session['email'] = user_email
    session['name'] = user_name
    session['info'] = user_info
    return redirect('/buscador/')


@app.route("/buscador/", methods=["GET", "POST"])
def buscador():
    #recupero el nombre de la sesión
    if 'name' not in session:
        # si no tiene el nombre signigica que no ha iniciado sesión
        # se le redirige a el login
        return redirect('/')
    nombre = session['name']
    
    # atiende los métodos
    if request.method == "POST":
        alimento = request.form["buscador"]
        
        
        if alimento.isdigit():
            error_message = "Error, no puedes introducir numeros"
            return render_template("buscador.html", nombre=nombre, error_message_1=error_message)
        elif re.search(r"[^a-zA-Z0-9\s]", alimento):
            error_message = "Error, no puedes introducir simbolos especiales"
            return render_template("buscador.html", nombre=nombre, error_message_2=error_message)

        #  Busca los alimentos que sintacticamente mas se parezcan al que se ha buscado
        else :
            alimento = alimento.lower()
        dict = funciones.mostrar_similitudes(alimento) 

        # Busca tanto el nutriscore como los alergenos del producto buscado
        answer = funciones.resultado_busqueda(alimento, dict)
        
        return answer, 200
    return render_template("buscador.html", nombre=nombre)

@app.route("/cerrar-sesion/", methods=["GET"])
def cerrar_sesion():
    session.pop('email', None)
    session.pop('name', None)
    session.pop('info', None)
    return redirect('/')



if __name__ == "__main__":
    app.run(debug=True, port=5000)