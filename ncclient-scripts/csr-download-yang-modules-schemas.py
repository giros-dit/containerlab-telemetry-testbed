import sys
import subprocess
from ncclient import manager

if len(sys.argv) < 2:
    print("Error - Incorrect arguments")
    print('Usage: python3 csr-download-yang-modules-schemas.py <container_name>')
    print('Example: python3 csr-download-yang-modules-schemas.pyy clab-telemetry-testbed-r1')
    exit(1)
else:
    container_name = sys.argv[1]
    check_container = subprocess.getoutput("docker ps -a | awk '{print $NF}' | grep " + container_name)

if check_container != container_name:
    print("Error - Incorrect arguments: You need to specify the container name of the network device.")
    print('Usage: python3 csr-download-yang-modules-schemas.py <container_name>')
    print('Example: python3 csr-download-yang-modules-schemas.py clab-telemetry-testbed-r1')
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

yang_module_name = ""
yang_module_revision = ""

"""
Retrieve the set of YANG modules supported by the network device and save the schema representation of 
the regarding YANG data model files.
"""
print("\n - Retrieving the YANG models supported by the network device "+ container_name + ": \n")
for capability_key in capabilities:
    capability = capabilities[capability_key]
    if "module" in capability.parameters:
        yang_module_name = capability.parameters['module']

        if "revision" in capability.parameters:
            yang_module_revision = capability.parameters['revision'] 
            # Execute the get-schema RPC to get the schema of a particular YANG module
            schema = session.get_schema(identifier=yang_module_name, version=yang_module_revision)
            # Save the YANG module schema as a YANG model file
            with open("./yang-models/{0}@{1}.yang".format(yang_module_name, yang_module_revision), 'w') as file:
                file.write(schema.data)
        else:
            yang_module_revision = None
            # Execute the get-schema RPC to get the schema of a particular YANG module
            schema = session.get_schema(identifier=yang_module_name, version=yang_module_revision)
            # Save the YANG module schema as a YANG model file
            with open("./yang-models/{0}.yang".format(yang_module_name), 'w') as file:
                file.write(schema.data)

session.close_session()