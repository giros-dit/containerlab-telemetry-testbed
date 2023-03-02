#!/bin/bash

echo 'Destroying containerlab topology...'

sudo containerlab destroy --topo telemetry-testbed.yaml

echo 'Done!'

echo ''
echo ''

echo 'All done!'
