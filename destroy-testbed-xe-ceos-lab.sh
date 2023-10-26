#!/bin/bash

echo 'Destroying containerlab topology with Cisco IOS XE CSR1000v and Arista cEOS routers ...'

sudo containerlab destroy --topo telemetry-testbed-xe-ceos.yaml

sudo rm .telemetry-testbed-xe-ceos.yaml.bak
sudo rm -Rf clab-telemetry-testbed-xe-ceos/

echo 'Done!'

echo ''
echo ''

echo 'All done!'
