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

def GetAll(cursor):
    try:
        
        
        cursor.execute('SELECT * FROM imagenes;')
        return(print(cursor.fetchall()))


    except(Exception, Error) as error:
        print('Error!' , error)



def Insert(cursor,vector, ruta):
    try:      
        cursor.execute('''INSERT INTO imagenes(vector, ruta) VALUES('{}','{}');'''.format(vector,ruta))
        print('insertado')


    except(Exception, Error) as error:
        print('Error!' , error)

   
def CerrarConexion(connection):
    if(connection):
            connection.commit()
            cursor.close()
            connection.close()
            print('Conexion finalizada :)')


#Insert(3,3)
#print(GetAll())

img2vec = Img2Vec()

input_path = '../../imagenes/imagenes-frutas/'
pics = {}

cursor, connection = IniciarConexion()

for file in os.listdir(input_path):
    filename = os.fsdecode(file)
    img = Image.open(os.path.join(input_path, filename))
    vec = img2vec.get_vec(img)
    
    Insert(cursor,vec,file)

CerrarConexion(connection)



