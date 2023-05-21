from flask import Flask
import mysql.connector  # IMPORTAMOS LO QUE HEMOS INSTALADO PIP INSTALL MYSQL.......

#db = list()
database = mysql.connector.connect( # LLAMAMOS AL FUNCION CONNECT PARA CONECTARNOS
    host ='btug0fx7ljzszoqysnwl-mysql.services.clever-cloud.com', #NUESTRO HOST, ESTA EN EL DOCKER COMPOSE
    port = 3306,
    user ='up8pf5catvcodukz', #USUARIO QUE USAMOS NOSOTROS
    password ='wEo63IA2urQveLCLPiWl', #CONTRASEÑA CON LA QUE NOS CONECTAMOS
    database='btug0fx7ljzszoqysnwl'
) 

def create_app():
    app = Flask(__name__)
    app.debug = True
    
    from .routes import routes

    app.register_blueprint(routes.app)

    return app

