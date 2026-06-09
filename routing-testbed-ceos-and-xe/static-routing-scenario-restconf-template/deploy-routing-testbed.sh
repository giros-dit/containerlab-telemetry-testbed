#!/bin/bash

echo 'Deploying containerlab topology with Cisco IOS XE CSR1000v and Arista cEOS routers...'

sudo ovs-vsctl add-br s1
sudo ovs-vsctl add-br s2
sudo ovs-vsctl add-br s3
sudo containerlab deploy --topo routing-testbed.yaml

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc11" container...'

sudo docker exec -it clab-routing-testbed-pc11 ifconfig eth1 192.168.1.100 netmask 255.255.255.0
sudo docker exec -it clab-routing-testbed-pc11 ip route add 192.168.2.0/24 via 192.168.1.1 dev eth1
sudo docker exec -it clab-routing-testbed-pc11 ip route add 192.168.3.0/24 via 192.168.1.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc12" container...'

sudo docker exec -it clab-routing-testbed-pc12 ifconfig eth1 192.168.1.101 netmask 255.255.255.0
sudo docker exec -it clab-routing-testbed-pc12 ip route add 192.168.2.0/24 via 192.168.1.1 dev eth1
sudo docker exec -it clab-routing-testbed-pc12 ip route add 192.168.3.0/24 via 192.168.1.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc21" container...'

sudo docker exec -it clab-routing-testbed-pc21 ifconfig eth1 192.168.2.100 netmask 255.255.255.0
sudo docker exec -it clab-routing-testbed-pc21 ip route add 192.168.1.0/24 via 192.168.2.1 dev eth1
sudo docker exec -it clab-routing-testbed-pc21 ip route add 192.168.3.0/24 via 192.168.2.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc22" container...'

sudo docker exec -it clab-routing-testbed-pc22 ifconfig eth1 192.168.2.101 netmask 255.255.255.0
sudo docker exec -it clab-routing-testbed-pc22 ip route add 192.168.1.0/24 via 192.168.2.1 dev eth1
sudo docker exec -it clab-routing-testbed-pc22 ip route add 192.168.3.0/24 via 192.168.2.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc31" container...'

sudo docker exec -it clab-routing-testbed-pc31 ifconfig eth1 192.168.3.100 netmask 255.255.255.0
sudo docker exec -it clab-routing-testbed-pc31 ip route add 192.168.1.0/24 via 192.168.3.1 dev eth1
sudo docker exec -it clab-routing-testbed-pc31 ip route add 192.168.2.0/24 via 192.168.3.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'Configuring client "pc32" container...'

sudo docker exec -it clab-routing-testbed-pc32 ifconfig eth1 192.168.3.101 netmask 255.255.255.0
sudo docker exec -it clab-routing-testbed-pc32 ip route add 192.168.1.0/24 via 192.168.3.1 dev eth1
sudo docker exec -it clab-routing-testbed-pc32 ip route add 192.168.2.0/24 via 192.168.3.1 dev eth1

echo 'Done!'

echo ''
echo ''

echo 'Configuring self-signed cert for RESTCONF management on router "r2" container...'
sleep 2
sudo docker exec -it clab-routing-testbed-r2 Cli -p 15 -c "security pki certificate generate self-signed restconf.crt key restconf.key generate rsa 2048 parameters common-name restconf"

echo 'Done!'

echo ''
echo ''

echo 'Configuring self-signed cert for RESTCONF management on router "r3" container...'
sleep 2
sudo docker exec -it clab-routing-testbed-r3 Cli -p 15 -c "security pki certificate generate self-signed restconf.crt key restconf.key generate rsa 2048 parameters common-name restconf"

echo 'Done!'

echo ''
echo ''

echo 'All done!'
