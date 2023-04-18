#!/bin/bash

mac=`ssh -l admin clab-telemetry-ixiac-lab-r1  "show interfaces GigabitEthernet2 | i (.* Hardware)" | awk '{print $7}' | tr -d '\n'` 
new_mac=""
position=0
let len=${#mac}-1

for (( pos=0; pos<=$len; pos++ ))
do
    if [[ ${mac:$pos:1} != "." ]]; then
        position=$((position+1))
        new_mac+="${mac:$pos:1}"
        let resto=$position%2

        if [ $resto -eq 0 ] && [ $pos -le $((len-1)) ]
        then
            new_mac+=":"
        fi
    fi
done
echo "Target MAC address of r1 = " $new_mac