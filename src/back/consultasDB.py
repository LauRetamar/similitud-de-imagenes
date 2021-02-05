import sys
import os
import psycopg2
from psycopg2 import Error

def IniciarConexion():
    try:
        connection = psycopg2.connect(user="postgres",
                                        password="postgre",
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
        return(cursor.fetchall())


    except(Exception, Error) as error:
        print('Error!' , error)
   
def CerrarConexion(connection):
    if(connection):
            connection.commit()
            cursor.close()
            connection.close()
            print('Conexion finalizada :)')



cursor, conexion = IniciarConexion()
db = GetAll(cursor)
CerrarConexion(conexion)
