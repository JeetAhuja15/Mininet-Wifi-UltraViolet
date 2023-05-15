import time
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
sta3 = net.addStation('sta3', position='10,30,0', ip='192.168.0.3/24')
sta4 = net.addStation('sta4', position='30,10,0', ip='192.168.0.4/24')
sta5 = net.addStation('sta5', position='80,80,0', ip='192.168.0.5/24')
sta6 = net.addStation('sta6', position='20,45,0', ip='192.168.0.6/24')
sta7 = net.addStation('sta7', position='45,30,0', ip='192.168.0.7/24')
sta8 = net.addStation('sta8', position='60,70,0', ip='192.168.0.8/24')
sta9 = net.addStation('sta9', position='20,15,0', ip='192.168.0.9/24')
sta10 = net.addStation('sta10', position='95,57,0', ip='192.168.0.10/24')
sta11 = net.addStation('sta11', position='70,20,0', ip='192.168.0.11/24')
sta12 = net.addStation('sta12', position='30,25,0', ip='192.168.0.12/24')
sta13 = net.addStation('sta13', position='15,15,0', ip='192.168.0.13/24')
sta14 = net.addStation('sta14', position='20,65,0', ip='192.168.0.14/24')
sta15 = net.addStation('sta15', position='45,85,0', ip='192.168.0.15/24')
sta16 = net.addStation('sta16', position='10,50,0', ip='192.168.0.16/24')
sta17 = net.addStation('sta17', position='90,90,0', ip='192.168.0.17/24')
sta18 = net.addStation('sta18', position='95,95,0', ip='192.168.0.18/24')
sta19 = net.addStation('sta19', position='100,100,0', ip='192.168.0.19/24')
sta20 = net.addStation('sta20', position='105,105,0', ip='192.168.0.20/24')
sta21 = net.addStation('sta21', position='110,110,0', ip='192.168.0.21/24')
sta22 = net.addStation('sta22', position='115,115,0', ip='192.168.0.22/24')
sta23 = net.addStation('sta23', position='120,120,0', ip='192.168.0.23/24')
sta24 = net.addStation('sta24', position='125,125,0', ip='192.168.0.24/24')
sta25 = net.addStation('sta25', position='130,130,0', ip='192.168.0.25/24')
sta26 = net.addStation('sta26', position='135,135,0', ip='192.168.0.26/24')
sta27 = net.addStation('sta27', position='140,140,0', ip='192.168.0.27/24')
sta28 = net.addStation('sta28', position='145,145,0', ip='192.168.0.28/24')
sta29 = net.addStation('sta29', position='150,150,0', ip='192.168.0.29/24')
sta30 = net.addStation('sta30', position='155,155,0', ip='192.168.0.30/24')
sta31 = net.addStation('sta31', position='160,160,0', ip='192.168.0.31/24')
sta32 = net.addStation('sta32', position='165,165,0', ip='192.168.0.32/24')

aps = []
for i in range(4):
    ap = net.addAccessPoint('ap%s' % (i+1), position='%s,50,0' % ((i+1)*50), mode='g', channel='1', ssid='ssid-ap%s' % (i+1))
    aps.append(ap)

print("Configuring nodes")
net.configureWifiNodes()

print("Creating links")
net.addLink(sta1, aps[0])
net.addLink(sta2, aps[0])
net.addLink(sta3, aps[0])
net.addLink(sta4, aps[0])
net.addLink(sta5, aps[0])
net.addLink(sta6, aps[0])
net.addLink(sta7, aps[0])
net.addLink(sta8, aps[0])
net.addLink(sta9, aps[1])
net.addLink(sta10, aps[1])
net.addLink(sta11, aps[1])
net.addLink(sta12, aps[1])
net.addLink(sta13, aps[1])
net.addLink(sta14, aps[1])
net.addLink(sta15, aps[1])
net.addLink(sta16, aps[1])
net.addLink(sta17, aps[2])
net.addLink(sta18, aps[2])
net.addLink(sta19, aps[2])
net.addLink(sta20, aps[2])
net.addLink(sta21, aps[2])
net.addLink(sta22, aps[2])
net.addLink(sta23, aps[2])
net.addLink(sta24, aps[2])
net.addLink(sta25, aps[3])
net.addLink(sta26, aps[3])
net.addLink(sta27, aps[3])
net.addLink(sta28, aps[3])
net.addLink(sta29, aps[3])
net.addLink(sta30, aps[3])
net.addLink(sta31, aps[3])
net.addLink(sta32, aps[3])

print("Building network")
net.build()
c0 = net.addController('c0', controller=Controller)
aps[0].start([c0])
aps[1].start([c0])
aps[2].start([c0])
aps[3].start([c0])

print("Introducing mobility")
net.setMobilityModel(time=0, model='RandomDirection', max_x=100, max_y=100, seed=20, ac_method='ssf')
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

print("Logging BW")
log_file = open('bandwidth.log', 'w+')
count = 0
sta_ap1 = [sta1, sta2, sta3, sta4, sta5, sta6, sta7, sta8]
sta_ap2 = [sta9, sta10, sta11, sta12, sta13, sta14, sta15, sta16]
sta_ap3 = [sta17, sta18, sta19, sta20, sta21, sta22, sta23, sta24]
sta_ap4 = [sta25, sta26, sta27, sta28, sta29, sta30, sta31, sta32]

for i in range(100): # time
    for sta in net.stations:
        #ap = [ap for ap in aps if sta in ap.associatedStations()][0]
        if sta in sta_ap1: #sta==sta1:
            ap_ins = aps[0]
        else:
            ap_ins = aps[1]
        result = sta.cmd('iperf -c %s -t 1' % ap_ins.IP())
        lines = result.split('\n')
        for line in lines:
            if 'Gbits/sec' in line:
                parts = line.split()
                bandwidth = parts[7]
                log_line = '%s: %s\n' % (sta,bandwidth)
                file_line = '%s, ' % (bandwidth)
                count = count + 1
                if count % 2 != 0:
                    client.publish("mnWifi", log_line)
                    if sta==sta1: #sta1' in log_line:
                        log_file.write(file_line)
                    print(log_line)

print("Stopping network")
net.stop()
