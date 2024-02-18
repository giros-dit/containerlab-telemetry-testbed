#!/bin/bash

echo 'Destroying containerlab topology with Nokia SR Linux routers...'

sudo containerlab destroy --topo telemetry-testbed-srl-srl.yaml

sudo rm .telemetry-testbed-srl-srl.yaml.bak
sudo rm -Rf clab-telemetry-testbed-srl-srl/

echo 'Done!'

echo ''
echo ''

echo 'All done!'
