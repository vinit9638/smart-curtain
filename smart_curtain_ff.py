import cv2
from  cvzone.HandTrackingModule import HandDetector
import paho.mqtt.client as mqtt
import ssl

def on_message(client, userdata, message):
    print("received message =", str(message.payload.decode("utf-8")))
def on_log(client, usedata, level, buf):
    print("log: ",buf)
def on_connect(client, userdata, flags , rc):
    print("Mqtt connected....",rc)

client = mqtt.Client("Vinit", True, None, mqtt.MQTTv31)
client.on_message = on_message
client.on_log = on_log
client.on_connect = on_connect
print("Connect to broker")
client.tls_set("server.pem", tls_version=ssl.PROTOCOL_TLSv1_2)
client.tls_insecure_set(value=False)
client.connect("mqtt.qkwik.com", port=8883, keepalive=60)


cap = cv2.VideoCapture(0)
cap.set(3,900)
cap.set(4,300)
detect_hand = HandDetector(detectionCon=0.8,maxHands=1)
flag_up, flag_down, flag_hold = True, True, True

while True:
    success, img  = cap.read()
    hands, img = detect_hand.findHands(img)
    if hands :
        hand = hands[0]
        finger = detect_hand.fingersUp(hand)
        # Gesture 1
        
        if finger == [0,1,1,1,0] and flag_up:
            print("Up")
            client.publish(topic="REEVA/BLE_MESH_GATEWAY/1C9DC2C31D2E/C/1", payload="""{"addr":5490,"type":"onoff","onoff":1}""")
        
            flag_up, flag_down, flag_hold = False, True, True

        # Gesture 2
        if finger == [0,1,1,0,0] and flag_down:
            print("Down")
            client.publish(topic="REEVA/BLE_MESH_GATEWAY/1C9DC2C31D2E/C/1", payload="""{"addr":5491,"type":"onoff","onoff":1}""")

            flag_up, flag_down, flag_hold = True, False, True

        
        # Gesture 3
        if finger == [1,1,1,1,1] and flag_hold:
            print("Hold")
            client.publish(topic="REEVA/BLE_MESH_GATEWAY/1C9DC2C31D2E/C/1", payload="""{"addr":5490,"type":"onoff","onoff":0}""")

            flag_up, flag_down, flag_hold = True, True, False

    cv2.imshow('frame', img)
    key = cv2.waitKey(1) 
    if  key == ord('q'):
        break

client.loop_forever()
