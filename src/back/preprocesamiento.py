import sys
import os
sys.path.append("../img2vec_pytorch")  # Adds higher directory to python modules path.
from img2vec_pytorch import Img2Vec
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity
import psycopg2

conn = psycopg2.connect("dbname=frutas user=postgres")

print(conn)
cur = conn.cursor()
print(cur)
cur.execute('CREATE TABLE fruits(id serial PRIMARY KEY, clave varchar, vector varchar)')


#print(conn.query('SELECT * FROM frutas'))

"""
#path de carpeta de imegenes
input_path = '../../imagenes/imagenes-frutas/'

print("Getting vectors for test images...\n")
img2vec = Img2Vec()




def guardarEnDB(clave,vec):
    cur.execute("INSERT INTO fruits (clave, vector) VALUES (clave,vec))
    conn.commit()

cur.close()
conn.close()

# For each test image, we store the filename and vector as key, value in a dictionary
pics = {}
for file in os.listdir(input_path):
    filename = os.fsdecode(file)
    img = Image.open(os.path.join(input_path, filename))
    vec = img2vec.get_vec(img)
    guardarEnDB(filename,vec)



available_filenames = ", ".join(pics.keys())
pic_name = ""
while pic_name != "exit":
    pic_name = str(input("\nWhich filename would you like similarities for?\nAvailable options: " + available_filenames + "\n"))

    try:
        sims = {}
        for key in list(pics.keys()):
            if key == pic_name:
                continue

            sims[key] = cosine_similarity(pics[pic_name].reshape((1, -1)), pics[key].reshape((1, -1)))[0][0]

        d_view = [(v, k) for k, v in sims.items()]
        d_view.sort(reverse=True)
        for v, k in d_view:
            print(v, k)

    except KeyError as e:
        print('Could not find filename %s' % e)

    except Exception as e:
        print(e)

"""
