#!/bin/bash

echo 'Destroying containerlab topology with Cisco IOS XE CSR1000v routers and Arista cEOS switches...'

sudo containerlab destroy --topo telemetry-testbed-l3-topology.yaml

sudo rm .telemetry-testbed-l3-topology.yaml.bak
sudo rm -Rf clab-telemetry-testbed-l3-topology/

echo 'Done!'

echo ''
echo ''

echo 'All done!'
