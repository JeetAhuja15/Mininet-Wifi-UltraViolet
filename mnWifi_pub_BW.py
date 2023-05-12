mport time
import paho.mqtt.client as mqtt

from mn_wifi.node import OVSKernelAP
from mn_wifi.topo import Topo
from mn_wifi.net import Mininet_wifi
from mininet.node import Controller
from containernet.node import OVSSwitch

net = Mininet_wifi(controller=Controller, accessPoint=OVSKernelAP)

print("Adding Stations + APs")
sta1 = net.addStation('sta1', position='10,10,0', ip='192.168.0.1/24')
sta2 = net.addStation('sta2', position='90,90,0', ip='192.168.0.2/24')
ap1 = net.addAccessPoint('ap1', position='50,50,0', mode='g', channel='1', ssid='ssid-ap1')

print("Configuring nodes")
net.configureWifiNodes()

print("Building network")
net.build()
c0 = net.addController('c0', controller=Controller)
ap1.start([c0])

print("Introducing mobility")
net.setMobilityModel(time=0, model='RandomDirection', max_x=100, max_y=100, seed=20)
net.startMobility()

print("Installing iperf in all stations")
for sta in net.stations:
    sta.cmd('apt-get update')
    sta.cmd('apt-get install -y iperf')
print("Start iperf server in stations")
for sta in net.stations:
    sta.cmd('iperf -s &')

mqttBroker = "mqtt.eclipseprojects.io"
client = mqtt.Client("mnWifi")
client.connect(mqttBroker)

print("Loggin BW")
log_file = open('bandwidth.log', 'w+')
count = 0
for i in range(100): # time 
    for sta in net.stations:
        result = sta.cmd('iperf -c %s -t 1' % ap1.IP())
        lines = result.split('\n')
        for line in lines:
            if 'Gbits/sec' in line:
                #print(line)
                parts = line.split()
                bandwidth = parts[7]
                log_line = '%s: %s\n' % (sta,bandwidth)
                file_line = '%s, ' % (bandwidth)
                count = count + 1
                if count % 2 != 0:
                    client.publish("mnWifi", log_line)
                    if 'sta1' in log_line:
                        log_file.write(file_line)
                    print(log_line)

print("Stopping network")
net.stop()                                                                   
