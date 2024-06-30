#En este archivo se recibe la url con las peticiones para que ejecute models.py
# y ejecute las funciones para conectarse a la base de datos 

from flask import jsonify #Se importa funcion que permite convertir en archivo .json
from app.models import Viajes #Se importa de models, la clase 'Viajes'


#--------------------------------------------------------------------------
#funcion para mostrar todos los viajes que tengamos
def mostrar_todos_viajes():
    viajes = Viajes.mostrar_todo()
    return jsonify(viajes) #me convierte lo obtenido en mostrar_todos_viajes a formato .json

#--------------------------------------------------------------------------
#funcion para mostrar 1 viaje en especifico
def mostrar_viajes(id_viaje):
    viajes = Viajes.mostrar_1(id_viaje)

    if viajes == None: #si no existe viaje, devolvemos mensaje de no encontrado
        return jsonify({'message': 'viaje no encontrado'})
    else:
        return jsonify(viajes)
    
#--------------------------------------------------------------------------
'''
#funcion para agregar un viaje
def agregar_viajes(): # podria ser agregar viajes al carrito?
    pass
    return jsonify({'mensaje':'viaje agregado correctamente'}) #Me devuelve en formato .json
'''
#--------------------------------------------------------------------------
'''
#funcion para modificar los viajes
def modificar_viajes(): #podria ser eliminar viajes?
    pass
    #return jsonify({'mensaje':'viaje eliminado correctamente'}) #Me devuelve formato .json
'''
#--------------------------------------------------------------------------
#funcion para eliminar un viaje en especifico
def eliminar_viajes():
    viajes = Viajes.mostrar_1() #buscamo si existe ese viaje
    if viajes == None:
        return jsonify({'message': 'viaje no encontrado'})
    else:
        viajes.eliminar_1()
        return jsonify({'message': 'viaje eliminado'})
    