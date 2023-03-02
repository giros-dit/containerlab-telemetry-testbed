# ContainerLab testbed for studying and analyzing telemetry services over NETCONF/YANG

## Prerequisites:
- Docker: https://docs.docker.com/engine/install/
- ContainerLab: https://containerlab.dev/install/
- A CISCO IOS XE qcow2 image for CSR 1000v devices must be converted and imported so it can be used with ContainerLab: https://github.com/hellt/vrnetlab/tree/master/csr

### Building custom Docker image for Linux clients

```
$ cd docker/
$ sudo docker build -t girosdit/clab-telemetry-testbed-ubuntu:latest .
```

## Topology

![](https://github.com/giros-dit/containerlab-telemetry-testbed/blob/main/img/topology.png)

## Deploying and destroying the topology

### Deploying the topology

To deploy the topology, simply run the deploy shell script:

```
$ ./deploy.sh
```

### Interacting with containers

For **CSR routers**, via SSH to open the CISCO CLI (password is `admin`):
```
$ ssh admin@clab-telemetry-testbed-r1 # For r1 router

(or)

$ ssh admin@clab-telemetry-testbed-r2 # For r2 router
```

or with `docker exec` to open an interactive `bash` Linux shell:
```
$ sudo docker exec -it clab-telemetry-testbed-r1 bash # For r1 router

(or)

$ sudo docker exec -it clab-telemetry-testbed-r2 bash # For r2 router
```

For **Linux containers (clients)**, with `docker exec` to open an interactive shell:
```
$ sudo docker exec -it clab-telemetry-testbed-c1 /bin/sh # For c1 client container

(or)

$ sudo docker exec -it clab-telemetry-testbed-c2 /bin/sh # For c2 client container
```

### Destroying the topology

To destroy the topology, simply run the destroy shell script:

```
$ ./destroy.sh
```

## More

### ContainerLab documentation

- VM-based routers integration: https://containerlab.dev/manual/vrnetlab/
- Linux containers: https://containerlab.dev/manual/kinds/linux/
- Usage with Keysight IXIA-C traffic generator: https://containerlab.dev/lab-examples/ixiacone-srl/

### CISCO YANG Suite

Web-based GUI and set of tools to perform NETCONF/RESTCONF/gNMI/gRPC operations supported over YANG modules.

- Official GitHub repository with installation instructions: https://github.com/CiscoDevNet/yangsuite
- Official documentation: https://developer.cisco.com/docs/yangsuite/

### Related and interesting RFCs

- RFC 8641: Subscription to YANG Notifications for Datastore Updates: https://datatracker.ietf.org/doc/html/rfc8641
- RFC 9196: YANG Modules Describing Capabilities for Systems and Datastore Update Notifications: https://datatracker.ietf.org/doc/html/rfc9196

### Related and interesting links with additional information

- CISCO IOS XE Model Driven Telemetry (for version 17.3.X): https://www.cisco.com/c/en/us/td/docs/ios-xml/ios/prog/configuration/173/b_173_programmability_cg/model_driven_telemetry.html
- ContainerLab: CISCO CSRs in containers?!: https://devnetdan.com/2021/12/15/containerlab-cisco-csrs-in-containers/
- Cisco CSR 1000v and Cisco ISRv Software Configuration Guide: https://www.cisco.com/c/en/us/td/docs/routers/csr1000/software/configuration/b_CSR1000v_Configuration_Guide.pdf
- How to Configure a Cisco CSR device using NETCONF/YANG: https://www.fir3net.com/Networking/Concepts-and-Terminology/how-to-configure-a-cisco-csr-using-netconf-yang.html
- ncclient documentation: https://ncclient.readthedocs.io/en/latest/
- YANG Models GitHub repository: https://github.com/YangModels/yang
- YANG Catalog Search: https://yangcatalog.org/yang-search
- Andrés Ripoll's TFG GitHub repository: https://github.com/andresripoll/TFG_NETCONF
- NETCONF Telemetry PoC: https://github.com/giros-dit/netconf-telemetry-poc
