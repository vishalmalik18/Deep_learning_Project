from flask import Flask,request,jsonify
import numpy as np
from io import BytesIO
from PIL import Image
import tensorflow as tf

app = Flask(__name__)

CLASS_NAMES = ['NORMAL','PNEUMONIA']
MODEL = tf.keras.models.load_model('D:/chest_xray/Chest_XRay.h5')

@app.route('/hello')

def hello():
    return "Hello everyone"


def read_file_as_image(data,target_size=(256,256)) -> np.ndarray:
    image = Image.open(BytesIO(data))
    image = image.resize(target_size)
    image= np.array(image)
    return image

@app.route('/predict',methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error':'No file part'})
    
    file = request.files['file']

    image = read_file_as_image(file.read())
    img_batch = np.expand_dims(image,0)

    predication = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predication[0])]
    confidence = np.max(predication[0])

    return {
        'class':predicted_class,
        'confidence':float(confidence)
    }


if __name__ == '__main__':
    app.run()