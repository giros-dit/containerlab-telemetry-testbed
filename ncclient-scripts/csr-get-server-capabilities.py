import sys
import subprocess
from ncclient import manager

if len(sys.argv) < 2:
    print("Error - Incorrect arguments")
    print('Usage: python3 csr-get-server-capabilities.py <container_name>')
    print('Example: python3 csr-get-server-capabilities.py clab-telemetry-testbed-r1')
    exit(1)
else:
    container_name = sys.argv[1]
    check_container = subprocess.getoutput("docker ps -a | awk '{print $NF}' | grep " + container_name)

if check_container != container_name:
    print("Error - Incorrect arguments: You need to specify the container name of the network device.")
    print('Usage: python3 csr-get-server-capabilities.py <container_name>')
    print('Example: python3 csr-get-server-capabilities.py clab-telemetry-testbed-r1')
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

# Get the NETCONF server capabilities
for item in session.server_capabilities:
    print(item)

session.close_session()