# Se definen modelos que contienen metodos para interactuar con la base de datos

from app.database import get_db #importamos get_db para que podamos conectarnos a la base de datos


#Creamos la clase Viajes
class Viajes: 
    def __init__(self,id_viaje=None, pais=None, destino=None, precio=None):
        self.id_viaje = id_viaje
        self.pais = pais
        self.destino = destino
        self.precio = precio

#--------------------------------------------------------------------------
#Modelo para traer listado de viajes
@staticmethod
def mostrar_todos():
    conex = get_db() #se establece la coneccion con la bd
    cursor = conex.cursor() #se crea el objeto cursor(que permite hacer consultas y obtener resultados de la bd)
    cursor.execute("SELECT * FROM viajes") #de ese cursor ejecutamos que traiga todos los datos de la tabla 'viajes' (tabla viajes deberia ser nuestra tabla en la base de datos)
    rows = cursor.fetchall() #sirve para recuperar las filas de resultados obtenidos arriba y se guardan en la tupla 'rows'(filas)
   
    viaje = []
    for i in rows:
        viaje_nuevo = Viajes(id_viaje=i[0],pais=i[1], destino=i[2], precio=i[3])
        viaje.append(viaje_nuevo)

    cursor.close() #cerramos cursor
    return viaje

#--------------------------------------------------------------------------
#Modelo para traer un viaje en especifico
@staticmethod
def mostrar_1():
    conex = get_db() #se establece la coneccion con la bd
    cursor = conex.cursor() #se crea el objeto cursor(que permite hacer consultas y obtener resultados de la bd)
    cursor.execute("SELECT * FROM viajes WHERE id_viajes = %s",(id_viaje,)) #de ese cursor ejecutamos que traiga todos los datos de la tabla 'viajes' (tabla viajes deberia ser nuestra tabla en la base de datos)
    i = cursor.fetchone() #sirve para recuperar la fila de resultados obtenidos arriba y se guardan en la tupla 'i'
    
    if i != []: #Si i es distinto de vacio   - ver si funciona o sino i != None
        viaje = Viajes(id_viaje=i[0], pais=i[1], destino=i[2], precio=i[3])   
    else: #si es vacio, no hay viaje con ese id
        viaje = None
    
    return viaje

#--------------------------------------------------------------------------
'''
#Modelo para agregar un viaje a la base de dato
@staticmethod
def agregar_1():
    conex = get_db() #se establece la coneccion con la bd
    cursor = conex.cursor() #se crea el objeto cursor(que permite hacer consultas y obtener resultados de la bd)
    cursor.execute("INSERT INTO viajes(id_viaje, pais, destino, precio) VALUES ()") #de ese cursor ejecutamos que se cree los datos para la tabla 'viajes'
    rows = cursor.fetchone() #sirve para recuperar la fila de resultados obtenidos arriba y se guardan en la tupla 'i'
    cursor.close() #cerramos cursor
    if rows != []:
        return viajes(pais=rows[0], destino=rows[1], precio=rows[2])
    else:
        return None
    
'''
#--------------------------------------------------------------------------
@staticmethod
def eliminar_1():
    conex = get_db() #se establece la coneccion con la bd
    cursor = conex.cursor() #se crea el objeto cursor(que permite hacer consultas y obtener resultados de la bd)
    cursor.execute("DELETE FROM viajes WHERE id_viaje = %s", (self.id_viaje))
    conex.commit()
    cursor.close()
    