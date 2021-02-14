from environs import Env
from flaskext.mysql import MySQL
import tensorflow as tf
from flask import (
    Flask, escape, jsonify, render_template, request
)

app = Flask(__name__)
env = Env()
mysql = MySQL(app, prefix="mysql1",
    host=env("DB_HOST"),
    user=env("DB_USER"),
    password=env("DB_PASS"),
    db=env("DB_NAME"),
    autocommit=True
)

@app.route('/', methods=['GET'])
def home():
    return render_template('test.html')

@app.route('/categorize', methods=['POST'])
def categorize():
    data = request.get_json()
    model = tf.keras.models.load_model('plant_classifier.h5')
    result = model.predict([data.image])
    return jsonify({"type": result[0]})


app.run()
