import os
import time
import paho.mqtt.client as mqtt
from Experiments_jeet import runNetworkDynamism

def on_message(client, userdata, message):
    print("hehe")
    """
    if 'sta1' in str(message.payload.decode("utf-8")):
        msg = str(message.payload.decode("utf-8"))
        edge_ins = 'Edge-1.1'
        print(msg[1], type(msg[1]))
        bw_ins = int(float(msg[1]))
        
        lat_ins = 30 #random value set
        #runNetworkDynamism.dummy.tmp.updateLinkParams(edge_ins, 0, bw=bw_ins/1000, delay=str(lat_ins) + "ms")
        exp = runNetworkDynamism.tmp
        exp.updateLinkParams(edge_ins, 0, bw=bw_ins, delay=str(lat_ins) + "ms")
        print("msg recieved" )
    """
    if 'sta1' in str(message.payload.decode("utf-8")):
        msg = str(message.payload.decode("utf-8")).split()
        print(msg[1], type(msg[1]))
        edge_ins = 'Edge-1.1'
        bw_ins = int(float(msg[1]))
        lat_ins = 30
        exp = runNetworkDynamism.tmp
        exp.updateLinkParams(edge_ins, 0, bw=bw_ins, delay=str(lat_ins) + "ms")
        #print("msg recieved" )

def run_network_dynamism():
    mqttBroker = "mqtt.eclipseprojects.io"

    client = mqtt.Client("netDyn")
    client.connect(mqttBroker)

    client.loop_start()

    client.subscribe("mnWifi")
    client.on_message = on_message

    time.sleep(200)
    client.loop_stop()
