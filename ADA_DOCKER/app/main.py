from flask import Flask, jsonify, request
from minio import Minio
import joblib
from io import BytesIO

app = Flask(__name__)

minio_client = Minio(
        endpoint='minio1:9000',
        access_key='asd',
        secret_key='asdasdasd',
        secure=False
)

@app.route("/")
def hello():
    data = minio_client.get_object('model', 'random123.pkl')
    model = joblib.load(BytesIO(data.data))
    pred = model.predict([[2,3]])
    return jsonify({'prediction': float(pred)})
    



if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
