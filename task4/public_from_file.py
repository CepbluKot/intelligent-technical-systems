import paho.mqtt.client as mqtt
import time, random


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))


def on_publish(client, userdata, mid):
    print("sent data", mid)


client = mqtt.Client()
client.on_connect = on_connect
client.on_publish = on_publish
client.connect("localhost", 1883, 60)
client.loop_start()


def send(data):
    try:
        data = str(data)
        client.publish(data, payload=1, qos=2, retain=True)
        time.sleep(1)
    except:
        print("error - send data")


def read_file(filename: str):
    try:
        with open(filename, "r") as file:
            return file.read()
    except:
        print("error - read file")


if __name__ == "__main__":
    while True:
        # data_to_send = read_file('test_data')
        data_to_send = random.randint(0, 100)
        send(data_to_send)
        time.sleep(1)
