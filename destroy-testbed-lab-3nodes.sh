#!/bin/bash

echo 'Destroying containerlab topology with Cisco IOS XE CSR1000v routers (3 router nodes)...'

sudo containerlab destroy --topo telemetry-testbed-3nodes.yaml

sudo rm .telemetry-testbed-3nodes.yaml.bak
sudo rm -Rf clab-telemetry-testbed-3nodes/

echo 'Done!'

echo ''
echo ''

echo 'All done!'
