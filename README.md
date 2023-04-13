# Smart-curtain
This project is a smart curtains system that allows you to control the open, close, and hold status of your curtains using hand gestures. The system is built using Bluetooth mesh technology and is connected through an MQTT gateway.

# Requirements
Python 3.x
Paho MQTT library
CVzone library
cv2 library
ssl library
Cloud MQTT server with certificate file (or local MQTT server)

# Installation

1. Clone the repository to your local machine:
> git clone https://github.com/vinit9638/smart-curtain.git
2. Install the required libraries using pip:
> pip install paho-mqtt cvzone opencv-python ssl
3. Open the config.py file and update the MQTT_SERVER, MQTT_PORT, MQTT_USERNAME, MQTT_PASSWORD, MQTT_TOPIC, MQTT_CERT_FILE, and GESTURE_TIME settings to match your MQTT server and certificate file information.
4. python smart_curtain.py

# Usage

To use the smart curtain system, make sure that the camera module is set up and connected to the system. Then, run the smart_curtain.py file to start the program. You should see the system connect to the MQTT server and start listening for hand gesture commands.

To open the curtains, use three fingers, To close the curtains, use two fingers and for hold use five fingers
