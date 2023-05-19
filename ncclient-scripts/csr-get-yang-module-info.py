import sys
import subprocess
from ncclient import manager

if len(sys.argv) < 3:
    print("Error - Incorrect arguments")
    print('Usage: python3 csr-get-yang-module-info.py <container_name> <yang_module_name>')
    print('Example: python3 csr-get-yang-module-info.py clab-telemetry-testbed-r1 ietf-interfaces')
    exit(1)
else:
    container_name = sys.argv[1]
    yang_module_name = sys.argv[2]
    check_container = subprocess.getoutput("docker ps -a | awk '{print $NF}' | grep " + container_name)

if check_container != container_name:
    print("Error - Incorrect arguments: You need to specify the container name of the network device.")
    print('Usage: python3 csr-get-yang-module-info.py <container_name>')
    print('Example: python3 csr-get-yang-module-info.py clab-telemetry-testbed-r1 ietf-interfaces')
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

# Extract the NETCONF capabilities
capabilities = session.server_capabilities

yang_module_supported = False 

"""
Retrieve the set of YANG modules supported by the network device and get only the information about the 
requested YANG module. For the requested YANG module we obtain the name, the revision/version, and the namespace URI. 
In addition, the requested YANG module may include additional implementation details, such as additional features and deviations.
"""
for capability_key in capabilities:
    capability = capabilities[capability_key]
    if "module" in capability.parameters:
        if capability.parameters['module'] == yang_module_name:
            capability.parameters['namespace_uri'] = capability.namespace_uri
            print("\nInformation about the requested YANG module " + str(yang_module_name) + " supported by the network device "+ container_name + ": " + str(capability.parameters)) 
            print("")
            yang_module_supported = True
            break

if yang_module_supported == False:
    print("\nThe requested YANG module " + str(yang_module_name) + " is not supported by the network device "+ container_name + ".") 

session.close_session()