import os
import time
import paho.mqtt.client as mqtt
from Experiments_jeet import runNetworkDynamism

count = 0

def on_message(client, userdata, message):
    global count
    #print("hehe")
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
        print(msg[1], 'sta1')
        edge_ins = 'Edge-1.1'
        bw_ins = float(msg[1])
        lat_ins = 10
        fog = "Fog-1"
        bdp = (2 * int(bw_ins) * int(lat_ins) * 1000)
        exp = runNetworkDynamism.tmp

        og_node = exp.get_node(fog)
        edge_node = exp.get_node(edge_ins)
        fog_node.cmd(f"sysctl net.ipv4.tcp_rmem=\"{bdp // 2} {bdp} {int(2.04 * bdp)}\" && sysctl net.ipv4.tcp_wmem=\"{bdp // 2} {bdp} {int(2.04 * bdp)}\"")
        edge_node.cmd(f"sysctl net.ipv4.tcp_rmem=\"{bdp // 2} {bdp} {int(2.04 * bdp)}\" && sysctl net.ipv4.tcp_wmem=\"{bdp // 2} {bdp} {int(2.04 * bdp)}\"")
        count = count + 1
        if count % 5 == 0:
            exp.updateLinkParams(edge_ins, 0, bw=bw_ins, delay=str(lat_ins) + "ms")
        #print("msg recieved" )
    elif 'sta2' in str(message.payload.decode("utf-8")):
        msg = str(message.payload.decode("utf-8")).split()
        print(msg[1], 'sta2')
        edge_ins = 'Edge-2.1'
        bw_ins = int(float(msg[1]))
        lat_ins = 10
        fog = "Fog-2"
        exp = runNetworkDynamism.tmp
        exp.updateLinkParams(edge_ins, 0, bw=bw_ins, delay=str(lat_ins) + "ms")

def run_network_dynamism():
    mqttBroker = "mqtt.eclipseprojects.io"

    client = mqtt.Client("netDyn")
    client.connect(mqttBroker)

    client.loop_start()

    client.subscribe("mnWifi")
    client.on_message = on_message

    time.sleep(250)
    client.loop_stop()
                                                                                                                                                     65,1          Bot
