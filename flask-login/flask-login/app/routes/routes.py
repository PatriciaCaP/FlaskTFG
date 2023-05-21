from flask import Flask, render_template, request, redirect, url_for, session, Blueprint, flash # pip install Flask
from app import database as db

from app.data.infoUsuarios import Usuarios

app = Blueprint("routes", __name__)

@app.route('/', methods=["GET","POST"])
def home():
    return render_template("login.html")

@app.route("/logout")
def logout():
	session["nombre"] = None
	return redirect("/contenido")

@app.route("/contenido")
def index():
  # check if the users exist or not
    if not session.get("nombre"):
        # if not there in the session then redirect to the login page
        return redirect("/")
    return render_template('contenido.html')


@app.route("/registrarse", methods=["GET","POST"])
def registrarse():
    nombre = request.form['nombre'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL NOMBRE QUE INDIQUEMOS
    email = request.form['email'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL NOMBRE QUE INDIQUEMOS
    password = request.form['password'] # PARA PODER OBTENER EL CONTENIDO DEL INPUT CON EL NOMBRE QUE INDIQUEMOS
    infoUsuarios : Usuarios = Usuarios(db)
    infoUsuarios.addUsuario(nombre,email,password)
    return redirect(url_for('routes.registrado')) # Y REDIRIGIMOS A HOME DE NUE
  
@app.route('/registrado', methods=["GET","POST"])
def registrado():
    return render_template("registrado.html")