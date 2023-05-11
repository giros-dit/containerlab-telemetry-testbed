#!/bin/bash

echo 'Destroying containerlab topology with Cisco IOS XE CSR1000v routers ...'

sudo containerlab destroy --topo telemetry-testbed.yaml

sudo rm .telemetry-testbed.yaml.bak
sudo rm -Rf clab-telemetry-testbed/

echo 'Done!'

echo ''
echo ''

echo 'All done!'
