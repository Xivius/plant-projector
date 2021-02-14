from os import environ
from environs import Env
from mysql import connector
from requests.auth import HTTPBasicAuth
import requests
import tensorflow as tf
from flask import (
    Flask, escape, jsonify, render_template, request
)

app = Flask(__name__)
env = Env()
env.read_env()
mysql = connector.connect(
    host=environ["DB_HOST"],
    user=environ["DB_USER"],
    password=environ["DB_PASS"],
    database=environ["DB_NAME"],
    autocommit=True
)

@app.route('/', methods=['GET'])
def home():
    return render_template('test.html')

@app.route('/analyze', methods=['POST'])
def categorize():
    data = request.get_json()
    print(data)

    # classify plant based on img
    img = tf.io.decode_base64(data.img)
    model = tf.keras.models.load_model('model.h5')
    result = model.predict([data.image])[0]

    # get plant data based on classification
    sql = "SELECT * FROM plant_data WHERE name = %s"
    cursor = mysql.cursor(prepared=True)
    cursor.execute(sql, (result,))
    plant_data = cursor.fetchall()
    plant_temp_upper = 0
    plant_temp_lower = 0
    plant_abs_temp_upper = 0
    plant_abs_temp_lower = 0
    for d in plant_data:
        plant_temp_upper = d[2]
        plant_temp_lower = d[3]
        plant_abs_temp_upper = d[4]
        plant_abs_temp_lower = d[5]

    # get weather data for further processing
    possible_outcomes = [
        "misshapen/catfaced yield", "optimal", "reduced yield", "poor fruit set", "danger of dying"
    ]
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={data.y}&lon={data.x}&appid={environ["WEATHER_API_KEY"]}"
    headers = {"Accept": "application/json"}
    weatherData = requests.get(url, headers=headers)
    min_temp = weatherData["main"]["temp_min"]
    min_temp = ((min_temp - 273.15) * 1.8) + 32
    max_temp = weatherData["main"]["temp_max"]
    max_temp = ((max_temp - 273.15) * 1.8) + 32
    situation = ""

    if min_temp <= plant_abs_temp_lower:
        situation = possible_outcomes[3]
    elif max_temp >= plant_abs_temp_upper:
        situation = possible_outcomes[2]
    elif min_temp <= plant_temp_lower:
        situation = possible_outcomes[0]
    elif max_temp <= plant_temp_upper:
        situation = possible_outcomes[1]

    return jsonify({
        "plant-type": result[0],
        "outcome": situation
    })

if __name__ == "__main__":
    app.run(
        host=(env("HOST_IP") if 'HOST_IP' in environ else '127.0.0.1'),
        port=8000, debug=True, ssl_context='adhoc'
    )
