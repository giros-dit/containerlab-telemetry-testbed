#!/bin/bash
echo 'Configuring IP addressing and static routing on Arista cEOS routers...'

#Configuring interface IP address on R1
echo '{"IF_NAME": "Ethernet2", "IF_IP": "10.10.10.1", "PREFIX": 30}' | \
gnmic -a clab-routing-testbed-r1:6030 -u admin -p admin --insecure \
set --request-file configure_ip_address.yaml --request-vars -

echo '{"IF_NAME": "Ethernet3", "IF_IP": "10.10.11.1", "PREFIX": 30}' | \
gnmic -a clab-routing-testbed-r1:6030 -u admin -p admin --insecure \
set --request-file configure_ip_address.yaml --request-vars -

#Configuring interface IP routing on R1
echo '{"PREFIX": "192.168.2.0/24", "NEXT_HOP": "10.10.10.2"}' | \
gnmic -a clab-routing-testbed-r1:6030 -u admin -p admin --insecure \
set --request-file configure_ip_routing.yaml --request-vars -

echo '{"PREFIX": "192.168.3.0/24", "NEXT_HOP": "10.10.11.2"}' | \
gnmic -a clab-routing-testbed-r1:6030 -u admin -p admin --insecure \
set --request-file configure_ip_routing.yaml --request-vars -

#Configuring interface IP address on R2
echo '{"IF_NAME": "Ethernet2", "IF_IP": "10.10.10.2", "PREFIX": 30}' | \
gnmic -a clab-routing-testbed-r2:6030 -u admin -p admin --insecure \
set --request-file configure_ip_address.yaml --request-vars -

echo '{"IF_NAME": "Ethernet3", "IF_IP": "10.10.12.1", "PREFIX": 30}' | \
gnmic -a clab-routing-testbed-r2:6030 -u admin -p admin --insecure \
set --request-file configure_ip_address.yaml --request-vars -

#Configuring interface IP routing on R2
echo '{"PREFIX": "192.168.1.0/24", "NEXT_HOP": "10.10.10.1"}' | \
gnmic -a clab-routing-testbed-r2:6030 -u admin -p admin --insecure \
set --request-file configure_ip_routing.yaml --request-vars -

echo '{"PREFIX": "192.168.3.0/24", "NEXT_HOP": "10.10.12.2"}' | \
gnmic -a clab-routing-testbed-r2:6030 -u admin -p admin --insecure \
set --request-file configure_ip_routing.yaml --request-vars -

#Configuring interface IP address on R3
echo '{"IF_NAME": "Ethernet2", "IF_IP": "10.10.11.2", "PREFIX": 30}' | \
gnmic -a clab-routing-testbed-r3:6030 -u admin -p admin --insecure \
set --request-file configure_ip_address.yaml --request-vars -

echo '{"IF_NAME": "Ethernet3", "IF_IP": "10.10.12.2", "PREFIX": 30}' | \
gnmic -a clab-routing-testbed-r3:6030 -u admin -p admin --insecure \
set --request-file configure_ip_address.yaml --request-vars -

#Configuring interface IP routing on R3
echo '{"PREFIX": "192.168.1.0/24", "NEXT_HOP": "10.10.11.1"}' | \
gnmic -a clab-routing-testbed-r3:6030 -u admin -p admin --insecure \
set --request-file configure_ip_routing.yaml --request-vars -

echo '{"PREFIX": "192.168.2.0/24", "NEXT_HOP": "10.10.12.1"}' | \
gnmic -a clab-routing-testbed-r3:6030 -u admin -p admin --insecure \
set --request-file configure_ip_routing.yaml --request-vars -