#!/bin/bash

echo 'Destroying containerlab topology with Nokia SR Linux and Arista cEOS routers...'

sudo containerlab destroy --topo telemetry-testbed-srl-ceos.yaml

sudo rm .telemetry-testbed-srl-ceos.yaml.bak
sudo rm -Rf clab-telemetry-testbed-srl-ceos/

echo 'Done!'

echo ''
echo ''

echo 'All done!'
