import paho.mqtt.client as mqtt
import json
import time

MQTT_BROKER = "new-vynhu0.a02.usw2.aws.hivemq.cloud"  # Replace with your MQTT broker address
MQTT_PORT = 1883

TOPICS = {
    "order": 0,
    "instantActions": 0,
    "state": 0,
    "visualization": 0,
    "connection": 1,
}

def on_connect(client, userdata, flags, rc, properties=None):
    print("Connected with result code " + str(rc))
    for topic, qos in TOPICS.items():
        client.subscribe(topic, qos=qos)

def on_message(client, userdata, msg):
    print(f"Message received on topic {msg.topic}: {msg.payload.decode()}")
    handle_message(msg.topic, msg.payload.decode())

def handle_message(topic, payload):
    data = json.loads(payload)
    if topic == "order":
        execute_order(data)
    elif topic == "instantActions":
        execute_instant_action(data)
    elif topic == "state":
        print("State message received")
    elif topic == "visualization":
        print("Visualization message received")
    elif topic == "connection":
        print("Connection message received")

def execute_order(order):
    print(f"Executing order: {order}")

def execute_instant_action(action):
    print(f"Executing instant action: {action}")

def publish_state(client, state):
    client.publish("state", json.dumps(state))

def publish_visualization(client, visualization):
    client.publish("visualization", json.dumps(visualization))

def publish_connection(client, connection):
    client.publish("connection", json.dumps(connection))

client = mqtt.Client(protocol=mqtt.MQTTv5)
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT, 60)

if __name__ == "__main__":
    client.loop_start()

    while True:
        state = {"battery_level": 80, "error_code": 0, "speed": 1.2}
        publish_state(client, state)

        visualization = {"distance_from_last_node": 5, "last_node_ID": 2, "target_ID": 10}
        publish_visualization(client, visualization)

        connection = {"res_time": 20, "TTL": 60, "retry": 3}
        publish_connection(client, connection)

        time.sleep(1)
