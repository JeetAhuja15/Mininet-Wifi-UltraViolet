import time

from MaxiNet.Frontend import maxinet
from MaxiNet.Frontend.container import DockerSta
from mn_wifi.topo import Topo
from mn_wifi.net import Mininet_wifi
from mininet.node import Controller
from mn_wifi.node import OVSKernelAP
from containernet.node import OVSSwitch

topo = Topo()
net = Mininet_wifi(controller=Controller, accessPoint=OVSKernelAP)

print("Adding Stations and AP")
d1 = net.addStation("d1", cls=DockerSta, ip="192.168.0.1/24", dimage="ubuntu:trusty", position="10,10,0")
d2 = net.addStation("d2", cls=DockerSta, ip="192.168.0.2/24", dimage="ubuntu:trusty", position="90,90,0")
  
ap1 = net.addAccessPoint('ap1', position="50,50,0", channel='1', mode='g')

print("Configuring nodes")
net.configureWifiNodes()

#print("Setting mobility model")
#net.setMobilityModel(time=0, model='RandomDirection', max_x=100, max_y=100, seed=20)

#net.startMobility()

print("building network")
net.build()
c0 = net.addController('c0', controller=Controller)
ap1.start([c0])

print("Setting mobility model")
net.setMobilityModel(time=0, model='RandomDirection', max_x=100, max_y=100, seed=20)
net.startMobility()

"""
print("Integration with UV")
cluster = maxinet.Cluster()
exp = maxinet.Experiment(cluster, topo, switch=OVSSwitch)
exp.setup()

print("Getting node and executing cmd")
time.sleep(5)
print(exp.get_node("d1").cmd("ifconfig"))
"""

print("Retrieving BW and Lat")
for sta in net.stations:
    sta.cmd('apt-get update')
    sta.cmd('apt-get install -y iperf3')
    sta.cmd('iperf3 -s &')
for sta in net.stations:
    result = sta.cmd('iperf3 -c %s -t 10' % ap1.IP())
    print("Station %s: %s" %(sta, result))


print("Stopping network")
net.stop()
             
