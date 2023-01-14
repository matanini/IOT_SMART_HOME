import paho.mqtt.client as mqtt

def on_log(client, userdata, level, buf):
    print("log: " + buf)


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("connected OK")
    else:
        print("Bad connection Returned code=", rc)


def on_disconnect(client, userdata, flags, rc=0):
    print("DisConnected result code " + str(rc))


def on_message(client, userdata, msg):
    topic = msg.topic
    m_decode = str(msg.payload.decode("utf-8", "ignore"))
    print("message received: ", m_decode)




class mqttClient(mqtt.Client):
    def __init__(
        self,
        client_id :str, 
        broker = "broker.hivemq.com",
        port = 1883,
        clean_session:bool = True,
        on_connect = on_connect,
        on_disconnect = on_disconnect,
        on_message = on_message,
        ):
        super().__init__(client_id, clean_session = clean_session)
        self.on_connect = on_connect  
        self.on_disconnect = on_disconnect
        self.on_log = on_log
        self.on_message = on_message
        self.connect(broker, port)
        print("connected succesfully")

    def send_data(self, data, topic = "VioTrackerLiveFeed"):
        self.publish(topic, str(data))
        
    def get_data(self, topic = "VioTrackerLiveFeed"):
        self.loop_start()
        self.subscribe(topic)
    
    def stop_receiving(self):
        self.stop_loop()
        self.disconnect()