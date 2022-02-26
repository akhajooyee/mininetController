from mininet.net import Mininet
from mininet.topo import Topo
from mininet.log import setLogLevel
from mininet.cli import CLI
from mininet.node import RemoteController

#no loop
#AM[i][j] denotes the link between i and j
AM = [[0,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,0]]
numOfSwitches = 4
numOfHosts = 2

net = Mininet()

#Adding Controllers
c0 = net.addController()

#adding Switches
switches = []
for i in range(numOfSwitches):
    switches.append(net.addSwitch('s'+str(i)))

# adding hosts
#adding hosts to the switches
hosts = []
for i in range(numOfSwitches):
    for j in range(numOfHosts):
        hosts.append(net.addHost('h'+str(j+i*numOfHosts)))
        net.addLink(hosts[j+i*numOfHosts],switches[i])

#adding switches links
for i in range(numOfSwitches):
    for j in range(numOfSwitches):
        if AM[i][j] == 1:
            net.addLink(switches[i],switches[j])

net.start()
net.pingAll()
net.stop()


