import paho.mqtt.client as mqtt
import time, random


class MqttPoster:
    def __init__(self) -> None:
        self.client = mqtt.Client()
        self.client.connect("localhost", 1883, 60)
        self.client.loop_start()


    def send(self, data):
        # try:
            data = str(data)
            self.client.publish( 'position', data)
            time.sleep(0.1)
        # except:
        #     print("error - send mqtt data")
