#!/bin/bash

echo 'Destroying containerlab topology with Cisco IOS XE CSR1000v routers ...'

sudo containerlab destroy --topo telemetry-testbed.yaml

echo 'Done!'

echo ''
echo ''

echo 'All done!'
