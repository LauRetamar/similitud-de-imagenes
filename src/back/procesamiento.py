import operator
from consultasDB import GetAll, IniciarConexion, CerrarConexion
from sklearn.metrics.pairwise import cosine_similarity
import numpy



cursor, conexion = IniciarConexion()

def ObtenerSimilares(cantidad):
    imagenes = GetAll(cursor)
  
    vector = numpy.asarray(imagenes[1][1])
    similares = {}

    for indice in range(0, cantidad-1):
        
        comparacion = cosine_similarity(vector.reshape((1, -1)), numpy.asarray(imagenes[indice][1]).reshape((1, -1)))[0][0]
        print(comparacion)
        similares[imagenes[indice][2]] = comparacion

    similares_sort = sorted(similares.items(), key=operator.itemgetter(1))

    print(similares_sort)

    '''for imagen in imagenes:
        comparacion = 
        for item in similares:'''

ObtenerSimilares(5)