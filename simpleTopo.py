#!/usr/bin/python

from mininet.net import Mininet
from mininet.node import Controller, RemoteController,OVSKernelSwitch,OVSSwitch,Host
from mininet.cli import CLI
from mininet.log import setLogLevel, info
import mininet

def simpleTopo():

    net=Mininet(topo=None,listenPort=6633,build=False)
    info( '*** Adding controller\n' )
    c0=net.addController(name='c0' ,controller=RemoteController,protocol='tcp',port=6633)
    info( '*** Add switches\n')
    s1 = net.addSwitch('s1', cls=OVSKernelSwitch,failMode='secure')
    info( '*** Add hosts\n')
    h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
    h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
    info( '*** Add links\n')
    net.addLink(h1, s1)
    net.addLink(h2,s1)

    info( '*** Starting network\n')
    net.build()
    info( '*** Starting controllers\n')
    s1.start([c0])
    
    info( '*** Post configure switches and hosts\n')
    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel( 'info' )
    simpleTopo()



# def myNetwork():

#     net = Mininet( topo=None,
#                    listenPort=6633,
#                    build=False)

#     info( '*** Adding controller\n' )
#     info( '*** Add switches\n')
#     s1 = net.addSwitch('s1', cls=OVSKernelSwitch, failMode='secure')
#     s2 = net.addSwitch('s2', cls=OVSKernelSwitch, failMode='secure')
#     s3 = net.addSwitch('s3', cls=OVSKernelSwitch, failMode='secure')

#     info( '*** Add hosts\n')
#     h2 = net.addHost('h2', cls=Host, ip='10.0.0.2', defaultRoute=None)
#     h1 = net.addHost('h1', cls=Host, ip='10.0.0.1', defaultRoute=None)
#     h3 = net.addHost('h3', cls=Host, ip='10.0.0.3', defaultRoute=None)

#     info( '*** Add links\n')
#     net.addLink(h1, s1)
#     net.addLink(s1, s2)
#     net.addLink(s2, h2)
#     net.addLink(s2, s3)
#     net.addLink(s3, h3)
#     net.addLink(s3, s1)

#     info( '*** Starting network\n')
#     net.build()
#     info( '*** Starting controllers\n')
#     for controller in net.controllers:
#         controller.start()

#     info( '*** Starting switches\n')
#     net.get('s1').start([])
#     net.get('s2').start([])
#     net.get('s3').start([])

#     info( '*** Post configure switches and hosts\n')

#     CLI(net)
#     net.stop()

# if __name__ == '__main__':
#     setLogLevel( 'info' )
#     myNetwork()

# def myNet():


#     #OpenDayLight controller
#     ODL_CONTROLLER_IP='10.0.0.4'

#     #Floodlight controller
#     FL_CONTROLLER_IP='10.0.0.5'

#     net = Mininet( topo=None, build=False)

#     # Create nodes
#     h1 = net.addHost( 'h1', mac='01:00:00:00:01:00', ip='192.168.0.1/24' )
#     h2 = net.addHost( 'h2', mac='01:00:00:00:02:00', ip='192.168.0.2/24' )

#     # Create switches
#     s1 = net.addSwitch( 's1', listenPort=6634, mac='00:00:00:00:00:01' )
#     s2 = net.addSwitch( 's2', listenPort=6634, mac='00:00:00:00:00:02' )

#     print "*** Creating links"
#     net.addLink(h1, s1, )
#     net.addLink(h2, s2, )   
#     net.addLink(s1, s2, )  

#     # Add Controllers
#     odl_ctrl = net.addController( 'c0', controller=RemoteController, ip=ODL_CONTROLLER_IP, port=6633)

#     fl_ctrl = net.addController( 'c1', controller=RemoteController, ip=FL_CONTROLLER_IP, port=6633)


#     net.build()

#     # Connect each switch to a different controller
#     s1.start( [odl_ctrl] )
#     s2.start( [fl_ctrl] )

#     s1.cmdPrint('ovs-vsctl show')

#     CLI( net )
#     net.stop()

# if __name__ == '__main__':
#     setLogLevel( 'info' )
#     myNet()

