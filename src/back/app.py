import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
from PIL import Image
from img2vec_pytorch import Img2Vec
from procesamiento import ObtenerSimilares



UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'C:\imgGAD'


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # if user does not select file, browser also
        # submit an empty part without filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            img = Image.open(request.files['file'].stream)
            img2vec = Img2Vec()
            # The next line generates and stores the image vector in the 'vec' variable.
            vec = img2vec.get_vec(img)
            print(ObtenerSimilares(5,vec))
            # print(vec)

    return '''
    <!doctype html>
    <title>Similitud de frutas</title>
    <h1>Elija una imagen para encontrar las frutas más similares.</h1>
    <h2>¡Nuestra base de datos cuenta con más de 31.000 imágenes!</h2>
    <form method=post enctype=multipart/form-data>
      <input id="fileinput" type=file name=file>
      <br>
      <br>
      <input type=submit value=Comparar>
      <br>
      <br>
      <img id="output">
    </form>
    '''


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
