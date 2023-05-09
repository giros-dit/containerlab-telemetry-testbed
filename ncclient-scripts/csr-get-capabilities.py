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

# Extract the NETCONF server capabilities
capabilities = session.server_capabilities

"""
# Get the NETCONF server capabilities in raw format
for item in session.server_capabilities:
    print(item)
"""

"""
Retrieve the set of YANG modules supported by the network device. For each YANG module we obtain the name, 
the revision/version, and the namespace URI. In addition, certain YANG modules include additional 
implementation details, such as additional features and deviations.
"""
print("\n - YANG modules supported by the network device "+ container_name + ": \n")
for capability_key in capabilities:
    capability = capabilities[capability_key]
    if "module" in capability.parameters:
        capability.parameters['namespace_uri'] = capability.namespace_uri
        print(capability.parameters) 
        print("")

"""
Retrieve the set of NETCONF server capabilities supported by the network device, such as XPath filtering 
support in RPC operations (e.g., `urn:ietf:params:netconf:capability:xpath:1.0`) and the capability to 
send notifications to subscribers (e.g., `urn:ietf:params:netconf:capability:notification:1.0`). 
Each NETCONF server capability is identified by its particular namespace URI.
"""        
print("\n - NETCONF server capabilities supported by the network device "+ container_name + ": \n")
for capability_key in capabilities:
    capability = capabilities[capability_key]
    if not "module" in capability.parameters:
        if capability.namespace_uri:
           print(capability.namespace_uri.replace("\n", "").replace(" ",""))
           print("")

session.close_session()