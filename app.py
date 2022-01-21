from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('stacking_classifiers.pkl', 'rb'))


@app.route('/', methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()


@app.route("/predict", methods=['POST'])
def predict():
    Fuel_Type_Diesel = 0
    if request.method == 'POST':
        Text = request.form['Text']
        prediction = model.predict([Text])
        output = prediction[0]
        if output == 0:
            return render_template('index.html', prediction_text="This is not sarcastic sentence.")
        else:
            return render_template('index.html', prediction_text="This is sarcastic sentence.")
    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(host='127.0.0.2', debug=True)
