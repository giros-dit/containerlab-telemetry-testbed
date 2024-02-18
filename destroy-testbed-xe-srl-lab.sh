#!/bin/bash

echo 'Destroying containerlab topology with Cisco IOS XE CSR1000v and Nokia SR Linux routers...'

sudo containerlab destroy --topo telemetry-testbed-xe-srl.yaml

sudo rm .telemetry-testbed-xe-srl.yaml.bak
sudo rm -Rf clab-telemetry-testbed-xe-srl/

echo 'Done!'

echo ''
echo ''

echo 'All done!'
