#Archivo principal en donde se parametrizan las cosas que se van instalando
import os #permite interacturar con el sistema operativo indistantemente en el que se encuentre para las variables de entorno
from flask import Flask, jsonify
from flask_migrate import Migrate #Libreria que da acceso a comandos para poder poblar la base de datos con las tablas, colummnas, datos.
from flask_cors import CORS #Permite establecer conexión con el front para hacer consultas con fetch. 
from dotenv import load_dotenv #Permite cargar en memoria la info del archivo .env.
from models import db #Permite vincular a través de migrate a app.py con models.py y los comandos de migrate.
from routes import api

load_dotenv()

app = Flask(__name__) #Instanacia de la aplicación Flask. Name hace referencia al mismo archivo.
#A continuación connfiguración de variables por medio de la propiedad config:
app.config['DEBUG'] = True #Permite saber si hay errores en modo desarrolo en true.
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False #En false permite que los cambios se han visibles pero cuando se generen las migraciones.
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')

db.init_app(app) # víncula el archivo models con la aplicación Flask
Migrate(app, db) # da accesso a los comandos db init, db migrate, db upgrade, db downgrade
CORS(app)

@app.route('/') #Ruta principal
def main():
    return jsonify({ "status": "App Running Successfully!"}), 200

app.register_blueprint(api, url_prefix='/api') #Víncula el archivo routes.py con el archivo app.py

if __name__ == '__main__': #condiciona si name es el archivo principal inicia app
    app.run()