#!/bin/bash

echo 'Getting the MAC addresses of the incoming interface of routers r1 and r2 ...'

echo ''

echo 'Establishing SSH connection to r1 ...'

./discover_target_mac_r1.sh

echo 'Done!'

echo ''
echo ''

echo 'Establishing SSH connection to r2 ...'

./discover_target_mac_r2.sh

echo 'Done!'

echo ''
echo ''

echo 'All done!'
