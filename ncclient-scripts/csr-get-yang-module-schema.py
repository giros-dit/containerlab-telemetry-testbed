import sys
import subprocess
from ncclient import manager

if len(sys.argv) < 3:
    print("Error - Incorrect arguments")
    print('Usage: python3 csr-get-yang-module-schema.py <container_name> <yang-module-name> [<yang-module-revision>]')
    print('Example: python3 csr-get-yang-module-schema.py clab-telemetry-testbed-r1 ietf-interfaces 2014-05-08')
    exit(1)
else:
    container_name = sys.argv[1]
    check_container = subprocess.getoutput("docker ps -a | awk '{print $NF}' | grep " + container_name)

if check_container != container_name:
    print("Error - Incorrect arguments: You need to specify the container name of the network device.")
    print('Usage: python3 csr-get-yang-module-schema.py <container_name> <yang-module-name> [<yang-module-revision>]')
    print('Example: python3 csr-get-yang-module-schema.py clab-telemetry-testbed-r1 ietf-interfaces 2014-05-08')
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

yang_module_name = sys.argv[2]

if len(sys.argv) == 4:
    yang_module_revision = sys.argv[3]
else:
    yang_module_revision = None

# Execute the get-schema RPC to get the schema of a particular YANG module
schema = session.get_schema(identifier=yang_module_name, version=yang_module_revision)
# Get RPC reply with the YANG module schema
print(schema)

session.close_session()