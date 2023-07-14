# Local-Website-for-data-visualization
Simple website that receive and plot data from Firebase.
# Configuration
Create a new project on [Firebase console](https://console.firebase.google.com/)\
![image](https://github.com/Taiga-chann/Local-Website-for-data-visualization/assets/90364299/997c4331-52fb-4bce-a65b-4379501a5f77)\
Next, click ![image](https://github.com/Taiga-chann/Local-Website-for-data-visualization/assets/90364299/2d4e6f8f-b219-4e9e-8663-ba2443fe8c00) icon below project name and select web app.\
![image](https://github.com/Taiga-chann/Local-Website-for-data-visualization/assets/90364299/40887d0b-0b99-42a7-950a-55c70661b6de)\
After that, click to the web app you've created and choose setting ![image](https://github.com/Taiga-chann/Local-Website-for-data-visualization/assets/90364299/eb38f4b3-f2fa-4a4c-b81d-1596162a3ba8)\
Here you can see the project's setting. Scroll down until you see something like this:\
![image](https://github.com/Taiga-chann/Local-Website-for-data-visualization/assets/90364299/f53b1c8b-2e04-4b2d-b2cc-9962fcd3bd47)\
Copy all fields in `firebaseConfig` for later use.\
Now go back to `main.py` file. Paste the config you copied to `firebaseConfig`. Remember to change the configuration of Mqtt app\
![image](https://github.com/Taiga-chann/Local-Website-for-data-visualization/assets/90364299/557d3995-8773-4769-a3ef-b1e92f9632c6)\
If you want to learn more about the Mqtt configuration on flask app, read the [documentation](https://flask-mqtt.readthedocs.io/en/latest/).\
You also need to go to template\index.html, find `firebaseConfig` and change the configuration like in the `main.py` file.\
Now you done. Here is a little demo

https://github.com/Taiga-chann/Local-Website-for-data-visualization/assets/90364299/4e217907-53c8-4bb7-9fc7-816b0ea1d5df

