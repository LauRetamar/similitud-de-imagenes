#Lo mismo que el otro pero intenta guardar el vector en un arreglo de float para su facil procesamiento posterior

import sys
import os
sys.path.append("../img2vec_pytorch")  # Adds higher directory to python modules path.
from img2vec_pytorch import Img2Vec
import psycopg2
from psycopg2 import Error
from PIL import Image


def IniciarConexion():
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="sql",
                                        host="localhost",
                                        port="5432",
                                        database="frutas")

        cursor = connection.cursor()        
        return cursor, connection

    except(Exception, Error) as error:
        print('Error!' , error)




def Insert(cursor,vector, ruta):
    try:      
        cursor.execute('''INSERT INTO imagenes2(vector, ruta) VALUES('{}','{}');'''.format(vector,ruta))
        print('insertado')

    except(Exception, Error) as error:
        print('Error!' , error)

   
def CerrarConexion(connection):
    if(connection):
            connection.commit()
            cursor.close()
            connection.close()
            print('Conexion finalizada :)')




img2vec = Img2Vec()

input_path = './imagenes/imagenes-frutas/'
pics = {}

cursor, connection = IniciarConexion()

i = 0
for file in os.listdir(input_path):

    filename = os.fsdecode(file)
    img = Image.open(os.path.join(input_path, filename))
    vec = img2vec.get_vec(img)
    
    #Acomodando formato
    vec = str(vec)
    vec = vec.replace('[','{')
    vec = vec.replace(']','}')
    vec = vec.replace(' ',', ')

    Insert(cursor,vec,file)
    
    if (i == 10):
        
        print('listo los 10')
        break
    i += 1

CerrarConexion(connection)


