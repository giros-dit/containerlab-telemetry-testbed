#!/bin/bash

echo 'Destroying containerlab topology with Nokia SR Linux routers and Arista cEOS switches...'

sudo containerlab destroy --topo routing-testbed-ceos-and-srlinux.yaml
sudo rm -Rf clab-routing-testbed-ceos-and-srlinux/

echo 'Done!'

echo ''
echo ''

echo 'All done!'
