from flask import Flask, render_template
from flask_mqtt import Mqtt
import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyDs_-trHHhERYIdxGQXTC2X9vOJjgv3De8",
    "authDomain": "miniproject-4b767.firebaseapp.com",
    "databaseURL": "https://miniproject-4b767-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "miniproject-4b767",
    "storageBucket": "miniproject-4b767.appspot.com",
    "messagingSenderId": "881832076020",
    "appId": "1:881832076020:web:11d52f63169fdb4764b4a1",
    "measurementId": "G-865J1P1CNZ"
}

firebase = pyrebase.initialize_app(firebaseConfig)
dataBase = firebase.database()

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'mqtt.flespi.io'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = 'dTdnqad1yuqQGMjMk7L36rEDD83IV88WSb789aXvsdbYNiyXfaParhDSfwqYtmI9'
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
app.config['MQTT_TLS_ENABLED'] = False
mqtt = Mqtt(app)

@app.route('/')
def hello():
    return render_template('index.html')

# xu ly su kien on_connect
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    # subscribe cac topic de nhan du lieu
    mqtt.subscribe('/smarthome/temp')
    mqtt.subscribe('/smarthome/humid')
    mqtt.subscribe('/smarthome/rain')

# xu ly su kien on_message
@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    # tao 1 dictionary de luu du lieu gui den
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print (data["topic"],": Data received!\n")
    # xu ly: khi du lieu duoc gui den topic tuong ung, cap nhat va luu lai tren firebase
    if data['topic'] == '/smarthome/temp':
        dataTemp = float(data['payload'])
        # cap nhat du lieu
        dataBase.child("Sensor").update({"Temp":dataTemp})
        # luu du lieu
        dataBase.child("zData").push({"Temp":dataTemp})
    elif data['topic'] == '/smarthome/humid':
        dataHumid = float(data['payload'])
        dataBase.child("Sensor").update({"Humid":dataHumid})
        dataBase.child("zData").push({"Humid":dataHumid})
    elif data['topic'] == '/smarthome/rain' :
        dataRain = float(data['payload'])
        dataBase.child("Sensor").update({"Rain":dataRain})
        dataBase.child("zData").push({"Rain":dataRain})

if __name__ == '__main__':
    app.run()