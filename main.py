from flask import Flask, render_template
from flask_mqtt import Mqtt
import pyrebase

firebaseConfig = {
    "apiKey": "YOUR_CONFIG_ON_FIREBASE",
    "authDomain": "YOUR_CONFIG_ON_FIREBASE",
    "databaseURL": "YOUR_CONFIG_ON_FIREBASE",
    "projectId": "YOUR_CONFIG_ON_FIREBASE",
    "storageBucket": "YOUR_CONFIG_ON_FIREBASE",
    "messagingSenderId": "YOUR_CONFIG_ON_FIREBASE",
    "appId": "YOUR_CONFIG_ON_FIREBASE",
    "measurementId": "YOUR_CONFIG_ON_FIREBASE"
}

firebase = pyrebase.initialize_app(firebaseConfig)
dataBase = firebase.database()

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = 'mqtt.flespi.io'
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_USERNAME'] = 'PUT_YOUR_TOKEN_HERE'
app.config['MQTT_PASSWORD'] = ''
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
app.config['MQTT_TLS_ENABLED'] = False
mqtt = Mqtt(app)

@app.route('/')
def hello():
    return render_template('index.html')

# Handle on_connect event
@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    # Subscribe to topics to receive data
    mqtt.subscribe('/smarthome/temp')
    mqtt.subscribe('/smarthome/humid')
    mqtt.subscribe('/smarthome/rain')

# Handle on_message event
@mqtt.on_message()
def handle_mqtt_message(client, userdata, message):
    # Create a dictionary to save received data
    data = dict(
        topic=message.topic,
        payload=message.payload.decode()
    )
    print (data["topic"],": Data received!\n")
    # When received data, update and save on Firebase realtime database
    if data['topic'] == '/smarthome/temp':
        dataTemp = float(data['payload'])
        # Update data
        dataBase.child("Sensor").update({"Temp":dataTemp})
        # Save data
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
