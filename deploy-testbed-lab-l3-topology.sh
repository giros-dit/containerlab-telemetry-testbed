#!/bin/bash

echo 'Deploying containerlab L3 topology with Cisco IOS XE CSR1000v routers and Arista cEOS switches ...'

sudo containerlab deploy --topo telemetry-testbed-l3-topology.yaml

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc11" container...'

sudo docker exec -it clab-telemetry-testbed-l3-topology-pc11 ifconfig eth1 192.168.1.100 netmask 255.255.255.0
#sudo docker exec -it clab-telemetry-testbed-l3-topology-pc11 ip route add default via 192.168.1.1
sudo docker exec -it clab-telemetry-testbed-l3-topology-pc11 ip route add 192.168.2.0/24 via 192.168.1.1 dev eth1
sudo docker exec -it clab-telemetry-testbed-l3-topology-pc11 ip route add 192.168.3.0/24 via 192.168.1.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc12" container...'

sudo docker exec -it clab-telemetry-testbed-l3-topology-pc12 ifconfig eth1 192.168.1.101 netmask 255.255.255.0
#sudo docker exec -it clab-telemetry-testbed-l3-topology-pc12 ip route add default via 192.168.1.1
sudo docker exec -it clab-telemetry-testbed-l3-topology-pc12 ip route add 192.168.2.0/24 via 192.168.1.1 dev eth1
sudo docker exec -it clab-telemetry-testbed-l3-topology-pc12 ip route add 192.168.3.0/24 via 192.168.1.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc21" container...'

sudo docker exec -it clab-telemetry-testbed-l3-topology-pc21 ifconfig eth1 192.168.2.100 netmask 255.255.255.0
#sudo docker exec -it clab-telemetry-testbed-l3-topology-pc21 ip route add default via 192.168.2.1
sudo docker exec -it clab-telemetry-testbed-l3-topology-pc21 ip route add 192.168.1.0/24 via 192.168.2.1 dev eth1
sudo docker exec -it clab-telemetry-testbed-l3-topology-pc21 ip route add 192.168.3.0/24 via 192.168.2.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc22" container...'

sudo docker exec -it clab-telemetry-testbed-l3-topology-pc22 ifconfig eth1 192.168.2.101 netmask 255.255.255.0
#sudo docker exec -it clab-telemetry-testbed-l3-topology-pc22 ip route add default via 192.168.2.1
sudo docker exec -it clab-telemetry-testbed-l3-topology-pc22 ip route add 192.168.1.0/24 via 192.168.2.1 dev eth1
sudo docker exec -it clab-telemetry-testbed-l3-topology-pc22 ip route add 192.168.3.0/24 via 192.168.2.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc31" container...'

sudo docker exec -it clab-telemetry-testbed-l3-topology-pc31 ifconfig eth1 192.168.3.100 netmask 255.255.255.0
#sudo docker exec -it clab-telemetry-testbed-l3-topology-pc31 ip route add default via 192.168.3.1
sudo docker exec -it clab-telemetry-testbed-l3-topology-pc31 ip route add 192.168.1.0/24 via 192.168.3.1 dev eth1
sudo docker exec -it clab-telemetry-testbed-l3-topology-pc31 ip route add 192.168.2.0/24 via 192.168.3.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc32" container...'

sudo docker exec -it clab-telemetry-testbed-l3-topology-pc32 ifconfig eth1 192.168.3.101 netmask 255.255.255.0
#sudo docker exec -it clab-telemetry-testbed-l3-topology-pc32 ip route add default via 192.168.3.1
sudo docker exec -it clab-telemetry-testbed-l3-topology-pc32 ip route add 192.168.1.0/24 via 192.168.3.1 dev eth1
sudo docker exec -it clab-telemetry-testbed-l3-topology-pc32 ip route add 192.168.2.0/24 via 192.168.3.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'All done!'
