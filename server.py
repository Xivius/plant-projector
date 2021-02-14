from os import environ
from environs import Env
from flaskext.mysql import MySQL
import requests
import tensorflow as tf
from flask import (
    Flask, escape, jsonify, render_template, request
)

app = Flask(__name__)
env = Env()
env.read_env()
mysql = MySQL(app, prefix="mysql1",
    host=environ["DB_HOST"],
    user=environ["DB_USER"],
    password=environ["DB_PASS"],
    db=environ["DB_NAME"],
    autocommit=True
)

@app.route('/', methods=['GET'])
def home():
    return render_template('test.html')

@app.route('/analyze', methods=['POST'])
def categorize():
    data = request.get_json()
    print(data)
    img = tf.io.decode_base64(data.img)
    model = tf.keras.models.load_model('model.h5')
    result = model.predict([data.image])
    cursor = mysql.get_db().cursor()
    weatherData = requests.get("http://api.weatherapi.com/v1/current.json")



    return jsonify({
        "plant-type": result[0],
        "outcome":
    })

if __name__ == "__main__":
    app.run(
        host=(env("HOST_IP") if 'HOST_IP' in environ else '127.0.0.1'),
        port=8000, debug=True, ssl_context='adhoc'
    )
