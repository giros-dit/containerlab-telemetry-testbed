import sys
import subprocess
from ncclient import manager

if len(sys.argv) < 2:
    print("Error - Incorrect arguments")
    print('Usage: python3 csr-create-query-get-hostname.py <container_name>')
    print('Example: python3 csr-create-query-get-hostname.py clab-telemetry-testbed-r1')
    exit(1)
else:
    container_name = sys.argv[1]
    check_container = subprocess.getoutput("docker ps -a | awk '{print $NF}' | grep " + container_name)

if check_container != container_name:
    print("Error - Incorrect arguments: You need to specify the container name of the network device.")
    print('Usage: python3 csr-create-query-get-hostname.py <container_name>')
    print('Example: python3 csr-create-query-get-hostname.py clab-telemetry-testbed-r1')
    exit(1)

r = {
    "host": container_name,
    "port": 830,
    "username": "admin",
    "password": "admin",
    "hostkey_verify": False,
    "device_params": {"name": "csr"}
}

session = manager.connect(**r)

print ("\nSession ID: ", session.session_id)

# Create a configuration filter
hostname_filter = """
<native
	xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
	<hostname></hostname>
</native>
"""

# Execute the get RPC
reply = session.get(filter=("subtree", hostname_filter))

print("\nHostname of network device "+ container_name + ": \n")

print(reply)

session.close_session()