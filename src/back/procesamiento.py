import operator
from consultasDB import GetAll, IniciarConexion, CerrarConexion
from sklearn.metrics.pairwise import cosine_similarity

cursor, conexion = IniciarConexion()

def ObtenerSimilares(cantidad):
    imagenes = GetAll(cursor)
    vector = imagenes[25][1]
    similares = {}

    vector = vector[:-1]
    vector = vector[1:]
    vector = list(map(float, vector.split(" ")))

    for indice in range(0, cantidad-1):
        aux = imagenes[indice][1][:-1]
        aux = aux[1:]
        aux = list(map(float, aux.split(" ")))

        comparacion = cosine_similarity(vector.reshape((1, -1)), aux.reshape((1, -1)))

        similares[imagenes[indice][2]] = (comparacion)

    similares_sort = sorted(similares.items(), key=operator.itemgetter(1))

    print(similares_sort)

    '''for imagen in imagenes:
        comparacion = 
        for item in similares:'''

ObtenerSimilares(5)