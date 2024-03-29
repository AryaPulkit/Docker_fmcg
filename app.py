# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 17:03:17 2020

"""

import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
app=Flask(__name__,template_folder='templates')

model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    print(request.form)
   
    int_features = [int(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    
    print(int_features)
    print(final_features)
    
    prediction = model.predict(final_features)

    output = round(prediction[0], 4)

    return render_template('index.html', prediction_text='Achieved Sales Value is  $ {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
