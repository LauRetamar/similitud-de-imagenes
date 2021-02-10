import sys
import os
sys.path.append("../img2vec_pytorch")  # Adds higher directory to python modules path.
from img2vec_pytorch import Img2Vec
import psycopg2
from psycopg2 import Error
from PIL import Image
from progress.bar import Bar, ChargingBar
import time

def IniciarConexion():
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="xxxx",
                                        host="localhost",
                                        port="5432",
                                        database="frutas")

        cursor = connection.cursor()        
        return cursor, connection

    except(Exception, Error) as error:
        print('Error iniciando conexión!' , error)


def CrearTabla(cursor):
    try:      
        cursor.execute('''CREATE TABLE imagenes(id serial PRIMARY KEY, vector real[], ruta varchar)''')
        print('Tabla creada')
    except(Exception, Error) as error:
        print('Error creando tabla!' , error)


def Insert(cursor,vector, ruta):
    try:      
        cursor.execute('''INSERT INTO imagenes(vector, ruta) VALUES('{}','{}');'''.format(vector,ruta))

    except(Exception, Error) as error:
        while(True):
            print('Ruta defectuosa: ' + ruta)
            time.sleep(2)
        print('Error insertando!' , error)
        
   

   
def CerrarConexion(connection):
    if(connection):
            connection.commit()
            cursor.close()
            connection.close()
            print('Conexion finalizada :)')



img2vec = Img2Vec()

input_path = './static/'
pics = {}

cursor, connection = IniciarConexion()
CrearTabla(cursor)

bar1 = Bar('Procesando:', max=31688)


for file in os.listdir(input_path):

    filename = os.fsdecode(file)
    img = Image.open(os.path.join(input_path, filename))
    vec = img2vec.get_vec(img)
    
    vec = str(vec)
    vec = vec.replace('[','{')
    vec = vec.replace(']','}')
    vec = vec.replace(' ',', ')

    Insert(cursor,vec,file)


    bar1.next()

CerrarConexion(connection)
bar1.finish()



