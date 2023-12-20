from flask import Flask,jsonify,request
import numpy as numpy
from io import BytesIO
from PIL import Image
import tensorflow as tf
import numpy as np

app = Flask(__name__)

CLASS_NAMES = ['glioma', 'meningioma', 'notumor', 'pituitary']
MODEL = tf.keras.models.load_model('D:/brain_tumor_classification_project/brain_tumor_model.h5')

@app.route('/hello')
def hello():
    return "hello everyone"

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

    predications = MODEL.predict(img_batch)
    predicted_class = CLASS_NAMES[np.argmax(predications[0])]
    confidence = np.max(predications[0])

    return {
        'class':predicted_class,
        'confidence':float(confidence)
    }

    
    
if __name__ == '__main__':
    app.run()
