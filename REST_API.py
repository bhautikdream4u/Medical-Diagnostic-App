import pickle
import numpy as np
from flask import Flask, request, json, jsonify

app = Flask(__name__)

filename = 'diabetes.sav'

loaded_model = pickle.load(open(filename,'rb'))
@app.route('/diabetes/v1/predict', methods = ['POST'])

def predict():
    #--- get the features to predict ---
    features = request.json

    #---create the features list for prediction---
    features_list = [features["Glucose"], features["BMI"], features["Age"]]

    #---get the prediction class---
    prediction = loaded_model.predict([features_list])
    confidence = loaded_model.predict_proba([features_list])

    #---formulate the response to return to client---
    response = {}
    response['prediction'] = int(prediction[0])
    response['confidence'] = str(round(np.amax(confidence[0]) * 100, 2))
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)    