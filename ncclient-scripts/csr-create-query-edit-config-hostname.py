import sys
import subprocess
from ncclient import manager
from jinja2 import Template

if len(sys.argv) < 3:
    print("Error - Incorrect arguments")
    print('Usage: python3 csr-create-query-edit-config-hostname.py <container_name> <hostname>')
    print('Example: python3 csr-create-query-edit-config-hostname.py clab-telemetry-testbed-r1 r1-ios-xe-csr1000v')
    exit(1)
else:
    container_name = sys.argv[1]
    check_container = subprocess.getoutput("docker ps -a | awk '{print $NF}' | grep " + container_name)

if check_container != container_name:
    print("Error - Incorrect arguments: You need to specify the container name of the network device.")
    print('Usage: python3 csr-create-query-edit-config-hostname.py <container_name> <hostname>')
    print('Example: python3 csr-create-query-edit-config-hostname.py clab-telemetry-testbed-r1 r1-ios-xe-csr1000v')
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

# Render our Jinja template
hostname_template = Template(open('./jinja2-templates/hostname-native.xml').read())
hostname_rendered = hostname_template.render(
    HOSTNAME = sys.argv[2]
)

# Execute the edit-config RPC
reply = session.edit_config(target="running", config=hostname_rendered)

print("\nEditing hostname of network device "+ container_name + " ...\n")

print(reply)

session.close_session()