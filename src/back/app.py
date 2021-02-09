import os
from flask import Flask, flash, request, redirect, url_for, send_from_directory, render_template
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
    data = ''

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
            
        
            data = (ObtenerSimilares(5,vec))

            rutas = []
            porcentajes = []
            for key in data:
                 rutas.append(key)
                 porcentajes.append(data[key].round(3))
            
            #rutaimagen1 = '../../imagenes/imagenes-frutas/' + rutas[0]
       
            
   
            
  
            return render_template('home.html', ruta0 = rutas[0], coincidencia0 = porcentajes[0])
                   

            
    if  request.method == 'GET':
        return render_template('home.html')


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)
