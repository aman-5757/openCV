import paho.mqtt.client as mqtt
import time
import random
def lambda_handler(event= None, context= None):
    

    
    def on_connect(client, userdata, flags, rc):
        print("Connected with code :"+str(rc))
        client.subscribe("aakashk_kvjp58/f/otp")
    def on_message(client, userdata, msg):
        print(str(msg.payload))
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set("aakashk_kvjp58", "46f406136c5e4e5f874e283f95ed3dfc")
    client.connect("io.adafruit.com", 1883, 60)
    client.loop_start()
    time.sleep(1)
    client.publish("aakashk_kvjp58/f/otp", random.randint(1000,9999), qos =1)
    print('msg sent!')
    time.sleep(15)
    client.loop_stop()
    client.disconnect()


