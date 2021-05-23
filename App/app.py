# importing the required libraries
import numpy as np
from flask import Flask, render_template, request
from os.path import join, dirname, realpath
from tensorflow import keras
from keras.preprocessing.image import load_img,img_to_array
from werkzeug.utils import secure_filename
import os


app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config["CACHE_TYPE"] = "null"
app.static_folder = 'static'
f = ""
original_filename =""
UPLOADS_PATH = join(dirname(realpath(__file__)), 'static\\')

def get_array(img_path):
  img = load_img(img_path,target_size=(224,224))
  img = img_to_array(img)
  img = np.expand_dims(img,axis=0)
  return img


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    #For rendering results on HTML GUI
    f = request.files['file']
    f.save(os.path.join(UPLOADS_PATH,f.filename))
    original_filename = f.filename
    path = "G:\Academics\SSN\\6th Sem\Chest-Xray-System\Covid -19 Prediction Using Chest X-rays\App\static\\"+original_filename
    test_1 = get_array(path)
    model = keras.models.load_model("model_1.h5")
    result_1 = model.predict_classes(test_1)
    output = {1:"Covid patient😭😱",0:"Normal patient😎😋"}
    res = output[result_1[0][0]]
    return render_template('index.html', output='Result :{}'.format(res))

if __name__ == "__main__":
    app.run(debug=True)