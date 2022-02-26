from mininet.topo import Topo

class MyTopo( Topo ):
    "Simple topology example."

    def build( self ):
        "Create custom topo."

        AM = [[0, 1, 1, 0], [1, 0, 1, 1], [1, 1, 0, 1], [0, 1, 1, 0]]
        numOfSwitches = 4
        numOfHosts = 2

        # Adding Controllers
        #c0 = self.addController('c0', controller=RemoteController, ip="127.0.0.1", port=6633)

        # adding Switches
        switches = []
        for i in range(numOfSwitches):
            switches.append(self.addSwitch('s' + str(i), failMode='secure', protocols='OpenFlow13'))

        # adding hosts
        # adding hosts to the switches
        hosts = []
        for i in range(numOfSwitches):
            for j in range(numOfHosts):
                hosts.append(self.addHost('h' + str(j + i * numOfHosts)))
                self.addLink(hosts[j + i * numOfHosts], switches[i])

        # adding switches links
        for i in range(numOfSwitches):
            for j in range(numOfSwitches):
                if AM[i][j] == 1:
                    self.addLink(switches[i], switches[j])


topos = { 'mytopo': ( lambda: MyTopo() ) }