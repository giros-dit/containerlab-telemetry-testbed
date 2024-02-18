#!/bin/bash

echo 'Deploying containerlab topology with Cisco IOS XE CSR1000v routers and Keysight Ixia-C traffic generator...'

sudo containerlab deploy --topo telemetry-ixiac-lab-old.yaml

echo 'Done!'

echo ''
echo ''

echo 'All done!'
