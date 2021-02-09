import operator
from src.back.consultasDB import GetAll, IniciarConexion, CerrarConexion
from sklearn.metrics.pairwise import cosine_similarity
import numpy


cursor, conexion = IniciarConexion()

def ObtenerSimilares(cantidad, vectorEntrada):
    imagenes = GetAll(cursor)
  
    #vector = numpy.asarray(imagenes[1][1])

    similares = {}

    for indice in range(0, (len(imagenes)-1)):
        
        comparacion = cosine_similarity(vectorEntrada.reshape((1, -1)), numpy.asarray(imagenes[indice][1]).reshape((1, -1)))[0][0]
        similares[imagenes[indice][2]] = comparacion*100

    similares_sort = dict(sorted(similares.items(), key=lambda item: item[1],reverse=True)[:cantidad])

    return(similares_sort, similares)


