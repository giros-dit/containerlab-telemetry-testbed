#!/bin/bash

echo 'Deploying containerlab topology with Cisco IOS XE CSR1000v routers (3 nodes) ...'

sudo containerlab deploy --topo telemetry-testbed-3nodes.yaml

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc1" container...'

sudo docker exec -it clab-telemetry-testbed-3nodes-pc1 ifconfig eth1 192.168.1.100 netmask 255.255.255.0
sudo docker exec -it clab-telemetry-testbed-3nodes-pc1 ip route add 192.168.2.0/24 via 192.168.1.1 dev eth1
sudo docker exec -it clab-telemetry-testbed-3nodes-pc1 ip route add 192.168.3.0/24 via 192.168.1.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc2" container...'

sudo docker exec -it clab-telemetry-testbed-3nodes-pc2 ifconfig eth1 192.168.2.100 netmask 255.255.255.0
sudo docker exec -it clab-telemetry-testbed-3nodes-pc2 ip route add 192.168.1.0/24 via 192.168.2.1 dev eth1
sudo docker exec -it clab-telemetry-testbed-3nodes-pc2 ip route add 192.168.3.0/24 via 192.168.2.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc3" container...'

sudo docker exec -it clab-telemetry-testbed-3nodes-pc3 ifconfig eth1 192.168.3.100 netmask 255.255.255.0
sudo docker exec -it clab-telemetry-testbed-3nodes-pc3 ip route add 192.168.1.0/24 via 192.168.3.1 dev eth1
sudo docker exec -it clab-telemetry-testbed-3nodes-pc3 ip route add 192.168.2.0/24 via 192.168.3.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'All done!'
