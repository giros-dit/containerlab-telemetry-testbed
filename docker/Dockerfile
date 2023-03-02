# Dockerfile to build a custom Ubuntu image to be used in the topology

# Base image is Ubuntu 20.04 LTS (bionic)
FROM ubuntu:bionic

# Preinstalled software and packages are updated
RUN apt-get update && apt-get -y dist-upgrade && apt-get -y autoremove && apt-get autoclean

# Other packages are installed
RUN apt-get install -y iproute2 net-tools ldnsutils traceroute iperf3 tcpdump openssh-server
