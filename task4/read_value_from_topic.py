import paho.mqtt.client as mqtt


v = [0, 0, 0]


def calculate_avg(recieved_val: int):
    try:
        global v
        recieved_val = int(recieved_val)
        if v[2]:
            if v[1]:
                v[0] = v[1]
            v[1] = v[2]

        v[2] = recieved_val

        return int(v[2] * 0.6 + v[1] * 0.3 + v[0] * 0.1)
    except:
        print("error - calc")


def on_connect(client: mqtt.Client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe(topic="#")


def on_message(client, userdata, msg: mqtt.MQTTMessage):
    # print('recieved data', 'curr topic:', msg.topic, 'cur_avg', calculate_avg(msg.topic))
    print("curr topic:", msg.topic, "cur_avg", calculate_avg(msg.topic))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("localhost", 1883, 60)
client.loop_forever()
