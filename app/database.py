# Archivo con toda la logica que va a permitir conectar con la base de datos 
# y otras funciones extras
# (Archivo comun a todos los grupos)


import os
import mysql.connector      #Ver esta linea
from flask import g
from dotenv import load_dotenv      #ver esta linea

load_dotenv()

DATABASE_CONFIG = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_NAME'),
    'port': os.getenv('DB_PORT', '''numero de puerto''')
}

# Funcion para establecer la conexion con la base de datos
# dependiendo de si ya esta conectada o si creamos una nueva conexion
def get_db():
    #preguntamos si existe la conexion, si no existe la creamos
    if 'db' not in g:
        g.db = mysql.connector.connect(**DATABASE_CONFIG)
    #si esta creada la retorno.
    return g.db

# Funcion que me permite cerrar la conexion a la base de datos
def close_db(e=None):

    db = g.pop('db',None)

    if db is not None:
        db.close()

#Funcion para iniciar la palicacion con el manejo de la base
def init_app(app):
    # antes de realizar un return en la vista deberiamos cerrar la conexion
    app.teardown_appcontext(close_db)
