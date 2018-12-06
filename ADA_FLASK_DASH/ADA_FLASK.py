from flask import Flask, jsonify, abort, request
import pandas as pd
import numpy as np
import pickle


app = Flask(__name__)

@app.route('/api/v1.0/linear', methods=['GET'])
def get_properties():
    path = 'pathToYourSavedModel'
    model = pickle.load(open(path, 'rb'))

    meret = request.args['p'].split()[0]
    szoba = request.args['p'].split()[1]

    prediction = model.predict([[int(meret), int(szoba)]])

    return jsonify({'prediction': float(prediction) })


@app.route('/api/v1.0/random', methods=['GET'])
def get_randomforest_prediction():
    path = 'PathToYourSavedModel'
    model = pickle.load(open(path, 'rb'))

    meret = request.args['p'].split()[0]
    szoba = request.args['p'].split()[1]

    prediction = model.predict([[int(meret), int(szoba)]])

    return jsonify({'prediction': float(prediction)})


if __name__ == '__main__':
    app.run(debug=True)
