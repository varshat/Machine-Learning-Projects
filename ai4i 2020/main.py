from flask import Flask, render_template, request
from flask import jsonify
import requests
import pickle
#import numpy as np
#import sklearn
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)
model = pickle.load(open('Linear_Regression_model.pickle', 'rb'))

@app.route('/',methods=['GET'])
def Home():
    return render_template('test.html')

@app.route("/predict", methods=['POST'])
def predict():

    if request.method == 'POST':
        ProcessTemp = float(request.form['process'])
        hdf = int(request.form['hdf'])
        prediction = model.predict([[ProcessTemp,hdf]])
        output = round(prediction[0],2)
        if output < 0:
            return render_template('test.html',prediction_texts="Please try with valid inputs")
        else:
            return render_template('test.html',prediction_text="The Predicted Air Temperature is {}".format(output))
    else:
        return render_template('test.html')

if __name__=="__main__":
    app.run(debug=True)