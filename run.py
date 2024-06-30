from flask import Flask
from app.views import * #Se importa todos los metodos de 'app.views'
from app.database import init_app #importamos la funcion de database

#se inicia el proyecto flask
app = Flask(__name__)

init_app(app)

#----------------------------------------------------------------------------------------
#Cuando accedemos a la ruta /mostrar_todos_viajes, se ejecutara mostrar todos los viajes
app.route('/mostrar_todos_viajes',methods=['GET'])(mostrar_todos_viajes)#funcion de views

#----------------------------------------------------------------------------------------
#Cuando accedemos a la ruta /mostrar_viajes, se ejecutara mostrar un viaje en especifico
app.route('/mostrar_viajes',methords=['GET'])(mostrar_viajes)#funcion de views

#----------------------------------------------------------------------------------------
# #Cuando accedemos a la ruta /agregar_viajes, se ejecutara agregar viajes
# app.route('/agregar_viajes',methords=['POST'])(agregar_viajes)#funcion de views

#----------------------------------------------------------------------------------------
# #Cuando accedemos a la ruta /modificar_viajes, se ejecutara modificar viajes
# app.route('/modificar_viajes',methods=['PUT'])(modificar_viajes)#funcion de views

#----------------------------------------------------------------------------------------
#Cuando accedemos a la ruta /eliminar_viajes, se ejecutara mostrar todos los viajes
app.route('/eliminar_viaje',methods=['DELET'])(eliminar_viajes)#funcion de views



if __name__ == '__main__':
    app.run(debug=True)
