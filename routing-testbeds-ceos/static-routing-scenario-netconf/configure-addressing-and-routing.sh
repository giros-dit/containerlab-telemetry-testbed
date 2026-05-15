#!/bin/bash
echo 'Configuring IP addressing and static routing on Arista cEOS routers...'
echo ''

#Configuring interface IP addresses on R1
python3.8 configure_ip_address.py clab-routing-testbed-r1 Ethernet2 10.10.10.1 30
python3.8 configure_ip_address.py clab-routing-testbed-r1 Ethernet3 10.10.11.1 30

#Configuring interface IP routing on R1
python3.8 configure_ip_routing.py clab-routing-testbed-r1 192.168.2.0/24 10.10.10.2
python3.8 configure_ip_routing.py clab-routing-testbed-r1 192.168.3.0/24 10.10.11.2

#Configuring interface IP addresses on R2
python3.8 configure_ip_address.py clab-routing-testbed-r2 Ethernet2 10.10.10.2 30
python3.8 configure_ip_address.py clab-routing-testbed-r2 Ethernet3 10.10.12.1 30

#Configuring interface IP routing on R2
python3.8 configure_ip_routing.py clab-routing-testbed-r2 192.168.1.0/24 10.10.10.1
python3.8 configure_ip_routing.py clab-routing-testbed-r2 192.168.3.0/24 10.10.12.2

#Configuring interface IP addresses on R3
python3.8 configure_ip_address.py clab-routing-testbed-r3 Ethernet2 10.10.11.2 30
python3.8 configure_ip_address.py clab-routing-testbed-r3 Ethernet3 10.10.12.2 30

#Configuring interface IP routing on R3
python3.8 configure_ip_routing.py clab-routing-testbed-r3 192.168.1.0/24 10.10.11.1
python3.8 configure_ip_routing.py clab-routing-testbed-r3 192.168.2.0/24 10.10.12.1