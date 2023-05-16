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
sta33 = net.addStation('sta33', ip='192.168.0.33/24', position='96, 47, 0')
sta34 = net.addStation('sta34', ip='192.168.0.34/24', position='12, 14, 0')
sta35 = net.addStation('sta35', ip='192.168.0.35/24', position='97, 59, 0')
sta36 = net.addStation('sta36', ip='192.168.0.36/24', position='55, 21, 0')
sta37 = net.addStation('sta37', ip='192.168.0.37/24', position='28, 49, 0')
sta38 = net.addStation('sta38', ip='192.168.0.38/24', position='66, 76, 0')
sta39 = net.addStation('sta39', ip='192.168.0.39/24', position='39, 24, 0')
sta40 = net.addStation('sta40', ip='192.168.0.40/24', position='13, 91, 0')
sta41 = net.addStation('sta41', ip='192.168.0.41/24', position='25, 22, 0')
sta42 = net.addStation('sta42', ip='192.168.0.42/24', position='30, 92, 0')
sta43 = net.addStation('sta43', ip='192.168.0.43/24', position='41, 7, 0')
sta44 = net.addStation('sta44', ip='192.168.0.44/24', position='94, 26, 0')
sta45 = net.addStation('sta45', ip='192.168.0.45/24', position='72, 8, 0')
sta46 = net.addStation('sta46', ip='192.168.0.46/24', position='20, 87, 0')
sta47 = net.addStation('sta47', ip='192.168.0.47/24', position='87, 4, 0')
sta48 = net.addStation('sta48', ip='192.168.0.48/24', position='3, 63, 0')
sta49 = net.addStation('sta49', ip='192.168.0.49/24', position='39, 12, 0')
sta50 = net.addStation('sta50', ip='192.168.0.50/24', position='79, 43, 0')
sta51 = net.addStation('sta51', ip='192.168.0.51/24', position='70, 27, 0')
sta52 = net.addStation('sta52', ip='192.168.0.52/24', position='70, 85, 0')
sta53 = net.addStation('sta53', ip='192.168.0.53/24', position='15, 35, 0')
sta54 = net.addStation('sta54', ip='192.168.0.54/24', position='97, 45, 0')
sta55 = net.addStation('sta55', ip='192.168.0.55/24', position='12, 58, 0')
sta56 = net.addStation('sta56', ip='192.168.0.56/24', position='36, 84, 0')
sta57 = net.addStation('sta57', ip='192.168.0.57/24', position='59, 39, 0')
sta58 = net.addStation('sta58', ip='192.168.0.58/24', position='6, 88, 0')
sta59 = net.addStation('sta59', ip='192.168.0.59/24', position='45, 21, 0')
sta60 = net.addStation('sta60', ip='192.168.0.60/24', position='15, 88, 0')
sta61 = net.addStation('sta61', ip='192.168.0.61/24', position='52, 87, 0')
sta62 = net.addStation('sta62', ip='192.168.0.62/24', position='38, 4, 0')
sta63 = net.addStation('sta63', ip='192.168.0.63/24', position='45, 4, 0')
sta64 = net.addStation('sta64', ip='192.168.0.64/24', position='81, 33, 0')



aps = []
for i in range(8):
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
net.addLink(sta33, aps[4])
net.addLink(sta34, aps[4])
net.addLink(sta35, aps[4])
net.addLink(sta36, aps[4])
net.addLink(sta37, aps[4])
net.addLink(sta38, aps[4])
net.addLink(sta39, aps[4])
net.addLink(sta40, aps[4])
net.addLink(sta41, aps[5])
net.addLink(sta42, aps[5])
net.addLink(sta43, aps[5])
net.addLink(sta44, aps[5])
net.addLink(sta45, aps[5])
net.addLink(sta46, aps[5])
net.addLink(sta47, aps[5])
net.addLink(sta48, aps[5])
net.addLink(sta49, aps[6])
net.addLink(sta50, aps[6])
net.addLink(sta51, aps[6])
net.addLink(sta52, aps[6])
net.addLink(sta53, aps[6])
net.addLink(sta54, aps[6])
net.addLink(sta55, aps[6])
net.addLink(sta56, aps[6])
net.addLink(sta57, aps[7])
net.addLink(sta58, aps[7])
net.addLink(sta59, aps[7])
net.addLink(sta60, aps[7])
net.addLink(sta61, aps[7])
net.addLink(sta62, aps[7])
net.addLink(sta63, aps[7])
net.addLink(sta64, aps[7])


print("Building network")
net.build()
c0 = net.addController('c0', controller=Controller)
aps[0].start([c0])
aps[1].start([c0])
aps[2].start([c0])
aps[3].start([c0])
aps[4].start([c0])
aps[5].start([c0])
aps[6].start([c0])
aps[7].start([c0])


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
sta_ap5 = [sta33, sta34, sta35, sta36, sta37, sta38, sta39, sta40]
sta_ap6 = [sta41, sta42, sta43, sta44, sta45, sta46, sta47, sta48]
sta_ap7 = [sta49, sta50, sta51, sta52, sta53, sta54, sta55, sta56]




for i in range(100): # time
    for sta in net.stations:
        #ap = [ap for ap in aps if sta in ap.associatedStations()][0]
        if sta in sta_ap1: #sta==sta1:
          ap_ins = aps[0]
        elif sta in sta_ap2:
          ap_ins = aps[1]
        elif sta in sta_ap3:
          ap_ins = aps[2]
        elif sta in sta_ap4:
          ap_ins = aps[3]
        elif sta in sta_ap5:
          ap_ins = aps[4]
        elif sta in sta_ap6:
          ap_ins = aps[5]
        elif sta in sta_ap7:
          ap_ins = aps[6]
        else:
          ap_ins = aps[7]
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
