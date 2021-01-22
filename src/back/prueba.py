from img2vec_pytorch import Img2Vec
from PIL import Image

# Initialize Img2Vec with GPU
img2vec = Img2Vec(cuda=True)

# Read in an image
img = Image.open('E:\DESARROLLO\GAD\repoimagenes\Fruit-Images-Dataset\Training\Apple Braeburn/')
# Get a vector from img2vec, returned as a torch FloatTensor
vec = img2vec.get_vec(img, tensor=True)
# Or submit a list
vectors = img2vec.get_vec(list_of_PIL_images)